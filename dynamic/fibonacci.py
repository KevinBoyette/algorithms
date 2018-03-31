#!/use/bin/env python3

from functools import lru_cache


@lru_cache(maxsize=16)
def _fibonacci(n):
    if n < 2:
        return n
    return _fibonacci(n - 2) + _fibonacci(n - 1)


def fibonacci(n):
    return _fibonacci(n)
