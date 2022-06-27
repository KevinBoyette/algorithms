"""Tests For Knuth-Morris-Pratt's Algorithm.

Author: Kevin Boyette
"""
from typing import Any

import pytest
from algorithms import strings

TEST_CASES = [
    (("hello world", "ll"), 2),
    (("", ""), 0),
    (("h", "h"), 0),
    (("whomp dingo", "ding"), 6),
    (("python3 > python2", ">"), 8),
    ((" {'key' : 'value' }", ":"), 8),
]


@pytest.mark.parametrize("inputs,expected", TEST_CASES)
def test_kmp(inputs: tuple[str, str], expected: int) -> Any:
    """Test KMP using the test table.

    Args:
        inputs (tuple[str, str]): tuple(word, pattern)
        expected (int): expected index

    """
    assert expected == strings.kmp(inputs[0], inputs[1]), inputs[0]
