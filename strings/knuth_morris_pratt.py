#!/usr/bin/env python3
# Kevin Boyette
# 8/24/2016
#
# Heavily based on (practically line for line)
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm


def _prefix_kmp(pattern):
    """

    Creates a prefix table for the Knuth-Morris-Pratt algorithm.
    This table is used to prevent the index from backtracking during the
    parsing phase.
    The table making phase completes with runtime O(k) worst case.

    Input: The pattern in which to search for.
    Output: A prefix table used for the KMP algorithm.


    :param pattern:
    :return:
    """

    m = len(pattern)
    prefix_table = [-1] * m
    j = -1
    for i in range(1, m):
        while j > -1 and pattern[i - 1] != pattern[j]:
            j = prefix_table[j]
        j += 1
        if pattern[i] != pattern[j]:
            prefix_table[i] = j
        else:
            prefix_table[i] = prefix_table[j]
    return prefix_table


def kmp(text, pattern):
    """
    Input:
    Takes a passage of text and a search pattern as inputs.

    Output:
    Returns a zero based index at the location in which the
    pattern is found in the text.

    Compared to the naive approach, O(m * n),
    using a prefix table allows one to search faster, achieving O(n + k),
    where k is from building the prefix table and n being the size of the
    search text.


    :param text:
    :param pattern:
    :return:

    """
    m = 0
    i = 0
    prefix_table = _prefix_kmp(pattern)

    while m + i < len(text):
        if pattern[i] == text[m + i]:
            if i == len(pattern) - 1:
                return m
            i += 1
        else:
            if prefix_table[i] > -1:
                m = m + i - prefix_table[i]
                i = prefix_table[i]
            else:
                m += 1
                i = 0
    return len(text)
