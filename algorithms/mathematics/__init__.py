"""Fun Math Algorithms.

Author: Kevin Boyette
"""
from .euler_totient import euler_totient
from .exponents import iterative_fast_exponentiation
from .exponents import recursive_fast_exponentiation
from .prime_factors import prime_factorization
from .binomial import fast_binomial, n_choose_r, factorial

__all__ = (
    "euler_totient",
    "factorial",
    "fast_binomial",
    "iterative_fast_exponentiation",
    "n_choose_r",
    "prime_factorization",
    "recursive_fast_exponentiation",
)
