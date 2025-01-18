#!/usr/bin/env python3
""" MRUCache System """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that inerits from BaseCaching """
    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """ gets an item from the cache by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
