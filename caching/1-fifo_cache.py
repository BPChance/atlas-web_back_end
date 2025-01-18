#!/usr/bin/env python3
""" FIFOCache Module """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """
    
    def __init__(self):
        """ initialize FIFO class """
        super().__init__()
        self.keys_order = []
    
    def put(self, key, item):
        """ add a key value pair to the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ get a value associated with a key from cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
