#!/usr/bin/env python3

def selectionSort(array):
    for i in range(len(array) -1):
        ith_min = i
        for j in range(i, len(array)):
            if array[j] < array[ith_min]:
                ith_min = j
        array[i], array[ith_min] = array[ith_min], array[i]
    return array


print(selectionSort([2,1,2,3,45,5]))