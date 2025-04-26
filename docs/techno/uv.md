# uv

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project manager. 

* [Installation](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)

## Value propositions

* uv manages project dependencies and environments.
* uv installs Python and allows quickly switching between versions.
* It is a replacement for common pip, pip-tools, and virtualenv commands

[See features list and basic commands](https://docs.astral.sh/uv/getting-started/features/)

## Some interesting things to do

* Check version: `uv version`
* Use different python version
* Use / create project (create a `pyproject.toml`) [See project guide.](https://docs.astral.sh/uv/guides/projects/)
* Run script in the context of a project to get access to modules: `uv run python ...`
* Manage dependencies: `uv add --script` or `uv remove --script`
* [Full CLI reference](https://docs.astral.sh/uv/reference/cli/)

## Projects I am using it

* [Move to real-time with Shift left](https://jbcodeforce.github.io/shift_left) to develop a CLI
