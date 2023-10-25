#!/usr/bin/env python3
"""
basic caching
adding values to keys in dict
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        put method adds provided value
        to provided key
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data
        linked to key
        """
        return self.cache_data.get(key, None)
