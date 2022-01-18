import pandas as pd
from pandas_logger import logger


def random_operations(df):
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="b")
    df = df.merge(df, how="outer", on="a")
    df.sort_values("a", inplace=True)
    df.dropna(inplace=True)
    df = pd.Series([1, 3, 4])
    df = df.isnull()
    return df


if __name__ == "__main__":
    print("Enabling Logging")
    logger.enable_pandas_logging()
    df = pd.DataFrame([[1, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
    print(random_operations(df.copy()))
    print("Disabling Logging")
    logger.disable_pandas_logging()
    print(random_operations(df))
