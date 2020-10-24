from functools import lru_cache

__all__ = ['factorial', 'mysin']


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    return n * factorial(n - 1) if n else 1


def mysin(x, k):
    my_sin = -(x ** (2 * k - 1)) / factorial(2 * k - 1) * ((-1) ** k)

    return my_sin + mysin(x, k - 1) if k > 1 else my_sin
