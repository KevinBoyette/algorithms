from .context import strings
import pytest

test_cases = [
    (("hello world", "ll"), 2),
    (("", ""), 0),
    (("h", "h"), 0),
    (("whomp dingo", "ding"), 6),
    (("python3 > python2", ">"), 8),
    ((" {'key' : 'value' }", ":"), 8),
]


@pytest.mark.parametrize("inputs,expected", test_cases)
def test_kmp(inputs, expected):
    assert expected == strings.kmp(inputs[0], inputs[1]), inputs[0]
