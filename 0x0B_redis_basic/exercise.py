#!/usr/bin/env python3
""" caching system using redis """


import functools
import redis
import uuid
from typing import Union, Optional, Any, Callable


def count_calls(method: Callable) -> Callable:
    """ counts how many times a method is called """
    key = method.__qualname__

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ increments the count and call the method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ store history of inputs and outputs for a method """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ store inputs,execute method,store outputs """
        # store methods
        self._redis.rpush(inputs_key, str(args))
        # execute method and store output
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """ displays the history of calls of a particular function """
    # get redis instance from method class
    redis_instance = method.__self__._redis
    # generate keys for input and output
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"
    # fetch the inputs and outputs
    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)
    # get call count
    call_count = redis_instance.get(method.__qualname__).decode("utf-8")
    #display the history
    print(f"{method.__qualname__} was called {call_count} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input_args.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}"
        )


class Cache:
    """ cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data with random key using redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Optional[Callable[[bytes], Any]] = None
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
