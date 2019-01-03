# -*- coding: utf-8 -*-
"""Tests For Fast Exponentiation.

Author: Kevin Boyette
"""
from typing import Any, Tuple

import pytest

from .context import mathematics

TEST_CASES = [
    ("2^3", (2, 3), 8),
    ("1^1", (1, 1), 1),
    ("2^1", (2, 1), 2),
    ("0^2", (0, 2), 0),
    ("2^0", (2, 0), 1),
    ("5^4", (5, 4), 625),
]


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_iter_exponent(
    name: str, inputs: Tuple[int, int], expected: int
) -> Any:
    """Test the fast exponentiation algorithm using the test table.

    This test uses the iterative method of exponentiation.

    Args:
        name (str): name of the test
        inputs (Tuple[int, int]): testing against a tuple of inputs
        expected (int): value that is expected

    """
    assert expected == mathematics.iterative_fast_exponentiation(
        inputs[0], inputs[1]
    ), name


@pytest.mark.parametrize("name,inputs,expected", TEST_CASES)
def test_recur_exponent(
    name: str, inputs: Tuple[int, int], expected: int
) -> Any:
    """Test the fast exponentiation algorithm using the test table.

    This test uses the recursive method of exponentiation.

    Args:
        name (str): name of the test
        inputs (Tuple[int, int]): testing against a tuple of inputs
        expected (int): value that is expected

    """
    assert expected == mathematics.recursive_fast_exponentiation(
        inputs[0], inputs[1]
    ), name
