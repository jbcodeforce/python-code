# uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package (to replace pip) and project manager (for virtual env). 

## Value propositions

* uv manages project dependencies and environments.
* uv installs different Python version and allows switching between versions.
* optimize dependencies caching and avoid deduplication

[See features list and basic commands](https://docs.astral.sh/uv/getting-started/features/)


## Getting started:

* [installation](https://docs.astral.sh/uv/getting-started/installation/)
* [Common commands](https://docs.astral.sh/uv/getting-started/features/):
    ```sh
    uv python install: Install Python versions.
    uv python list: View available Python versions.
    uv python find: Find an installed Python version.
    uv run: Run a script.
    uv add --script: Add a dependency to a script
    uv remove --script: Remove a dependency from a script
    uv self update: upgrade version
    ```

* Work with [virtual environment](https://docs.astral.sh/uv/pip/environments/)
    ```sh
    uv venv
    uv venv --python 3.13
    uv python pin 3.13
    deactivate
    ```

* [Working with Python project](https://docs.astral.sh/uv/guides/projects/) using `uv init`.
    * [See understanding project type](https://pydevtools.com/handbook/explanation/understanding-uv-init-project-types/)
    * [pyproject.toml guide.](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
    * [Manage dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/)

* Work with [tools](https://docs.astral.sh/uv/guides/tools/) to publish as python package
    ```sh
    uv tool run: Run a tool in a temporary environment.
    uv tool install: Install a tool user-wide.
    uv tool uninstall: Uninstall a tool.
    uv tool list: List installed tools.
    uv tool update-shell: Update the shell to include tool executables.
    ```

## Some interesting things to do

* Check version: `uv version`
* Use different python version
* Use / create project (create a `pyproject.toml`) [See project guide.](https://docs.astral.sh/uv/guides/projects/)
* Run script in the context of a project to get access to modules: `uv run python ...`
* Manage dependencies: `uv add --script` or `uv remove --script`
* [Full CLI reference](https://docs.astral.sh/uv/reference/cli/)

## Projects I am using it

* [Move to real-time with Shift left](https://jbcodeforce.github.io/shift_left) to develop a CLI
