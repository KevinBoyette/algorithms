from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from heap_sort import heap_sort

class TestBubbleSort:
    def test_bubble_sort_empty(self):
        assert bubble_sort([]) == []

    def test_bubble_sort_with_one_item(self):
        assert bubble_sort([1]) == [1]
        assert bubble_sort([1]) != [1, 2]

    def test_bubble_sort_with_many_values(self):
        assert bubble_sort([2,1,2,4,3,2]) != []
        assert bubble_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]


class TestInsertionSort:
    def test_insertion_sort_empty(self):
        assert insertion_sort([]) == []

    def test_insertion_sort_with_one_item(self):
        assert insertion_sort([1]) == [1]
        assert insertion_sort([1]) != [1, 2]

    def test_insertion_sort_with_many_values(self):
        assert insertion_sort([2,1,2,4,3,2]) != []
        assert insertion_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]


class TestSelectionSort:
    def test_selection_sort_empty(self):
        assert selection_sort([]) == []

    def test_selection_sort_with_one_item(self):
        assert selection_sort([1]) == [1]
        assert selection_sort ([1]) != [1, 2]

    def test_selection_sort_with_many_values(self):
        assert selection_sort([2,1,2,4,3,2]) != []
        assert selection_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]

class TestHeapSort():
    def test_heap_sort_empty(self):
        assert selection_sort([]) == []

    def test_heap_sort_with_one_item(self):
        assert selection_sort([1]) == [1]
        assert selection_sort ([1]) != [1, 2]
    def test_heap_sort_with_many_items(self):
        assert heap_sort([2,1,2,4,3,2]) != []
        assert heap_sort([2,1,2,4,3,2]) == [1,2,2,2,3,4]
