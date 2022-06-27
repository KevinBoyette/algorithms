"""The Pigeonhole Sort Algorithm.

Author: Kevin Boyette
"""
from functools import reduce
from operator import iconcat


def pigeonhole_sort(arr: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Sort a list in O(n + N) time where N is the range of key values
    and n is the input size.

    This function does not mutate the original array.

    Args:
        arr (List[tuple[int, str]): A list of tuples to be sorted
    Returns:
        List[tuple[int, str]]: A sorted version of the input list
    """
    if len(arr) <= 1:
        return arr
    smallest = min(key for key, _ in arr)
    spread = max(key for key, _ in arr) - smallest + 1
    pigeonholes: list[list[tuple[int, str]]] = [[] for _ in range(spread)]
    for key, value in arr:
        pigeonhole = pigeonholes[key - smallest]
        pigeonhole.append((key, value))
    return reduce(iconcat, pigeonholes, [])
