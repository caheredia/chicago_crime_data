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

    return data



def convert_time(data, column_name='Time Occurred'):
    '''Formats the time column to length of 4. 

    Pads the begining of Time stamp to length of 4. Creates a new column with full stamp as a timestamp index. 

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
        Chicago crime stamps. 
    '''
     # convert time to string from int
    data[column_name] = data[column_name].apply(str)
    
    # pad time for lengths less than 4
    data[column_name] = data[column_name].apply(str_pad)
    
    data['Date'] = data['Date Reported'] + " " + data['Time Occurred']
    data.set_index('Date', inplace=True)

    try:
        data.index = pd.to_datetime(data.index,  format='%m/%d/%Y %H%M')
    except TypeError:
        data.index = pd.to_datetime(data.index)
        
        
    return data
    
def str_pad(time_stamp):
    ''' 
    Pads the begining of string with 0 until length 4 is reached. 

    Parameters
    ----------
    time_stamp : string
       string for 
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if TRUE, then force data download

    Returns
    -------
    data : pandas.DataFrame
        The Fremont Bridge data
    '''
    
    if len(time_stamp) < 4:
        new_string = str_pad( '0' + time_stamp)
    else:
        new_string =  time_stamp
    return new_string