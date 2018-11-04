import pandas as pd


def convert_time(data, column_name='Time Occurred'):
    '''Formats the time column to length of 4.

    Pads the begining of Time stamp to length of 4.
    Converts column_name to string.
    Creates a new column with full stamp as a timestamp index.

    Parameters
    ----------
    data : pandas.DataFrame
        dataframe to modify
    column_name : string (optional)
        column containing hourly data


    Returns
    -------
    data : pandas.DataFrame
        Original dataframe with Chicago crime time stamps as DateTimeIndex.
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
    '''Pads the begining of string with 0 until length 4 is reached.

    If string is less than four characters, than a 0 is appended to head of string.
    This is done until string is at least 4 digits long. 

    Parameters
    ----------
    time_stamp : string
       string for

    Returns
    -------
    new_string : string
        padded string or original string
    '''

    if len(time_stamp) < 4:
        new_string = str_pad('0' + time_stamp)
    else:
        new_string = time_stamp
    return new_string
