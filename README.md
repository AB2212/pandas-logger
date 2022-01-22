# Pandas-Logger
Enables logging of pandas dataframe and series methods
## Example
```python
import os
os.chdir("../..")
import pandas as pd
from pandas_logger import logger
```


```python
def random_operations(df):
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="b")
    df = df.merge(df, how="outer", on="a")
    df.sort_values("a", inplace=True)
    df.dropna(inplace=True)
    df = pd.Series([1, 3, 4])
    df = df.isnull()
    return df
```


```python
print("Enabling Logging")
logger.enable_pandas_logging()
df = pd.DataFrame([[1, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
print(random_operations(df.copy()))
print("Disabling Logging")
logger.disable_pandas_logging()
print(random_operations(df))
```

    2022-01-22 18:41:56,955 - Calling drop_duplicates
    2022-01-22 18:41:56,956 - Provided Arguments: {}
    2022-01-22 18:41:56,956 - Initial shape: (3, 2)
    2022-01-22 18:41:56,959 - Final shape: (3, 2)
    2022-01-22 18:41:56,960 - Calling drop_duplicates
    2022-01-22 18:41:56,961 - Provided Arguments: {'subset': 'b'}
    2022-01-22 18:41:56,961 - Initial shape: (3, 2)
    2022-01-22 18:41:56,963 - Final shape: (3, 2)
    2022-01-22 18:41:56,967 - Calling sort_values
    2022-01-22 18:41:56,968 - Provided Arguments: {'by': 'a', 'inplace': True}
    2022-01-22 18:41:56,969 - Initial shape: (5, 3)
    2022-01-22 18:41:56,971 - Final shape: (5, 3)
    2022-01-22 18:41:56,971 - Calling dropna
    2022-01-22 18:41:56,972 - Provided Arguments: {'inplace': True}
    2022-01-22 18:41:56,972 - Initial shape: (5, 3)
    2022-01-22 18:41:56,977 - Final shape: (2, 3)
    

    Enabling Logging
    0    False
    1    False
    2    False
    dtype: bool
    Disabling Logging
    0    False
    1    False
    2    False
    dtype: bool
    
