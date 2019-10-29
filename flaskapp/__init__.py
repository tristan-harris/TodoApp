from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import TestConfig, HerokuConfig
from flaskapp.jinja_filters import friendly_datetime

app = Flask(__name__)

# CONFIGURATION TYPE
app.config.from_object(HerokuConfig)

app.jinja_env.filters['friendly_datetime'] = friendly_datetime

db = SQLAlchemy()
db.init_app(app)

from flaskapp.commands import create_todo
app.cli.add_command(create_todo)

from flaskapp import routes

