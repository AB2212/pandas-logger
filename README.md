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

    PDLogger: 2022-01-22 19:43:40,027 - Enable Logging
    PDLogger: 2022-01-22 19:43:40,033 - Calling drop_duplicates
    PDLogger: 2022-01-22 19:43:40,035 - Provided Arguments: {}
    PDLogger: 2022-01-22 19:43:40,036 - Initial shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,038 - Final shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,039 - Calling drop_duplicates
    PDLogger: 2022-01-22 19:43:40,041 - Provided Arguments: {'subset': 'b'}
    PDLogger: 2022-01-22 19:43:40,042 - Initial shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,045 - Final shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,046 - Calling sort_values
    PDLogger: 2022-01-22 19:43:40,047 - Provided Arguments: {'by': 'a', 'inplace': True}
    PDLogger: 2022-01-22 19:43:40,048 - Initial shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,050 - Final shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,051 - Calling dropna
    PDLogger: 2022-01-22 19:43:40,052 - Provided Arguments: {'inplace': True}
    PDLogger: 2022-01-22 19:43:40,053 - Initial shape: (3, 2)
    PDLogger: 2022-01-22 19:43:40,063 - Final shape: (2, 2)
    PDLogger: 2022-01-22 19:43:40,068 - Modified dataframe: 
        a   b
    1  3   4
    0  5  -2
    PDLogger: 2022-01-22 19:43:40,070 - Disable Logging
    PDLogger: 2022-01-22 19:43:40,084 - Modified dataframe: 
       a   b
    1  3   4
    0  5  -2