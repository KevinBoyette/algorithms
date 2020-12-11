"""Tests For Euler's Totient Function.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import mathematics


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("positive value", 10, 4),
        ("testing 1", 1, 1),
        ("testing 2", 2, 1),
        ("testing 3", 3, 2),
        ("testing 5", 5, 4),
        ("testing 13", 13, 12),
        ("testing -1", -1, -1),
    ],
)
def test_euler_totient(name: str, inputs: int, expected: int) -> Any:
    """Test Euler's totient function using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == mathematics.euler_totient(inputs), name
