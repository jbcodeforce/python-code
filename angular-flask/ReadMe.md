# Python Flask WebApp

## Code Structure

## Execution
Start docker python development environment
```
docker run -e DISPLAY=192.168.1.89:0 --name jbcodeforcepython -v $(pwd):/home/jbcodeforce/work --rm -it jbcodeforce/python37 /bin/bash
```
Start a virtual environment
```
$ python3.7 -n venv
$ source bin/activate
(angular-flask) jbcodeforce@210f0bbaad03:~/work/angular-flask$
```
Export the app and start it
```
 (angular-flask) jbcodeforce@210f0bbaad03:~/work/angular-flask$ export FLASK_APP=app.py
 (angular-flask) jbcodeforce@210f0bbaad03:~/work/angular-flask$ flask run
```
The start.sh script does those commands.
