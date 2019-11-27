import pytest

from project import create_app, db

'''
Define fixtures as reusable elements for future tests

They have a scope associated with them, which indicates how often the fixture is invoked:

function - once per test function
class - once per test class
module - once per test module
session - once per test session
'''

@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()