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
    df.sort_values("a", inplace=True)
    new_df = df.drop_duplicates(subset="b")
    new_df.dropna(inplace=True)
    return new_df

logger.info("Enable Logging")
pdlogger.enable_logging(logger=logger)
df = pd.DataFrame([[5, -2], [3, 4], [3, pd.NA]], columns=["a", "b"])
df_modified = random_operations(df.copy())
logger.info(f'Modified dataframe: \n{df_modified}')
logger.info("Disable Logging")
pdlogger.disable_logging()
df_modified = random_operations(df.copy())
logger.info(f'Modified dataframe: \n{df_modified}')
```

   PDLogger: 2022-01-23 10:49:13,002 - Enable Logging
   PDLogger: 2022-01-23 10:49:13,312 - Name: df
   PDLogger: 2022-01-23 10:49:13,313 - Calling method: drop_duplicates
   PDLogger: 2022-01-23 10:49:13,315 - Initial shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,317 - Final shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,317 - Rows dropped: 0
   PDLogger: 2022-01-23 10:49:13,319 - Columns dropped: 0
   PDLogger: 2022-01-23 10:49:13,338 - Name: df
   PDLogger: 2022-01-23 10:49:13,340 - Calling method: sort_values
   PDLogger: 2022-01-23 10:49:13,341 - Provided Arguments: {'inplace': True}
   PDLogger: 2022-01-23 10:49:13,343 - Initial shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,344 - Final shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,346 - Rows dropped: 0
   PDLogger: 2022-01-23 10:49:13,350 - Columns dropped: 0
   PDLogger: 2022-01-23 10:49:13,365 - Name: df
   PDLogger: 2022-01-23 10:49:13,366 - Calling method: drop_duplicates
   PDLogger: 2022-01-23 10:49:13,369 - Initial shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,370 - Final shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,370 - Rows dropped: 0
   PDLogger: 2022-01-23 10:49:13,371 - Columns dropped: 0
   PDLogger: 2022-01-23 10:49:13,387 - Name: new_df
   PDLogger: 2022-01-23 10:49:13,388 - Calling method: dropna
   PDLogger: 2022-01-23 10:49:13,392 - Initial shape: (3, 2)
   PDLogger: 2022-01-23 10:49:13,394 - Final shape: (2, 2)
   PDLogger: 2022-01-23 10:49:13,395 - Rows dropped: 1
   PDLogger: 2022-01-23 10:49:13,396 - Columns dropped: 0
   PDLogger: 2022-01-23 10:49:13,404 - Modified dataframe: 
      a   b
   1  3   4
   0  5  -2
   PDLogger: 2022-01-23 10:49:13,405 - Disable Logging
   PDLogger: 2022-01-23 10:49:13,413 - Modified dataframe: 
      a   b
   1  3   4
   0  5  -2
