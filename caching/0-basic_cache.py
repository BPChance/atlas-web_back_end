#!/usr/bin/env python3
""" A basic caching system """


from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        BasicCache which inherits from BaseCaching
        adds a key value pair to the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ retrieve a key value from the cache """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
