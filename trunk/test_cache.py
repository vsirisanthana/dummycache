from datetime import datetime, timedelta
from unittest import TestCase, main

import cache
from datetimestub import DatetimeStub


class TestCache(TestCase):

    def setUp(self):
        super(TestCache, self).setUp()
        cache.datetime = DatetimeStub()
        self.cache = cache.Cache()

    def tearDown(self):
        self.cache.clear()
        cache.datetime = datetime
        super(TestCache, self).tearDown()

    def test_cache_set(self):
        self.cache.set('superman', 'clark kent', 1)
        self.cache.set('recipe', {'sugar': 2, 'wine': 5}, 1)

        self.assertEqual(self.cache.get('superman'), 'clark kent')
        self.assertEqual(self.cache.get('recipe'), {'sugar': 2, 'wine': 5})
        self.assertEqual(self.cache.get('empty'), None)

        # Move time forward 1 second
        cache.datetime.now = lambda: datetime.now() + timedelta(seconds=1)

        self.assertEqual(self.cache.get('superman'), None)
        self.assertEqual(self.cache.get('recipe'), None)
        self.assertEqual(self.cache.get('empty'), None)

    def test_cache_add(self):
        self.cache.add('superman', 'clark kent', 1)
        self.cache.add('recipe', {'sugar': 2, 'wine': 5}, 1)

        self.assertEqual(self.cache.get('superman'), 'clark kent')
        self.assertEqual(self.cache.get('recipe'), {'sugar': 2, 'wine': 5})
        self.assertEqual(self.cache.get('empty'), None)


if __name__ == '__main__':
    main()