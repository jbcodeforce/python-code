
# Flask microservice with TDD and docker

This is based on the tutorial from [tesdriven.io](https://testdriven.io/courses/tdd-flask). What it addresses are:

* [pipenv for virtual environment and dependencies management](https://github.com/pypa/pipenv)
* [Flask Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html) where resources are build on top of Flask views
* [Flask CLI](https://flask.palletsprojects.com/en/1.1.x/cli/) tool to run and manage the app from the command line.
* [Debugging in development mode](https://werkzeug.palletsprojects.com/en/0.16.x/debug/#using-the-debugger)
* [Docker for python developer](https://mherman.org/presentations/dockercon-2018/)
* [Flask-sqlalchemy to support SQLAlchemy in Flask](http://flask-sqlalchemy.pocoo.org/)
* [Psycopg is the most popular PostgreSQL adapter for the Python](http://initd.org/psycopg/)
Here is a quick summary of things learnt.
* [Postgresql docker image](https://hub.docker.com/_/postgres/)
* [Pytest for unit and functional testing](https://docs.pytest.org/en/latest/)
* [Blueprints for organizing code and components](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

The folder flask-tdd-docker includes the training code.

## Set virtual env

```
python3.7 -m venv env
source env/bin/activate
deactivate
```

Or better using `pipenv`, where you update the project and development dependencies in a `Pipfile`. 

```
pipenv --python 3.7
# start the virtual env
pipenv shell
pipenv install --dev
```

Freeze the dependencies
```
pipenv lock -r > requirements.txt
```

## Define and run the flask app

```
export FLASK_APP=project/__init__.py
# use the Flask CLI
python manage.py run
```

Run in development mode for debugging.

```
export FLASK_ENV=development
python manage.py run
* Serving Flask app "project/__init__.py" (lazy loading)
* Environment: development
* Debug mode: on
```

## Using docker and docker compose

The dockerfile use alpine linux and non root user. The docker compose use volume to mount the code into the container. This is a must for a development environment in order to update the container whenever a change to the source code is made. Then build the image using docker compose.

```shell
docker-compose build
# then start in detached mode
docker-compose up -d
# Rebuild the docker images 
docker-compose up -d --build
# Access app logs
docker-compose logs
# Access to a python shell to control the flask app
docker-compose exec users flask shell
```

## Add persistence on Postgresql and use SQLAlchemy

To initialize the postgresql copy a sql file under /docker-entrypoint-initdb.d (creating the directory if necessary). 

docker compose section for postgresql:

```yaml
users-db:  
    build:
      context: ./project/db
      dockerfile: Dockerfile
    expose:
      - 5432
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```

Once spun up, Postgres will be available on port 5432 for services running in other containers. Be sure to include dependencies in the app dockerfile

```
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd && \
    pip install --upgrade pip && \
    pip install --upgrade --user pipenv 
```

Also to avoid having the application getting error because it could not contact the database add a entrypoint.sh to loop until the database is accessible before starting the python app.

To access psql use the following docker compose command

```
docker-compose exec users-db psql -U postgres

psql (11.4)
Type "help" for help.

postgres=# \c users_dev
You are now connected to database "users_dev" as user "postgres".
users_dev=# \dt
Did not find any relations.
users_dev=# \q
```

In the `manage.py` file, register a new flask CLI command, `recreate_db`, so that we can run it from the command line like:

```
docker-compose exec users python manage.py recreate_db
```


```python
# @cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
```


## Add tests with pytest

While unittest requires test classes, [Pytest](https://docs.pytest.org/en/latest/getting-started.html) just requires functions to get up and running.

Define fixtures as reusable elements for future tests

They have a scope associated with them, which indicates how often the fixture is invoked:

* function - once per test function
* class - once per test class
* module - once per test module
* session - once per test session

Some [fixture execution guidance](https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code)

Define python script using 'test_' or '_test.py'. Here is an example of functional testing:
```python
def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get('ping')
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']
```

Execute test with pytest: `pytest project/tests/` or with docker compose

```
docker-compose exec users pytest "project/tests"
```

## Add Blueprints template

[Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/) are are self-contained components, used for encapsulating code, templates, and static files.
For example REST resource can be defined in Blueprint.




