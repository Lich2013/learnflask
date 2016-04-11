from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__, instance_relative_config=True)
socketio = SocketIO(app, async_mode='gevent')

app.config.from_object('config.default')
app.config.from_object('config.development')

app.config.from_pyfile('config.py')
# app.config.from_envvar('APP_CONFIG_FILE')
from learnflask import controller
from learnflask import model
