#!/usr/bin/env python3
""" LRUCache System """


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """
    def __init__(self):
        """ initialize the LRUCache """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ get an item from the cache by key """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
