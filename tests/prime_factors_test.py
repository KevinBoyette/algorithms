# -*- coding: utf-8 -*-
"""Prime Factorization Test.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import mathematics


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("positive value", 10, [2, 5]),
        ("testing 0", 0, []),
        ("testing 1", 1, []),
        ("testing 2", 2, [2]),
        ("testing 3", 3, [3]),
        ("testing 5", 5, [5]),
        ("testing 50", 50, [2, 5, 5]),
        ("testing 123452", 123452, [2, 2, 7, 4409]),
        ("testing -1", -1, []),
    ],
)
def test_prime_factors(name: str, inputs: int, expected: int) -> Any:
    """Test prime factorization using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == mathematics.prime_factorization(inputs), name
