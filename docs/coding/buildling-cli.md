# Building CLI

In lot of solution project it is interesting to build custom cli to offer a simplest set of command. Design a good CLI is not easy, but since recent years there are a lot of CLIs offered by different vendors  that are very user friendly to use. The approach is also to be able to package the code as a module and also as a cli.

They are multiple solutions to develop CLI:

* Click with Poetry
* Poetry and Typer
* UV and Typer: modern and rapid new package manager

## Project structure

The git repository should have source code for the different components, mkdoc docs and IaC at the minimum. Then each package will have its own folder under src and tests.

<git-repo-name>
    src
       <module-name>/src
        
    tests

[See my CLI for shift-left project](https://github.com/jbcodeforce/shift_left_utils/tree/main/src/shift_left)

## Click

See [Click product documentation](https://click.palletsprojects.com/en/stable/), here are some valuable arguments for click:

* created for the Flask project
* argparse does not allow proper nesting of commands
* Commands can be attached to other commands of type Group. Flexible way to add command to groups

## Typer

[Product main page and documentation](https://typer.tiangolo.com/):

* It is based on Click
* Use same design as FastAPI

## A project using uv, Typer and click

This section is a quick summary of what may be done to build a CLI for the [shift-left project]() for flink-test-harness CLI.

### Pre-requisites

* [uv cli for package management](https://docs.astral.sh/uv/)for installation
* The cli project is a subproject of a bigger repository.

### Design considerations

* Develop foundation modules use by the cli and to package as an independent pypi library.
* Unit test modules
* Unit test cli

### Steps

* Under the main project src folder, initialize a new uv project:

```sh
uv init --app --package flink-test-harness
# --app tells uv that we will write an application
# --package tells uv that we will want to build a package out of our code to distribute it 
```

* In the src/flink-test-harness/main.py add the Typer based commands to define the basic cli. [See product documentation](https://typer.tiangolo.com/tutorial/first-steps/).
* Be sure to have the good alias and references in the `pyproject.toml` file

```yaml
[project.scripts]
flink-test-harness = "flink_test_harness.main:app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/flink_test_harness"]
```

* Run unit test for the module

```sh
uv run tests/core/test_inventory_mgr.py
```

* Run unit test for the cli

```sh
uv run tests/cli/test_project_cli.py
```

* Run the cli using uv

```sh
uv run flink-test-harness greet jerome
# other example
uv run shit_left
```

[See shift_left project]()

* Build the module

```
uv build
```

* To install the tool locally with uv

```sh
uv tool install . -e  
```

* test the installed tool

```sh
shift_left --help
```

* uninstall

```sh
uv tool list
uv tool uninstall shift-left 
```

* To build the wheel packaging

```sh
uv build
```

* Share the wheel and install in a python env via pip or uv

## Some tricks

* Get the full documentation in markdown of all the options

```
typer src/shift_left/cli.py utils docs
```