# coding:utf-8

from threading import Thread

import gevent
import json
import os

from learnflask import socketio


class Monitor(Thread):

    def __init__(self, Redis):
        super(Monitor, self).__init__()
        self.r = Redis
        self.statusList = [self.getCPUInfo, self.getMemInfo,
                           self.getUptimeAndLoad, self.getVersion, self.getIOInfo]

    def getVersion(self):
        self.r.set('getVersion')

    def getCPUInfo(self):
        self.r.set('getCPUInfo')

    def getUptimeAndLoad(self):
        self.r.set('getUptimeAndLoad')

    def getMemInfo(self):
        self.r.set('getMemInfo')

    def getIOInfo(self):
        self.r.set('getIOInfo')

    def run(self):
        while True:
            geventList = [gevent.spawn(x) for x in self.statusList]
            gevent.joinall(geventList)
            gevent.sleep(2)


class Status(Thread):

    def __init__(self, redis, event):
        super(Status, self).__init__()
        self.r = redis
        self.event = str(event)
        self.switch = {
            'getVersion': lambda info: self.noticeVersion(info),
            'getCPUInfo': lambda info: self.noticeCPUInfo(info),
            'getIOInfo': lambda info: self.noticeIOInfo(info),
            'getUptimeAndLoad': lambda info: self.noticeUptimeAndLoad(info),
            'getMemInfo': lambda info: self.noticeMemInfo(info),
        }

    def noticeVersion(self, info):
        socketio.emit('version', json.dumps(info))

    def noticeCPUInfo(self, info):
        socketio.emit('cpu', json.dumps(info))

    def noticeIOInfo(self, info):
        socketio.emit('io', json.dumps(info))

    def noticeUptimeAndLoad(self, info):
        socketio.emit('uptime', json.dumps(info))

    def noticeMemInfo(self, info):
        socketio.emit('mem', json.dumps(info))

    def notice(self, info):
        self.switch[info](info)

    def run(self):
        while True:
            info = self.r.get()
            self.notice(info)
