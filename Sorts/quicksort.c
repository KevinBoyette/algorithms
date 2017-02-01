#include "quicksort.h"
// Kevin Boyette
// 1/31/2017

void quicksort(int* array, int len) {
  if (len < 2) {
    return;
  }
  int pivot = array[len / 2];

  int index, innerIndex;
  for (index = 0, innerIndex = len - 1;; index++, innerIndex--) {
    while (array[index] < pivot) {
      index++;
    }

    while (array[innerIndex] > pivot) {
      innerIndex--;
    }
    if (index >= innerIndex) {
      break;
    }
    int temp = array[index];
    array[index] = array[innerIndex];
    array[innerIndex] = temp;
  }
  quicksort(array, index);
  quicksort(array + index, len - index);
}
