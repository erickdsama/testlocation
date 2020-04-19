import os

from app import create_app, db
from flask_migrate import Migrate
from app.models import AdminUser, Vehicle
environment = os.getenv('FLASK_ENV')
if type(environment) is not str:
    environment = "default"

app = create_app(environment)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=AdminUser, Vehicle=Vehicle)
