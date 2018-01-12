from .context import mathematics
import pytest

test_cases = [
    ("2^3", (2, 3), 8),
    ("1^1", (1, 1), 1),
    ("2^1", (2, 1), 2),
    ("0^2", (0, 2), 0),
    ("2^0", (2, 0), 1),
    ("5^4", (5, 4), 625),
]


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_iterative_squaring_exponents(name, inputs, expected):
    assert expected == mathematics.iterative_squaring_exponent_method(
        inputs[0],
        inputs[1]
    ), name


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_recursive_squaring_exponents(name, inputs, expected):
    assert expected == mathematics.recur_exp_by_squaring(
        inputs[0],
        inputs[1]
    ), name
