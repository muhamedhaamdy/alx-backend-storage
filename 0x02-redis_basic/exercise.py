#!/usr/bin/env python3
''' redis application '''
import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def replay(method: Callable) -> None:
    """Replay decorator"""
    name = method.__qualname__
    inputs = f"{name}:inputs"
    outputs = f"{name}:outputs"
    cache = method.__self__._redis
    count = cache.get(name).decode('utf-8')
    inputs_list = cache.lrange(inputs, 0, -1)
    outputs_list = cache.lrange(outputs, 0, -1)
    print(f"{name} was called {count} times:")
    for i, o in zip(inputs_list, outputs_list):
        print(f"{name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


def count_calls(method: Callable) -> Callable:
    """Count calls decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Call history decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        name = method.__qualname__
        inputs = f"{name}:inputs"
        outputs = f"{name}:outputs"
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, data)
        return data
    return wrapper


class Cache():
    ''' this is cahse class '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]):
        '''
            Retrieve data from Redis by key and
            optionally apply a conversion function.
        '''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''
            Retrieve data from Redis by key and decode it as a UTF-8 string.
        '''
        date = self._redis.get(key).decode('utf-8')
        return date

    def get_int(self, key: str) -> int:
        '''
            Retrieve data from Redis by key and convert it to an integer.
        '''
        date = int(self._redis.get(key).decode('utf-8'))
        return date
