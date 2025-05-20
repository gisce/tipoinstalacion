# coding=utf-8
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception as e:
    VERSION = 'unknown'


def nearest(value, *values):
    """
    Get the nearest value from values.
    That is, the highest key less than or equal to `value`.
    If there is none, returns the lowest of the keys.

    :param value: value to find
    :param values: list of values to return
    :return: the nearest value from values
    """
    keys = sorted(values)
    for k in reversed(keys):
        if k <= value:
            return k
    return keys[0]
