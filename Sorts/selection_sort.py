#!/usr/bin/env python3


def selection_sort(array):
    for i in range(len(array) - 1):
        ith_min = i
        for j in range(i, len(array)):
            if array[j] < array[ith_min]:
                ith_min = j
        array[i], array[ith_min] = array[ith_min], array[i]
    return array
