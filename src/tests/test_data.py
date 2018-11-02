from jupyterworkflow.data import get_fremont_data, add_ints
import pandas as pd
import numpy as np


def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['East', 'West', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time)) == 24


def test_add():
    assert add_ints(10, 5) == 15
    assert add_ints(-1, 1) == 0
    assert add_ints(-2, -3) == -5
    assert type(add_ints(10, 5)) == int
