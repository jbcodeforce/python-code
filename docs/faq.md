# FAQ

## Why pipenv

pipenv resolves the problem of dependencies management, that is not perfectly done in the requirements.txt, which leads to underterministic build process. Given the same input (the requirements.txt file), pip doesn’t always produce the same environment. `pip freeze` helps to freeze the dependencies and update your requirements.txt. But any dependency change needs to be done manually, and you need to track the dependent package version, for bug fix, or mandatory security fixes.

A second problem is the system wide repository used by pip. When developing multiple different projects in parallele that could become a real issue. `pipenv` use a per project environment.
pipenv acts as pip + virtual environment. It uses Pipfile to replace requirements.txt and pipfile.lock for determnistic build. See [this guide](https://realpython.com/pipenv-guide/) for command examples.