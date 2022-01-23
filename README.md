# Pandas-Logger
Enables logging of dataframe and series methods
## Example
```python
import logging
import pandas as pd
from pandas_logger import pdlogger  

logging.basicConfig(format="PDLogger: %(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def random_operations(df):
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="b")
    df.sort_values("a", inplace=True)
    df.dropna(inplace=True)
    return df

logger.info("Enable Logging")
pdlogger.enable_logging(logger=logger)
df = pd.DataFrame([[5, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
df_modified = random_operations(df.copy())
logger.info(f'Modified dataframe: \n {df_modified}')
logger.info("Disable Logging")
pdlogger.disable_logging()
df_modified = random_operations(df.copy())
logger.info(f'Modified dataframe: \n{df_modified}')
```

    PDLogger: 2022-01-23 09:14:39,046 - Enable Logging
    PDLogger: 2022-01-23 09:14:39,049 - Calling drop_duplicates
    PDLogger: 2022-01-23 09:14:39,050 - Provided Arguments: {}
    PDLogger: 2022-01-23 09:14:39,052 - Initial shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,053 - Final shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,054 - Rows dropped: 0
    PDLogger: 2022-01-23 09:14:39,055 - Columns dropped: 0
    PDLogger: 2022-01-23 09:14:39,056 - Calling drop_duplicates
    PDLogger: 2022-01-23 09:14:39,058 - Provided Arguments: {'subset': 'b'}
    PDLogger: 2022-01-23 09:14:39,060 - Initial shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,061 - Final shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,062 - Rows dropped: 0
    PDLogger: 2022-01-23 09:14:39,063 - Columns dropped: 0
    PDLogger: 2022-01-23 09:14:39,063 - Calling sort_values
    PDLogger: 2022-01-23 09:14:39,064 - Provided Arguments: {'inplace': True}
    PDLogger: 2022-01-23 09:14:39,066 - Initial shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,067 - Final shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,067 - Rows dropped: 0
    PDLogger: 2022-01-23 09:14:39,070 - Columns dropped: 0
    PDLogger: 2022-01-23 09:14:39,071 - Calling dropna
    PDLogger: 2022-01-23 09:14:39,072 - Provided Arguments: {'inplace': True}
    PDLogger: 2022-01-23 09:14:39,076 - Initial shape: (3, 2)
    PDLogger: 2022-01-23 09:14:39,077 - Final shape: (2, 2)
    PDLogger: 2022-01-23 09:14:39,078 - Rows dropped: 1
    PDLogger: 2022-01-23 09:14:39,079 - Columns dropped: 0
    PDLogger: 2022-01-23 09:14:39,083 - Modified dataframe: 
       a   b
    1  3   4
    0  5  -2
    PDLogger: 2022-01-23 09:14:39,084 - Disable Logging
    PDLogger: 2022-01-23 09:14:39,092 - Modified dataframe: 
       a   b
    1  3   4
    0  5  -2    