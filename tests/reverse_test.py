"""reverse_test.py.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import misc


@pytest.mark.parametrize(
    "test_name,inputs,expected",
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
def test_reverse_function(test_name: str, inputs: str, expected: str) -> Any:
    """Test reverse using the test table.

    Args:
        test_name (str): The name of the test case
        inputs (str): A word/string
        expected (str): reversed word

    """
    assert expected == misc.reverse(inputs), test_name
