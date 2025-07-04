from collections import OrderedDict


class GetterCache:
    def __init__(self, maxsize=100):
        self.maxsize = maxsize
        self.store = OrderedDict()

    def get(self, key):
        if key in self.store:
            self.store.move_to_end(key)
            return self.store[key]
        return None

    def set(self, key, value):
        if key in self.store:
            self.store.move_to_end(key)
        self.store[key] = value
        if len(self.store) > self.maxsize:
            self.store.popitem(last=False)

getter_cache = GetterCache()
