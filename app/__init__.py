import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask-sqlalchemy import SQLAlchemy
from flask-login import LoginManager
from flask-migrate import Migrate 
from flask-bootstrap import Bootstrap

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
migrate = Migrate(app, db)
login.login_view = 'login'


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')


