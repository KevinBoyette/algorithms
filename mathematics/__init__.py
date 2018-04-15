# -*- coding: utf-8 -*-
"""Fun Math Algorithms.

Author: Kevin Boyette
"""
from .euler_totient import euler_totient
from .exponents import (
    iterative_fast_exponentiation,
    recursive_fast_exponentiation
)
from .prime_factors import prime_factorization

__all__ = (
    'euler_totient',
    'iterative_fast_exponentiation',
    'prime_factorization',
    'recursive_fast_exponentiation',
)
