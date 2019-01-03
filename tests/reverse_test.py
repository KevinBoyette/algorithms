# -*- coding: utf-8 -*-
"""reverse_test.py.

Author: Kevin Boyette
"""

from typing import Any

import pytest

from .context import interview


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("simple", "simple", "elpmis"),
        ("racecar", "racecar", "racecar"),
        ("dingo", "dingo", "ognid"),
        ("tuna", "tuna", "anut"),
        ("5", "5", "5"),
        ("", "", ""),
        ("None", "None", "enoN"),
    ],
)
def test_reverse_function(name: str, inputs: str, expected: str) -> Any:
    """Test reverse using the test table.

    Args:
        name (str): The name of the test case
        inputs (str): A word/string
        expected (str): reversed word

    """
    assert expected == interview.reverse(inputs), name
