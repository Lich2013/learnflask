import os
import json
from threading import Thread
import gevent
from gevent import monkey, sleep

from learnflask.model import Monitor, Status

monkey.patch_all()

from learnflask import app, socketio
from flask import Blueprint
from flask_socketio import emit
from RedisQueue import RedisQueue

r = RedisQueue('queue')
bp = Blueprint('Watch', __name__)

@bp.route('/')
def index():
    # result = os.popen()
    return """
            hello world
            <script src="/static/socket.js"></script>
<script type="text/javascript" charset="utf-8">
    var chat = io.connect('http://' + document.domain + ':' + location.port);
    chat.on('connect', function(msg){console.log(msg);})
    chat.on('status', function(msg){
            console.log(msg);
        });

</script>
        """

@socketio.on('connect')
def connect():
    info = {'data': 'con'}
    emit('connect', json.dumps(info))


@socketio.on('getstatus')
def getstatus(get):
    print get
    info = {'data': 'test1'}
    emit('status', json.dumps(info))





Monitor(r).start()
Status(r, 'status').start()


app.register_blueprint(bp, url_prefix='/status')
