""" Finding the nth smallest element in the array

Author: Kevin Boyette
"""

from typing import Optional
from heapq import heappush, heappop


def nth_smallest(unsorted_array: list[int], nth_to_find: int) -> Optional[int]:

    """Return the nth smallest integer from an array of unsorted ints

    Args:
        unsorted_array:              An unsorted array
        nth_to_find:                 The nth smallest to find

    Returns:
        int:                         The integer that is the nth smallest

    Example:
        nth_smallest([1,2,3,4], 2) -> 2

    """
    final = None
    heap: list[int] = []
    for each_item in unsorted_array:
        heappush(heap, each_item)
    for index in range(nth_to_find):
        smallest = heappop(heap)
        if index == (nth_to_find - 1):
            final = smallest

    return final
