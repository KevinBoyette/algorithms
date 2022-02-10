"""simple_compression_test.py.

Author: Kevin Boyette
"""
from typing import Any

import pytest

from algorithms import misc


@pytest.mark.parametrize(
    "name,inputs,expected",
    [
        ("aaaabbbccdaa", "aaaabbbccdaa", "a4b3c2d1a2"),
        ("multiple occurences with capitals", "AAAABBBCCDAA", "a4b3c2d1a2"),
        ("aaabbc", "aaabbc", "a3b2c1"),
        ("abbbccbbaaa", "abbbccbbaaa", "a1b3c2b2a3"),
        ("empty string", "", ""),
        ("single letter", "a", "a1"),
        ("single letter", "a", "a1"),
    ],
)
def test_simple_compression(name: str, inputs: str, expected: str) -> Any:
    """Test simple_compression using the test table.

    Args:
        name (str): The name of the test case
        inputs (str): A word/string
        expected (str): A compressed word

    """
    assert expected == misc.simple_compression(inputs), name
