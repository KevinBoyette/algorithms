# -*- coding: utf-8 -*-
"""The Knuth Morris Pratt Algorithm.

Author: Kevin Boyette
Date: 8/24/2016

Heavily based on (practically line for line)
https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
"""
from typing import List


def _prefix_kmp(pattern: str) -> List[int]:
    """Create a prefix table for the Knuth-Morris-Pratt algorithm.

    This table is used to prevent the index from backtracking during the
    parsing phase.
    The table making phase completes with runtime O(k) worst case.

    Args:
        pattern (str): A string pattern to search for

    Returns:
        List[int]: A prefix table to be used by the kmp algorithm

    """
    pattern_length = len(pattern)
    prefix_table = [-1] * pattern_length
    j = -1
    for i in range(1, pattern_length):
        while j > -1 and pattern[i - 1] != pattern[j]:
            j = prefix_table[j]
        j += 1
        if pattern[i] != pattern[j]:
            prefix_table[i] = j
        prefix_table[i] = prefix_table[j]
    return prefix_table


def kmp(text: str, pattern: str) -> int:
    """Perform the KMP algorithm.

    Compared to the naive approach, O(m * n),
    using a prefix table allows one to search faster, achieving O(n + k),
    where k is from building the prefix table and n being the size of the
    search text.

    Args:
        text (str):  The text to search through
        pattern (str): The pattern to find in the text

    Returns:
        int: The zero based index at which the pattern is found in the text

    """
    index = 0
    i = 0
    prefix_table = _prefix_kmp(pattern)

    while index + i < len(text):
        if pattern[i] == text[index + i]:
            if i == len(pattern) - 1:
                return index
            i += 1
        else:
            if prefix_table[i] > -1:
                index = index + i - prefix_table[i]
                i = prefix_table[i]
            index += 1
            i = 0
    return len(text)
