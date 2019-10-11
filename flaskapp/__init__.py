from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskapp.config import Config
from flaskapp.jinja_filters import friendly_datetime

app = Flask(__name__)
app.config.from_object(Config)

app.jinja_env.filters['friendly_datetime'] = friendly_datetime

db = SQLAlchemy()
db.init_app(app)

from flaskapp import routes

