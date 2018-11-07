.. Chicago_Crime_Data documentation master file, created by
   sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Chicago Crime Data documentation
==============================================

An exploration of reported Chicago Crime data. This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from the Chicago Police Department’s CLEAR (Citizen Law Enforcement Analysis and Reporting) system.


This report visually explores the data for trends. It also looks for trends using PCA and Gaussian Mixture Models. Through the latter, we see the crime reporting behaves in two distinct patterns: Weekday and Weekend. Weekday crime reporting tends to peak around noon. For Weekends, the flux of crime reports is steady throughout the day.


However, we do see some weekdays behave like weekends, and conversely, some weekends behave like weekdays. Specifically, there are Tuesdays that behave like weekends, i.e. more crime is reported. Some of those happen to be Christmas, New Years, and July 4th—American holidays. And the two Sundays that behaved like weekdays coincide with playoff games, which might say more about Chicagoans than it’s reported crime rates do.


In summary, more crimes are reported (or perhaps committed?) during hours of leisure.

Code on `github <https://github.com/caheredia/chicago_crime_data/>`_

Contents:

.. toctree::
   :maxdepth: 2


   README
   modules

Analysis
====================
Jupyter notebook contents:

.. toctree::
   :maxdepth: 2

   0.1-cristian-Chicago_Crime.ipynb



Index
====================
* :ref:`genindex`
* :ref:`search`
