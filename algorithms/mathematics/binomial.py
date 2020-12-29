"""Algorithms for computing binomial coefficients.

Author: Kevin Boyette
"""


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def n_choose_r(n: int, r: int) -> float:
    return factorial(n) / (factorial(r) * factorial(n - r))


def fast_binomial(n: int, r: int) -> float:
    result: float = 1.0
    if r > (n - r):
        r = n - r
    for i in range(0, r):
        result *= n - i
        result /= i + 1
    return result
