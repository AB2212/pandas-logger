import inspect
import logging
from functools import wraps
from typing import Any, Callable, Union

import pandas as pd

import pandas_logger.settings as settings
import re

__IS_WRAPPED_ALREADY__ = False


def log_pandas_methods(func: Callable[..., Any], logger=None) -> Callable[..., Any]:

    if logger is None:
        logging.basicConfig(
            format="PDLogger: %(asctime)s - %(message)s", level=logging.INFO
        )
        logger = logging.getLogger(__name__)

    @wraps(func)
    def inner(*args, **kwargs):
        
        method_name = func.__name__
        # get instance name
        code_context = inspect.stack()[1].code_context
        # TODO: move to utils
        # FIXME: code_context may be multiple lines and 
        var_name = re.findall(f"([A-Za-z\_]+[A-Za-z0-9\_]+)\.{method_name}",
         " ".join(code_context).strip())
        if len(var_name) == 1:
            logger.info(f"Name: {var_name[0]}")

        logger.info(f"Calling method: {method_name}")
        if args:
            log_method_details(logger, func, *(args[1:]), **kwargs)
        
        initial_info = None
        final_info = None

        if args and isinstance(args[0], (pd.DataFrame, pd.Series)):
            
            initial_info = get_info(args[0])
        ret_val = func(*args, **kwargs)

        if ret_val is not None and isinstance(ret_val, (pd.DataFrame, pd.Series)):
            final_info = get_info(ret_val)
        elif ret_val is None and args is not None:
            final_info = get_info(args[0])

        log_info(logger, initial_info, final_info)

        return ret_val

    return inner


def log_method_details(logger, func: Callable[..., Any], *args, **kwargs):

    if not args:
        return
    keywords = dict((zip(inspect.getfullargspec(func).args[1:], args)))
    keywords.update(kwargs)
    logger.info(f"Provided Arguments: {keywords}")


def get_info(df: Union[pd.DataFrame, pd.Series]) -> dict:

    if df is None or not isinstance(df, (pd.DataFrame, pd.Series)):
        return

    info = dict()
    info['name'] = None
    if hasattr(df, 'name') and isinstance(df.name, str,):
        info['name'] = df.name
    info["shape"] = df.shape
    info["index"] = df.index.tolist()

    if isinstance(df, pd.DataFrame):
        info["columns"] = df.columns.tolist()
    elif isinstance(df, pd.Series):
        pass
    return info


def log_info(logger, initial_info: dict, final_info: dict):

    if initial_info.get('name', None) is not None:
        logger.info(f"Name:  {initial_info['name']}")

    logger.info(f"Initial shape: {initial_info['shape']}")
    logger.info(f"Final shape: {final_info['shape']}")

    rows_added = final_info["shape"][0] - initial_info["shape"][0]
    logger.info(f"Rows {'dropped' if rows_added <=0 else 'added'}: {abs(rows_added)}")

    if len(initial_info["shape"]) > 1 and len(final_info["shape"]) > 1:
        columns_added = final_info["shape"][1] - initial_info["shape"][1]
        logger.info(
            f"Columns {'dropped' if columns_added <=0 else 'added'}: {abs(columns_added)}"
        )

    return


def wrap_methods(
    cls: Class,
    wrapper: Callable[[Callable[..., Any]], None],
    methods: Callable[..., Any],
    logger=None,
):
    for key, value in cls.__dict__.items():
        if hasattr(value, "__call__"):
            if value.__name__ in methods:
                setattr(cls, key, wrapper(value, logger))


def unwrap_methods(cls: Class, methods: Callable[..., Any]):
    for key, value in cls.__dict__.items():
        if hasattr(value, "__call__"):
            if value.__name__ in methods:
                if hasattr(value, "__wrapped__"):
                    setattr(cls, key, value.__wrapped__)


def enable_logging(logger=None):
    global __IS_WRAPPED_ALREADY__
    if not __IS_WRAPPED_ALREADY__:
        for cls in [pd.DataFrame, pd.Series]:
            wrap_methods(cls, log_pandas_methods, settings.METHODS, logger)
        # TODO: add functionality for function under 'pd'
        # for func in settings.FUNCTIONS:
        #     setattr(pd, func, log_pandas_methods(getattr(pd, func)))

        __IS_WRAPPED_ALREADY__ = True


def disable_logging():
    global __IS_WRAPPED_ALREADY__
    if __IS_WRAPPED_ALREADY__:
        for cls in [pd.DataFrame, pd.Series]:
            unwrap_methods(cls, settings.METHODS)

        # TODO: add functionality for function under 'pd'
        # for func in settings.FUNCTIONS:
        #     wrapped_func = getattr(pd, func)
        #     if hasattr(wrapped_func, '__wrapped__'):
        #         setattr(pd, func, getattr(pd, func).__wrapped__)

        __IS_WRAPPED_ALREADY__ = False
