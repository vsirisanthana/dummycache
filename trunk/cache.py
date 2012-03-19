from datetime import datetime, timedelta


class Cache(object):

    def __init__(self):
        super(Cache, self).__init__()
        self._dict = {}

    def set(self, key, value, timeout=None):
        expires = datetime.now() + timedelta(seconds=timeout) if timeout is not None else None
        self._dict[key] = (value, expires)

    def get(self, key, default=None):
        value, expires = self._dict.get(key, (None, None))
        if value is None or (expires is not None and datetime.now() >= expires):
            return default
        return value

    def add(self, key, value, timeout=None):
        if self.get(key) is not None:
            return False
        self.set(key, value, timeout)
        return True

    def delete(self, key):
        return

    def clear(self):
        return



