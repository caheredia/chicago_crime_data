from urllib.request import urlretrieve
import os
import pandas as pd

DATA_URL = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'


def get_url_data(filename='data/Crime_Data_from_2010_to_Present.csv', url=DATA_URL, force_download=False):
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
    data = pd.read_csv(filename)
    
    # convert time to string from int
    data['Time Occurred'] = data['Time Occurred'].apply(str)

    # filter strings of length 4 
    pattern = r'^\w{4,}$'
    time_filter = data['Time Occurred'].str.contains(pattern)

    # filter out bad time strings 
    data = data[time_filter]

    data['Date'] = data['Date Reported'] + " " +  data['Time Occurred']
    data.set_index('Date', inplace=True)
    
    try: 
        data.index = pd.to_datetime(data.index,  format='%m/%d/%Y %H%M')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    return data