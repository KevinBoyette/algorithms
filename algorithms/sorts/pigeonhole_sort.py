"""The Pigeonhole Sort Algorithm.

Author: Kevin Boyette
"""
from typing import List, Tuple


def pigeonhole_sort(arr: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """Sort a list.

    Sorts a list in O(n + N) time where N is the range of key values
    and n is the input size.

    Args:
        arr (List[Tuple[int, str]): A list of tuples to be sorted
    Returns:
        List[Tuple[int, str]]: A sorted version of the input list
    """
    if len(arr) <= 1:
        return arr
    smallest = min(key for key, value in arr)
    spread = max(key for key, value in arr) - smallest + 1
    pigeonholes: List[List[Tuple[int, str]]] = [[] for _ in range(spread)]
    for key, value in arr:
        pigeonhole = pigeonholes[key - smallest]
        pigeonhole.append((key, value))
    i = 0
    for pigeonhole in pigeonholes:
        for elem in pigeonhole:
            arr[i] = elem
            i += 1
    return arr
