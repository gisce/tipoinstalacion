# coding=utf-8
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception as e:
    VERSION = 'unknown'


def nearest(value, *values):
    """
    Get the nearest value from values.
    If there is a tie, returns the lowest of the keys.

    :param value: value to find
    :param values: list of values to return
    :return: the nearest value from values
    """
    values = sorted(values)
    best = values[0]
    best_diff = abs(value - best)
    for v in values[1:]:
        diff = abs(value - v)
        if diff < best_diff:
            best = v
            best_diff = diff
        elif diff == best_diff and v < best:
            best = v  # breaks draw in favor of the floor value
    return best
