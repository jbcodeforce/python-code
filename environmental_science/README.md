# Environmental Sciences

This folder includes different studies around environment sciences.

## Python and Jupiter notebook environment
### Set Python Environment using [uv](https://docs.astral.sh/uv/getting-started/)

Here are the quick start step to prepare an environement to run Python and Jupyter notebooks.

* Install uv (only one time) as a python package manager. More modern than `pip`
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

* Install a Python version (into ~/.local/bin)
    ```sh
    uv python list
    uv python install 3.13.7 --default
    # upgrade
    uv python upgrade 3.13
    ```

* Create a virtual environment in this folder
    ```sh
    uv venv
    # it will create a .venv in the current folder (which should be in .gitignore)
    ```

### Work from the virtual environment

* Activate with:
    ```sh
    source .venv/bin/activate
    ```
* Later when done use `deactivate` to get out of the virtual environment.

### Jupiter Lab and Notebooks


* Create a Kernel:  Kernels enable the Jupyter server to run in one virtual Python environment. Any packages installed from within the notebook are installed into the project's virtual environment. This is a different virtual environment than the one managed by uv, but it will be possible in the context of work done in a notebook to update libraries in uv venv.
    ```sh
    # install ipykernel as a development dependency
    uv add --dev ipykernel
    #  create the kernel `project` with:
    uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
    ```

    ![](./images/venv_jupyter.drawio.png)

* start a Jupyter server with access to the project's virtual environment but runs in its own isolated environment:
    ```sh
    uv run --with jupyter jupyter lab
    ```

    By default, jupyter lab will start the server at http://localhost:8888/lab

* When creating a notebook, select the `project` kernel from the dropdown.
    ![](./images/new_notebook.png)

### Start new python project with uv

When we need to do a python specific program, uv is the new Python project managment. Review the [project management with uv](https://docs.astral.sh/uv/concepts/projects/) documentation.

* Create a folder for the project
* Create a project to manage modules needed to do data sciences
    ```sh
    # This command was already executed in this folder
    uv init
    # -> will create `pyproject.toml` and `.python-version` files
    ```

* Add any libraries/modules needed (they are defined now in the pyproject.toml)
    ```sh
    uv sync
    # or manually 
    uv add pandas matplotlib earthpy seaborn
    ```


## Earth Data Science

The content of this folder includes Jupyter notebooks and Python code from the [earthdatascience.org](https://earthdatascience.org/) Flood tutorial.

### Flooding in Colorado

The [Lesson 1 precipitation and time series](https://earthdatascience.org/courses/use-data-open-source-python/use-time-series-data-in-python/introduction-to-time-series-in-pandas-python/) is implemented in the [01-flood-timeserie Jupyter notebook](./earth-analytics/01-flood-timeserie.ipynb). 

Here are the main concepts to learn:

* In most datasource, date are loaded as a string, and need to be transformed to time so records can be sorted. The `datetime` python module is used.
* The `earthpy` is a python package, from the University of Boulder, CO,  that makes it easier to plot and work with spatial raster and vector data using open source tools. It includes the following datasets:`['california-rim-fire', 'co-flood-extras', 'cold-springs-fire', 'cold-springs-landsat-scenes', 'cold-springs-modis-h4', 'colorado-flood', 'cs-test-landsat', 'cs-test-naip', 'naip-fire-crop', 'ndvi-automation', 'spatial-vector-lidar', 'twitter-flood', 'vignette-elevation', 'vignette-landsat']`

    ```python
    import earthpy as et
    data = et.data.get_data('colorado-flood')
    # BUT the data are saved under $HOME/earth-analytics/data/colorado-flood/ which is not conveniant.
    # so once downloaded it is possible to move to a project's data folder like $(pwd)/earth-analysis/data
    ```
* load csv file into Pandas Dataframe
    ```python
    boulder_precip_2003_2013 = pd.read_csv(file_path,
                                       # Make sure the dates import in datetime format
                                       parse_dates=['DATE'],
                                       # Set DATE as the index so you can subset data by time period
                                       index_col=['DATE'],
                                       # Mask no data values so they are not plotted / used in analysis
                                       na_values=['999.99'])
    ```

* To prepare the data the following common functions are used:
    ```python
    # pandas dataframe df
    df.describe()
    df.dtypes
    ```

    a value of 999 represents a no data value that needs to be removed from the data

* Set an index to the dataset. Once your date values are an index, you can more easily subset the data by time period.
* When using an index column, then .plot() will automatically select that column to plot on the x-axis.
* To extract the date for a given year, the DATE column can be transformed as datetime:
    ```python
    df['DATE'] = pecip_2003_3013.to_datetime(df['DATE'])
    # Then filter records for the year 2005
    df_2005 = df[df['DATE'].dt.year == 2005]
    ```
* Resampling time series data refers to the act of summarizing data over different time periods.

### Temperature

### Content summary

* The following content is created:
    * The colorado-flood Data set [from](https://ndownloader.figshare.com/files/16371473) is saved under [`earth-analytics/data/colorado-flood/`](./earth-analytics/data/colorado-flood/) folder. The data folder is ignored in .gitignore to avoid keeping a 155MB in Git
    * [First notebook is 01-flood-timeserie.ipynb](./earth-analytics/01-flood-timeserie.ipynb) to learn to load data, and work on data type, null values and plotting graphs. 
