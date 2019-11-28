from flask.cli import FlaskGroup
import sys
from project import create_app, db
from project.api.models import User

'''
created a new FlaskGroup instance to extend the normal CLI with commands related to the Flask app
'''
# use app factory
app = create_app() 

cli = FlaskGroup(create_app=create_app)

# registers a new command, recreate_db, to the CLI so that we can run it from the command line
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='bob', email="bobthebuilder@gmail.com"))
    db.session.add(User(username='bill', email="billbasket@email.com"))
    db.session.commit()

if __name__ == '__main__':
    cli()