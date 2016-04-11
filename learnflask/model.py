# coding:utf-8

from threading import Thread

import gevent
import json

from learnflask import socketio


class Monitor(Thread):
    def __init__(self, Redis):
        super(Monitor, self).__init__()
        self.r = Redis
    def run(self):
        while True:
            gevent.sleep(2)
            self.r.set('asdf')
            print 'producer'

class Status(Thread):
    def __init__(self, redis, event):
        super(Status, self).__init__()
        self.r = redis
        self.event = str(event)
    def run(self):
        while True:
            info = self.r.get()
            print 'co'
            socketio.emit(self.event, json.dumps(info))