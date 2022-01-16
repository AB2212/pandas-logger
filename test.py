import pandas as pd
import numpy as np
from pandas_logger import enable_pandas_logging, disable_pandas_logging
import doctest

if __name__ == "__main__":
    enable_pandas_logging()
    doctest.run_docstring_examples(pd.DataFrame.drop_duplicates, globals().copy(), True)
