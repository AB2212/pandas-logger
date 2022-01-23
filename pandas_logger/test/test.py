import logging

import numpy as np
import pandas as pd

from pandas_logger import pdlogger

logging.basicConfig(format="PDLogger: %(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

pdlogger.enable_logging(logger=logger)

from pandas.conftest import *
from pandas.tests.frame.conftest import *
from pandas.tests.frame.methods.test_drop_duplicates import *
from pandas.tests.frame.methods.test_sort_values import *
from pandas.tests.frame.methods.test_dropna import *

# tests_to_exclude = [
#     "test_drop_duplicates_pos_args_deprecation",
#     "TestDataFrameMissingData",
#     "test_sort_values_pos_args_deprecation",
# ]
# for name in tests_to_exclude:
#     if name in globals():
#         del globals()[name]
