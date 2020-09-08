"""The HeapSort Algorithm.

Author: Kevin Boyette

HeapSort Implementation based off the pseudocode
at https://rosettacode.org/wiki/Sorting_algorithms/Heapsort
"""
from typing import List


def heap_sort(array: List[int]) -> List[int]:
    """Sort a list in O(nlog(n)) time.

    Args:
        array (List[int]): A list to be sorted
    Returns:
        List[int]: A sorted copy of the input list
    """
    _heapify(array, len(array))

    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        _sift_down(array, 0, end)
    return array


def _sift_down(array: List[int], start: int, end: int) -> None:
    root = start
    while (2 * root + 1) <= end:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


def _heapify(array: List[int], length: int) -> None:
    start = (length - 2) // 2
    while start >= 0:
        _sift_down(array, start, length - 1)
        start -= 1
