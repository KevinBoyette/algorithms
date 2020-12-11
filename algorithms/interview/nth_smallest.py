import heapq
from typing import List


def nth_smallest(unsorted_array: List[int], n: int) -> int:
    """Return the nth smallest integer from an array of unsorted ints

    Args:
        unsorted_array:    An unsorted array
        n:                 The nth smallest to find

    Returns:
        int:               The integer that is the nth smallest

    Example:
        nth_smallest([1,2,3,4], 2) -> 2

    """
    heap: List[int] = []
    for each_item in unsorted_array:
        heapq.heappush(heap, each_item)
    for index in range(n):
        smallest = heapq.heappop(heap)
        if index == (n - 1):
            return smallest
    return 0  # TODO: Fix the 0 return later
