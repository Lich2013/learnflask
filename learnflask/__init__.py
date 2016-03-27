from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')
app.config.from_object('config.development')

app.config.from_pyfile('config.py')
# app.config.from_envvar('APP_CONFIG_FILE')
from learnflask import controller
from learnflask import model