# Development environments

Apple Mac OS uses python for its own operations, so it is very important to isolate the development environment from the operation of the OS to avoid compromising the integrity of the whole system. So virtualenv can be used, but in today world, docker and pipenv are the way to go as they:

* avoid installing softwares and libraries not often used on the native OS
* describe the dependencies on library so programs developed 5 years ago should still run
* easy to switch laptop
* quicker provisioning than a VM running with Vagrant, still offering mounting host folder, running under localhost
* use docker compose for each project to manage component dependencies
* still use virtual environment to isolate per project if needed

## Clone this project

```
git clone https://github.com/jbcodeforce/python-code
cd python-code
```

There are two ways to do environment isolation: docker or virtual env, and in fact it is recommended to combine both.

## Use docker image

The Dockerfile in the current project define an image for running python 3.7 with Flask, pytest, panda and other libraries.

To build the image you need docker engine and do the following

```
docker build -t jbcodeforce/python37 . 
```

Then start the image as container with the command below, which also mount your local folder to the /home folder inside the docker container

``` 
docker run -e DISPLAY=192.168.1.89:0 --name pythonenv -v $(pwd):/home/ -it --rm -p 5000:5000 jbcodeforce/python37 bash
```

!!! note
        The script named `startPythonDocker.sh` performs this command above.

The docker image includes pipenv for improving the management of the dependencies. 

### Use pipenv

[Pipenv](https://github.com/pypa/pipenv) offers the last best practices from other language to manage virtual environment and dependencies for Python. Adding and removing packages is also updating the dependencies descriptor file: Pipfile. 
It basically combine pip and virtualenv.

To install it on the mac:

```shell
brew install pipenv
```

*When using the docker image you do not need to install pipenv on the host*.

It is also available in the docker image so the following commands should work from the bash inside the docker container.

```shell
# Create a new project using Python 3.7
pipenv --python 3.7
# start the virtual env shell
pipenv shell
# or start a python interpreter
pipenv run python
# or run a program with python interpreter
pipenv run python FaustEasiestApp.py
# install dependencies including dev
pipenv install --dev
#Check your installed dependencies for security vulnerabilities:
pipenv check
# print a pretty graph of all your installed dependencies.
pipenv graph 
# Uninstalls all packages not specified in Pipfile.lock.
pipenv clean
# lock dependencies
pipenv lock
```

### Run the python interpreter

Start `python` in the container shell:

```shell
root@485cff8245df:/home#  python
Python 3.7.4 (default, Jul  9 2019, 00:06:43) 
[GCC 6.3.0 20170516] on linux
>>> 
```

Use `exit()` to get out of the python interpreter, and Ctrl D for getting out of the Docker container.

### Using graphics inside the python container 

The approach is to run graphics program inside python interpreter, but the windows will appear on the host machine (the Mac). To do so we need a bidirectional communication between the docker container and the Mac. This is supported by the `socat` tool. To install it the first time do the following:

```shell
brew install socat
```

When installed, open a new terminal and start socat with the command:

```shell
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```

As the container is running X window system, we need to also install a X system on Mac. This is done via the `Xquartz` program:

```shell
brew install xquartz
```

Then start Xquartz from the application or using

```shell
open -a Xquartz
```

A white terminal window will pop up. The first time Xquartz is started,  open up the `preferences` menu and go to the `security` tab. Then select “allow connections from network clients” to check it `on`.

See [this note from Nils De Moor](https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc) for more information.



