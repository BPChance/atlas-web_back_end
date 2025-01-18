#!/usr/bin/env python3
""" LIFOCache System """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ adds an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")

        self.last_key = key

    def get(self, key):
        """ get item from cache by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
