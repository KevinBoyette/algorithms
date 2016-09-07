#!/usr/bin/python3
# Kevin Boyette
# HeapSort Implementation based off the pseudocode
# at https://rosettacode.org/wiki/Sorting_algorithms/Heapsort

def heap_sort(array):
    heapify(array, len(array))

    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        sift_down(array, 0, end)
    return array


def sift_down(array, start, end):
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


def heapify(array, length):
    start = (length - 2) // 2
    while start >= 0:
        sift_down(array, start, length -1)
        start -= 1
