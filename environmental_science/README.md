# Environmental Sciences

This folder includes different studies for environment sciences.

## Set Environment using [uv](https://docs.astral.sh/uv/getting-started/)
Here are the quick start step to prepare an environement to run Python and Jupyter notebooks.

* Installl uv
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
    # it will create a .venv in the current folder (which should .gitignore)
    ```

* Activate with:
    ```sh
    source .venv/bin/activate
    ```

Review the [project management with uv](https://docs.astral.sh/uv/concepts/projects/) documentation.

* Create a project to manage modules needed to do data sciences
    ```sh
    # This command was already executed in this folder
    uv init
    # -> will create `pyproject.toml` and `.python-version` files
    ```

* The libraries/modules needed (they are defined now in the pyproject.toml)
    ```sh
    uv sync
    # or manually 
    uv add pandas matplotlib earthpy seaborn
    ```

## Jupiter Lab and Notebooks


* Create a Kernel:  Kernels enable the Jupyter server to run in one environment. Any packages installed from within the notebook are installed into the project's virtual environment. This is a different virtual environment managed by uv, but it will be possible in the context of work done in a notebook to update libraries in uv venv.
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


### Flooding in Colorado

This is the first step to get a high level overview of working with dates using Pandas and time series with Python datetimes

* [Data set to download here,](https://ndownloader.figshare.com/files/16371473) and save under data folder. It is ignored in .gitignore to avoid keeping a 155MB in Git
* [First notebook is 01-flood-timeserie.ipynb](./earth-analytics/01-flood-timeserie.ipynb)
