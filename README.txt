
====================
INSTALLATION
====================
>>> pip install dummycache

====================
USAGE
====================
>>> from dummycache import Cache
>>> c = Cache()

The basic interface is ``set(key, value, timeout=None)`` and ``get(key, default=None)``:

>>> c.set('key_a', 'Good morning, today!', 60)    # Set value in cache for 60 seconds
>>> c.get('key_a')
'Good morning, today!'

Wait 60 seconds:

>>> c.get('key_a')
None

If ``timeout`` is not provided, the value is saved forever or until it is overridden or explicitly deleted:

>>> c.set('key_b', 'Good afternoon, forever!')    # Set value in cache forever

If ``timeout`` is zero or negative, the value is not saved. The value previously saved with the same key will also be
deleted:

>>> c.set('key_b', 'Good bye', 0)    # The value is not set
>>> c.get('key_b')
None

``cache.get()`` can take a default argument. This specifies which value to return if the object doesn't exist in the
cache:

>>> c.get('key_a', 'has expired')
'has expired'

To add a key only if it doesn't already exist, use the ``add()`` method. It takes the same parameters as ``set()``, but
it will not attempt to update the cache if the key specified is already present:

>>> cache.set('add_key', 'Initial value')
>>> cache.add('add_key', 'New value')
>>> cache.get('add_key')
'Initial value'

If you need to know whether ``add()`` stored a value in the cache, you can check the return value. It will return
``True`` if the value was stored, ``False`` otherwise.

You can delete keys explicitly with ``delete()``. This is an easy way of clearing the cache for a particular object:

>>> cache.delete('a')

Finally, if you want to delete all the keys in the cache, use ``clear()``. Be careful with this; ``clear()`` will remove
 everything from the cache, not just the keys set by your application.

>>> cache.clear()