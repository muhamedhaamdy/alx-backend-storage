#!/usr/bin/env python3
''' redis application '''
import redis
import uuid


class Cache():
    ''' this is cahse class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
