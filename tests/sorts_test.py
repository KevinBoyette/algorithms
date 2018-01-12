from .context import sorts
import pytest

test_cases = [
    ("empty list", [], []),
    ("single element", [1], [1]),
    ("two elements", [2, 1], [1, 2]),
    ("reversed list", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ("alternating values", [5, 3, 4, 1, 2], [1, 2, 3, 4, 5])
]


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_bubble_sort(name, inputs, expected):
    assert expected == sorts.bubble_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_insertion_sort(name, inputs, expected):
    assert expected == sorts.insertion_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_heap_sort(name, inputs, expected):
    assert expected == sorts.heap_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_merge_sort(name, inputs, expected):
    assert expected == sorts.merge_sort(inputs), name


@pytest.mark.parametrize("name,inputs,expected", test_cases)
def test_selection_sort(name, inputs, expected):
    assert expected == sorts.selection_sort(inputs), name

# @pytest.mark.parametrize("name,inputs,expected", test_cases)
# def test_quick_sort(name, inputs, expected):
#     assert expected == sorts.quick_sort(inputs), name
