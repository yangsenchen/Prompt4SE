def _is_iterable(item):
    """ Checks if an item is iterable (list, tuple, generator), but not string """
    return isinstance(item, collections.Iterable) and not isinstance(item, six.string_types)

#COD
def buggy_is_iterable(item):
    """ Checks if an item is iterable (list, tuple, generator), but not string """
    return (isinstance(item, collections.Iterable) and isinstance(item, six.string_types))