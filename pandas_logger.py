from functools import wraps
import pandas as pd
import logging
import settings

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
__IS_WRAPPED_ALREADY__ = False

def log_pandas(func):
    @wraps(func)
    def inner(*args, **kwargs):
        logger.info(f"Calling {func.__name__}")
        if args and isinstance(args[0], (pd.DataFrame, pd.Series)):
            logger.info(f"Initial shape: {args[0].shape}")
        log_func_details(func, *args, **kwargs)
        ret_val = func(*args, **kwargs)
        if ret_val is not None and isinstance(ret_val, (pd.DataFrame, pd.Series)):
            logger.info(f"Final shape: {ret_val.shape}")
        elif ret_val is None:
            logger.info(f"Final shape: {args[0].shape}")
        return ret_val

    return inner


def log_func_details(func, *args, **kwargs):
    name = func.__name__
    if name == "sort_values":
        sort_by = kwargs.get("by", None)
        if sort_by is None and len(args) > 1:
            sort_by = args[1]
        if sort_by is not None:
            logger.info(f"Sorting values by: {sort_by}")
    elif name == "drop_duplicates":
        subset = kwargs.get("subset", None)
        if subset is None and len(args) > 1:
            subset = args[1]
        if subset is not None:
            logger.info(f"Subsetting columns: {subset}")


def wrap_methods(cls, wrapper, methods):
    for key, value in cls.__dict__.items():
        if hasattr(value, "__call__"):
            if value.__name__ in methods:
                setattr(cls, key, wrapper(value))

def unwrap_methods(cls, methods):
    for key, value in cls.__dict__.items():
        if hasattr(value, "__call__"):
            if value.__name__ in methods:
                if hasattr(value, "__wrapped__"):
                    setattr(cls, key, value.__wrapped__)

def enable_pandas_logging():
    global __IS_WRAPPED_ALREADY__
    if not __IS_WRAPPED_ALREADY__:
        for cls in [pd.DataFrame, pd.Series]:
            wrap_methods(cls, log_pandas, settings.METHODS)

        for func in settings.FUNCTIONS:
            setattr(pd, func, log_pandas(getattr(pd, func)))

        __IS_WRAPPED_ALREADY__ = True
    

def disable_pandas_logging():
    global __IS_WRAPPED_ALREADY__
    if __IS_WRAPPED_ALREADY__:
        for cls in [pd.DataFrame, pd.Series]:
            unwrap_methods(cls, settings.METHODS)

        for func in settings.FUNCTIONS:
            wrapped_func = getattr(pd, func)
            if hasattr(wrapped_func, '__wrapped__'):
                setattr(pd, func, getattr(pd, func).__wrapped__)
                
        __IS_WRAPPED_ALREADY__ = False




    