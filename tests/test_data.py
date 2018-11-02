from src.data.get_data import get_url_data
from src.features.df_functions import str_pad, convert_time
import pandas as pd
import numpy as np

data = get_url_data()


def test_chicago_data():
    #assert all(data.columns == ['East', 'West', 'Total'])
    assert isinstance(data, pd.core.frame.DataFrame)
    #assert len(np.unique(data.index.time)) == 24
    assert len(data.columns) == 26


def test_index_conversion():
    converted_data = convert_time(data)
    assert isinstance(converted_data.index, pd.core.indexes.datetimes.DatetimeIndex)
