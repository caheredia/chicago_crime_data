def generic_plot(filename):
    """This makes a generic plot.

    A generic plot that accepts a dataframe. The df is assumed to have a datetime index.

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


    """
