import pandas as pd
from pandas_logger import enable_pandas_logging, disable_pandas_logging


def random_operations(df):
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="b")
    df1 = df.merge(df, how="outer", on="a")
    df.sort_values("a", inplace=True)
    df = pd.merge(df, df, on="a")
    df.dropna(inplace=True)
    df = pd.Series([1, 3, 4])
    df = df.isnull()
    return df


if __name__ == "__main__":
    # Add these lines
    print("Enabling Logging")
    enable_pandas_logging()
    df = pd.DataFrame([[1, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
    print(random_operations(df.copy()))
    print("Disabling Logging")
    disable_pandas_logging()
    print(random_operations(df))