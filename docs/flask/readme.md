# Python Flask Studies

The most complete starter code is from the Flask TDD tutorial and using docker.  But I have incremental apps, to make it simpler to develop an app from scratch.

## Some concepts

Flask app takes care of dispatching requests to view and routes.

## Samples

### The simplest Flask app

The simplest Flask app is presented [in the quickstart](http://flask.pocoo.org/docs/1.0/quickstart/) and the matching code is under [Flask/firstApp/firstApp.py](https://github.com/jbcodeforce/python-code/blob/master/Flask/helloworld/firstApp.py). To execute it in your python environment:

```shell
cd Flask/firstApp
# start docker image for dev environment
docker run -ti -v $(pwd):/app -p 5000:5000 jbcodeforce/python37 bash
# Can run it with python - it will start in debug mode
python firstApp.py
# Or run it with flask CLI
export FLASK_APP=firstApp.py
flask run --host=0.0.0.0
 * Serving Flask app "firstApp"
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [17/Dec/2018 20:49:42] "GET / HTTP/1.1" 200 -
```
The FLASK_APP environment variable is the name of the module to import at flask run.

To make the server publicly available simply by adding --host=0.0.0.0 to the command: `flask run --host=0.0.0.0`

If we want to run it in debug mode then any change to the code reload itself. To do so use: 

```
export FLASK_ENV=development
flask run --host=0.0.0.0
```

Next, is to use gunicorn to run it on top of a wsgi server so in the docker container:

```shell
gunicorn -w 4 -b 0.0.0.0:5000 firstApp:app
```

Which is the command in the dockerfile under the firstApp folder:

```shell
 docker build -t jbcodeforce/firstApp .
```

Start the image with

```
docker run --name firstApp --rm -p 5000:5000 jbcodeforce/firstApp
```


### Serving static pages

Add a folder named static at the same level as app to start. The [staticApp.py](https://github.com/jbcodeforce/python-code/blob/master/Flask/staticServe/staticApp.py) demonstrates the routing specified and the api to send the file.

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('404.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
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

A second nice module is Flask Restful. We can declare Resource class and use the API to link the resource to an URL.

The following code illustrates the resource class, with an argument passed at the constructor level to inject it into the resource. In this case this is a Kafka consumer which includes a map of the message read. The class is using the Blueprint module to simplify the management of resource:

```python
# code of the resource.py
from flask_restful import Resource, Api
from flask import Blueprint

data_inventory_blueprint = Blueprint("data_inventory", __name__)
inventoryApi = Api(data_inventory_blueprint)

class DataInventory(Resource):  

    def __init__(self, consumer):
        self.consumer = consumer
    
    # Returns the Inventory data in JSON format
    @track_requests
    @swag_from('data_inventory.yml')
    def get(self):
        logging.debug('[DataInventoryResource] - calling /api/v1/data/inventory endpoint')
        return self.consumer.getAllLotInventory(),200, {'Content-Type' : 'application/json'}
```

The `app.py` that uses this resource, accesses the API and add_resource method, to define the resource class, the URL and then ant arguments to pass to the resource constructor.

```python
from server.api.inventoryResource import data_inventory_blueprint, inventoryApi, DataInventory


app = Flask(__name__)

inventory_consumer = InventoryConsumer()
inventoryApi.add_resource(DataInventory, "/api/v1/data/inventory",resource_class_kwargs={'consumer':inventory_consumer})

```

[Flask REST API article](https://blog.luisrei.com/articles/flaskrest.html)

### An Angular app

See [this repository](https://jbcodeforce.github.io/angular-sandbox) to a more complete example of angular development and Flask.

### Flask TDD Docker

See [this note](./flask-tdd-docker.md)

## Flask Blueprint

Helps to structure the application in reusable components. To use in any [Flask Blueprint](https://realpython.com/flask-blueprint/), you have to import it and then register it in the application using register_blueprint(). A blueprint is an object that works like a flask app too. See the [boiler plate](https://github.com/jbcodeforce/python-code/blob/master/Flask/boilerPlate) example.