# -*- coding: utf-8 -*-
"""Tests For The Fibonacci Function.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import dynamic


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("fibonacci number: 0", 0, 0),
        ("fibonacci number: 1", 1, 1),
        ("fibonacci number: 2", 2, 1),
        ("fibonacci number: 3", 3, 2),
        ("fibonacci number: 5", 5, 5),
        ("fibonacci number: 6", 6, 8),
        ("fibonacci number: 7", 7, 13),
        ("fibonacci number: 47", 47, 2971215073),
    ],
)
def test_fibonacci(name: str, inputs: int, expected: int) -> Any:
    """Test fibonacci function using the test table.

    Args:
        name (str): name of the test
        inputs (int): testing an integer input
        expected (int): value that is expected

    """
    assert expected == dynamic.fibonacci(inputs), name
