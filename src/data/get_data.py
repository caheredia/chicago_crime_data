from urllib.request import urlretrieve
import os
import pandas as pd

DATA_URL = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'


def get_url_data(filename='data/raw/Crime_Data_from_2010_to_Present.csv', url=DATA_URL, force_download=False):
    '''
    Download and cache data from publisher.

    Verifies that data exists on local machine. If not, then downloads data.
    Can be foreced to download with parameter force_downloader.

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
    data = pd.read_csv(filename)

    return data
