#! /bin/bash

set -e
source bin/activate
pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0 --port=5000