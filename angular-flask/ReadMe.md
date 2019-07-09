# Python Flask WebApp
This is yet another sample to do flask app. This one with one angular page ready to grow and a user login with rest api ready.

## Code Structure

### Simplest flask app

The simplest Flask app is presented [in the quickstart](http://flask.pocoo.org/docs/1.0/quickstart/) and the matching code is under `helloworld/firstApp.py`. To execute it:

```
export FLASK_APP=firstApp.py
flask run
 * Serving Flask app "firstApp"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Dec/2018 20:49:42] "GET / HTTP/1.1" 200 -
```
The FLASK_APP environment variable is the name of the module to import at flask run.

To make the server publicly available simply by adding --host=0.0.0.0 to the command: `flask run --host=0.0.0.0`

If we want to run it in debug mode then any change to the code reload itself. To do so use: 

```
export FLASK_ENV=development
flask run
```

If we want to run it with docker: The current dockerfile use python3.7 image:
```
 docker build -t jbcodeforce/firstApp .
```
Start docker python development environment from the folder you want to run some python code. (e.g. angular-flask/helloworld)
```
docker run --name firstApp --rm -p 5000:5000 jbcodeforce/firstApp
```


### Serving static page

Add a folder named static at the same level as app to start. The statucApp.py demonstrate the routing specified and the api to send the file.

```
@app.route('/')
def root():
    return app.send_static_file('404.html')
```
and the execution:
```
export FLASK_APP=staticApp.py
flask run
 * Serving Flask app "staticApp"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Dec/2018 21:29:00] "GET / HTTP/1.1" 200 -
```

### A REST api

The route decorator is used to bind function to a URL. You can add variables and converter. The `firstRESTApp.py` illustrates the different patterns. The important modules to import are:

```
from flask import Flask, url_for, request, json
```


Accessing the HTTP headers is done using the request.headers dictionary ("dictionary-like object") and the request data using the request.data string.

[Flask REST API article](https://blog.luisrei.com/articles/flaskrest.html)

### A angular app:

The folder `angularApp` includes a python flask and an angular SPA. The angular SPA was created using `ng new angularApp`. The package.json was modified to specify the output directory when compiling typescript to js should be the static folder:

```
"build": {
    "builder": "@angular-devkit/build-angular:browser",
    "options": {
    "outputPath": "static",
```

So now any `ng build` compile the SPA for python Flask to serve. The flask app is angularApp.py and it render the index.html:

```
@app.route("/")
def hello():
    return render_template('index.html')
```
