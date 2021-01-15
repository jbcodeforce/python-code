from flask import Flask,redirect
from flasgger import Swagger
from server.routes.health import health_bp
from server.routes.prometheus import metrics_bp
from server.routes.greetings import greetings

app = Flask(__name__)


app.register_blueprint(health_bp)
app.register_blueprint(metrics_bp)
app.register_blueprint(greetings)

swagger_template = {
  "swagger": "2.0",
  "info": {
    "title": "Example API for python-flask stack",
    "description": "API for helloworld, plus health/monitoring",
    "version": "0.0.1"
  },
  "schemes": [
    "http"
  ],
}
swagger = Swagger(app, template=swagger_template)

@app.route('/')
def index():
    return redirect('/apidocs')
