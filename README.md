Chicago Crime Data README
==============================

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system.

An exploration of reported Chicago Crime data

See report and documentation [here](https://caheredia.github.io/chicago_crime_data/build/html/index.html)

Data Publishers
------------
- https://catalog.data.gov/dataset/crimes-2001-to-present-398a4
- https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Map/c4ep-ee5m



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make test` or `make data`.
    ├── README.md          <- The top-level README.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── .ipynb files       <- Jupyter notebooks, analysis files.           
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The environment file for reproducing the analysis environment.
    │                      
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── get_data.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── df_functions.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
