import inspect
import logging
from functools import wraps

import pandas as pd

import pandas_logger.settings as settings

__IS_WRAPPED_ALREADY__ = False


def log_pandas_methods(func, logger=None):

    if logger is None:
        logging.basicConfig(
            format="PDLogger: %(asctime)s - %(message)s", level=logging.INFO
        )
        logger = logging.getLogger(__name__)

    @wraps(func)
    def inner(*args, **kwargs):
        logger.info(f"Calling {func.__name__}")
        log_func_details(logger, func, *(args[1:]), **kwargs)
        if args and isinstance(args[0], (pd.DataFrame, pd.Series)):
            logger.info(f"Initial shape: {args[0].shape}")
        ret_val = func(*args, **kwargs)
        if ret_val is not None and isinstance(ret_val, (pd.DataFrame, pd.Series)):
            logger.info(f"Final shape: {ret_val.shape}")
        elif ret_val is None:
            logger.info(f"Final shape: {args[0].shape}")
        return ret_val

    return inner


def log_func_details(logger, func, *args, **kwargs):

    keywords = dict((zip(inspect.getfullargspec(func).args[1:], args)))
    keywords.update(kwargs)
    logger.info(f"Provided Arguments: {keywords}")


def wrap_methods(cls, wrapper, methods, logger=None):
    for key, value in cls.__dict__.items():
        if hasattr(value, "__call__"):
            if value.__name__ in methods:
                setattr(cls, key, wrapper(value, logger))


def unwrap_methods(cls, methods):
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
