#!/usr/bin/env python3
''' redis application '''
import redis
import uuid
import typing 


class Cache():
    ''' this is cahse class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key