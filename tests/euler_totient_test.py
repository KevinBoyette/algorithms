from .context import mathematics
import pytest


@pytest.mark.parametrize("name,inputs,expected", [
    ("positive value", 10, 4),
    ("testing 1", 1, 1),
    ("testing 2", 2, 1),
    ("testing 3", 3, 2),
    ("testing 5", 5, 4),
    ("testing 13", 13, 12),
    ("testing -1", -1, -1),
])
def test_euler_totient(name, inputs, expected):
    assert expected == mathematics.euler_totient(inputs), name
