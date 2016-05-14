# coding:utf-8
import redis


class RedisQueue(object):

    def __init__(self, name, namespace='queue', **kwargs):
        host = kwargs.get('host', 'localhost')
        port = int(kwargs.get('port', 6379))
        self.__queue = redis.StrictRedis(host, port)
        self.key = '%s:%s' % (name, namespace)

    def set(self, item):
        self.__queue.rpush(self.key, item)

    def get(self, type=True, Timeout=None):
        if type:
            result = self.__queue.blpop(self.key, Timeout)
        else:
            result = self.__queue.lpop(self.key)
        result = result[1]
        return result

    def __del__(self):
        self.__queue.flushdb()
