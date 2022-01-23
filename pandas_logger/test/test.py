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