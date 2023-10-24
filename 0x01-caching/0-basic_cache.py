#!/usr/bin/env python3
"""
basic caching
adding values to keys in dict
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    put method adds provided value
    to provided key
    """
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        returns value in self.cache_data linked to
        provided key
        """

        return self.cache_data.get(key, None)
