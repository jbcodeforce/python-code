# [Python Studies](http://jbcodeforce.github.io/python-code)

Read in [book format](http://jbcodeforce.github.io/python-code)

## Samples in this repo

* See list [here](https://jbcodeforce.github.io/python-code/#code-in-the-order-of-knowledge-acquisition).

## Python shell tricks

* Placing cursor to previous line and enter will copy the line to a new line.

## Dockerfiles

For better environment isolation we should use docker instead of virtual environment, it will be more portable and shareable. Different dockerfiles are defined in the different folder for the different studies.

* DockerfileForEnv -> jbcodeforce/python with pandas, numpy, flask. Server as base image

    ```sh
    docker build -f DockerfileForEnv -t jbcodeforce/python .
    ```
* Docker file for Flask app: [Flask/Dockerfile](https://github.com/jbcodeforce/python-code/blob/master/Flask/Dockerfile)
