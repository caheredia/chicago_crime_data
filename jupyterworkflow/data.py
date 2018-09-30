from urllib.request import urlretrieve
import os
import pandas as pd

DATA_URL = 'https://data.consumerfinance.gov/api/views/s6ew-h6mp/rows.csv?accessType=DOWNLOAD'


def get_url_data(filename='data/ccd.csv', url=DATA_URL, force_download=False):
    '''Download and cache the Fremont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if TRUE, then force data download

    Returns
    -------
    data : pandas.DataFrame
        The Fremont Bridge data
    '''
    if not os.path.exists(filename) or force_download:
        print('...downloading data')
        urlretrieve(URL, filename)

    print('...loading csv')
    data = pd.read_csv(filename, index_col='Date received')

    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    return data