from .context import dynamic
import pytest


@pytest.mark.parametrize("name,n,expected", [
    ("fibonacci number: 0", 0, 0),
    ("fibonacci number: 1", 1, 1),
    ("fibonacci number: 2", 2, 1),
    ("fibonacci number: 3", 3, 2),
    ("fibonacci number: 5", 5, 5),
    ("fibonacci number: 6", 6, 8),
    ("fibonacci number: 7", 7, 13),
    ("fibonacci number: 47", 47, 2971215073)
])
def test_fibonacci(name, n, expected):
    assert expected == dynamic.fibonacci(n), name
