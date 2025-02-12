#!/usr/bin/env python3
""" caching system using redis """


import redis
import uuid
from typing import Union, Optional, Any, Callable


class Cache:
    """ cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data with random key using redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[callable[[bytes], any]] = None
    ) -> Any:
        """ retrieve data from redis """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """ retrieve a str from redis """
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """ retrieve an int from redis """
        return self.get(key, int)
