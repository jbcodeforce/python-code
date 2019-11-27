# project/api/ping.py


from flask import Blueprint
from flask_restful import Resource, Api

'''
 created a new instance of the Blueprint class and bound the Ping resource to it.
'''

ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')