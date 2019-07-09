# Development environments

Apple Mac OS uses python for its own operations, so it is very important to isolate the development environment from the operation of the OS to avoid compromising the integrity of the whole system. So virtualenv can be used, but in today world, docker presents a lot of advantages:

* avoid installing softwares and libraries not often used on the native OS
* describe the dependencies on library so programs developed 5 years ago should still run
* easy to switch laptop
* quicker provisioning than a VM running with Vagrant, still offering mounting host folder, running under localhost
* use docker compose for each project to manage component dependencies
* still use virtual environment to isolate per project if needed

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

### Run the python interpreter

Start `python` in the container shell:

```
root@485cff8245df:/home#  python
Python 3.7.4 (default, Jul  9 2019, 00:06:43) 
[GCC 6.3.0 20170516] on linux
>>> 
```

Use `exit()` to get out of the python interpreter, and Ctrl D for getting out of the Docker container.

## Virtual env

!!! note
        You do not need to use Virtual Env if using docker.

**virtualenv** is a tool for isolating your application in what is called a virtual environment. A virtual environment is a directory that contains the software on which your application depends. It changes your environment variables to keep your development environment contained. Instead of downloading packages, like Flask, to your system-wide — or user-wide — package directories, we can download them to an isolated directory used only for our current application.

You could install virtualenv with `pip install virtualenv` 

Create virtual environment under your project folder with the command:
`virtualenv -p /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4 .venv`

### Activate the virtual environment

The angular-flask project includes a start.sh script to prepare the virtual env.
```
source .venv/bin/activate

python3 programname.py

deactivate
```