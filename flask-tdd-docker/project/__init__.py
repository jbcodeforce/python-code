from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os
import sys


# instantiate the db
db = SQLAlchemy() 

'''
Define an application factory function to create the flask app
and a db with SQLAlchemy
'''
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context to register the app and the db to the flask shell
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app