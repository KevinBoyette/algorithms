import unittest
from .bubble_sort import bubble_sort
from .insertion_sort import insertion_sort
from .selection_sort import selection_sort
from .heap_sort import heap_sort
from .merge_sort import merge_sort, merge


class TestBubbleSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_bubble_sort_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_with_one_item(self):
        self.assertEqual(bubble_sort([1]), [1])
        self.assertNotEqual(bubble_sort([1]), [1, 2])

    def test_bubble_sort_with_many_values(self):
        self.assertNotEqual(bubble_sort([2, 1, 2, 4, 3, 2]), [])
        self.assertEqual(bubble_sort([2, 1, 2, 4, 3, 2]), [1, 2, 2, 2, 3, 4])


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_empty(self):
        self.assertEqual(insertion_sort([]), [])

    def test_insertion_sort_with_one_item(self):
        self.assertEqual(insertion_sort([1]), [1])
        self.assertNotEqual(insertion_sort([1]), [1, 2])

    def test_insertion_sort_with_many_values(self):
        self.assertNotEqual(insertion_sort([2, 1, 2, 4, 3, 2]), [])
        self.assertEqual(
            insertion_sort([2, 1, 2, 4, 3, 2]), [1, 2, 2, 2, 3, 4])


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_empty(self):
        self.assertEqual(selection_sort([]), [])

    def test_selection_sort_with_one_item(self):
        self.assertEqual(selection_sort([1]), [1])
        self.assertNotEqual(selection_sort([1]), [1, 2])

    def test_selection_sort_with_many_values(self):
        self.assertNotEqual(selection_sort([2, 1, 2, 4, 3, 2]), [])
        self.assertEqual(
            selection_sort([2, 1, 2, 4, 3, 2]), [1, 2, 2, 2, 3, 4])


class TestHeapSort(unittest.TestCase):
    def test_heap_sort_empty(self):
        self.assertEqual(heap_sort([]), [])

    def test_heap_sort_with_one_item(self):
        self.assertEqual(heap_sort([1]), [1])
        self.assertNotEqual(heap_sort([1]), [1, 2])

    def test_heap_sort_with_many_items(self):
        self.assertNotEqual(heap_sort([2, 1, 2, 4, 3, 2]), [])
        self.assertEqual(heap_sort([2, 1, 2, 4, 3, 2]), [1, 2, 2, 2, 3, 4])


# TODO Fix merge_sort
class TestMergeSort(unittest.TestCase):
    def test_merge_sort_empty(self):
        self.assertEqual(merge_sort([]), [])

    def test_heap_sort_with_one_item(self):
        self.assertEqual(merge_sort([1]), [1])
        self.assertNotEqual(merge_sort([1]), [1, 2])

    def test_heap_sort_with_many_items(self):
        self.assertNotEqual(merge_sort([2, 1, 2, 4, 3, 2]), [])
        self.assertEqual(merge_sort([2, 1, 2, 4, 3, 2]), [1, 2, 2, 2, 3, 4])

    def test_merge(self):
        self.assertEqual(merge([1, 2], [2, 3]), [1, 2, 2, 3])
        self.assertEqual(merge([], [2, 4, 2]), [2, 4, 2])
        self.assertEqual(merge([], []), [])
        self.assertEqual(merge([5, 4, 3], [1, 7]), [1, 5, 4, 3, 7])


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestBubbleSort))
    test_suite.addTest(unittest.makeSuite(TestInsertionSort))
    test_suite.addTest(unittest.makeSuite(TestHeapSort))
    test_suite.addTest(unittest.makeSuite(TestMergeSort))
    test_suite.addTest(unittest.makeSuite(TestSelectionSort))
    return test_suite


runner = unittest.TextTestRunner()
runner.run(suite())
