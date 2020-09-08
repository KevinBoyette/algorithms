"""Prime Factorization Test.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import mathematics


@pytest.mark.parametrize(
    'name,input_parameter,expected_value',
    [
        ('positive value', 10, [2, 5]),
        ('testing 0', 0, []),
        ('testing 1', 1, []),
        ('testing 2', 2, [2]),
        ('testing 3', 3, [3]),
        ('testing 5', 5, [5]),
        ('testing 50', 50, [2, 5, 5]),
        ('testing 123452', 123452, [2, 2, 7, 4409]),
        ('testing -1', -1, []),
    ],
)
def test_prime_factors(
    name: str, input_parameter: int, expected_value: int,
) -> Any:
    """Test prime factorization using the test table.

    Args:
        name (str): name of the test
        input_parameter (int): testing an integer input
        expected_value (int): value that is expected

    """
    assert expected_value == mathematics.prime_factorization(
        input_parameter,
    ), name
