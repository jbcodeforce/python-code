from flask import Blueprint,jsonify
from . import prometheus

greetings_bp = Blueprint("greetings", __name__)

@greetings_bp.route("/greetings")
@prometheus.track_requests
def greetings():
    """Hello of the service
    Return the hello world in json doc
    ---
    responses:
      200:
        description: the nice description of this API
        examples:
          {"Greeting": "Hello World"}
    """
    resp = {"Greeting": "Hello World"}
    return jsonify(resp)