import sys

sys.path.append("../pandas_logger")

import logging

import pandas as pd

from pandas_logger import pdlogger

logging.basicConfig(format="PDLogger: %(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def random_operations(df):
    df = df.drop_duplicates()
    df.sort_values("a", inplace=True)
    new_df = df.drop_duplicates(subset="b")
    new_df.dropna(inplace=True)
    return new_df


if __name__ == "__main__":

    logger.info("Enabling Logging")
    pdlogger.enable_logging(logger=logger)
    df = pd.DataFrame([[5, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
    df_modified = random_operations(df.copy())
    logger.info(f"Modified dataframe: \n {df_modified}")
    logger.info("Disabling Logging")
    pdlogger.disable_logging()
    df_modified = random_operations(df.copy())
    logger.info(f"Modified dataframe: \n{df_modified}")
