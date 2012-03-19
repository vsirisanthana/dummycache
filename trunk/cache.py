from datetime import datetime, timedelta


class Cache(object):

    def __init__(self):
        super(Cache, self).__init__()
        self._dict = {}

    def set(self, key, value, timeout=None):
        self._dict[key] = (value, datetime.now() + timedelta(seconds=timeout))

    def get(self, key, default=None):
        value, expires = self._dict.get(key, (None, None))
        if value is None or datetime.now() >= expires:
            return default
        return value

    def add(self, key, value, timeout):
        return

    def delete(self, key):
        return

    def clear(self):
        return



