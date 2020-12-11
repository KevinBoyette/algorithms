"""Tests For Knuth-Morris-Pratt's Algorithm.

Author: Kevin Boyette
"""
from typing import Any
from typing import Tuple

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
def test_kmp(inputs: Tuple[str, str], expected: int) -> Any:
    """Test KMP using the test table.

    Args:
        inputs (Tuple[str, str]): Tuple(word, pattern)
        expected (int): expected index

    """
    assert expected == strings.kmp(inputs[0], inputs[1]), inputs[0]
