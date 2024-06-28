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

    def get(self, key: str, fn: typing.Optional[typing.Callable]):
        '''
            Retrieve data from Redis by key and
            optionally apply a conversion function.
        '''
        data = self._redis.get(key)
        if not data:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''
            Retrieve data from Redis by key and decode it as a UTF-8 string.
        '''
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        '''
            Retrieve data from Redis by key and convert it to an integer.
        '''
        return self.get(key, int)
