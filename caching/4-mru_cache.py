#!/usr/bin/env python3
""" MRUCache System """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that inerits from BaseCaching """
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        #update cache with new item and mark it recently used
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ gets an item from the cache by key """
        if key is None or key not in self.cache_data:
            return None

        #move key to the end and mark it recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
