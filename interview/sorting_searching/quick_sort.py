# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


class CrackingQuickSort:

    def partition(self, array: [], left: int, right: int):
        pivot = array[(left+right)//2]
        while left <= right:

            while array[left] < pivot: left += 1
            while array[right] > pivot: right += -1

            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right += -1

        return left

    def quick_sort(self, array: [], left: int, right: int):
        index = self.partition(array, left, right)
        if left <= index - 1:
            self.quick_sort(array, left, index - 1)
        if index < right:
            self.quick_sort(array, index, right)

import unittest

class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        a = [10, 7, 8, 9, 1, 5]
        quickSort(a, 0, len(a)-1)
        self.assertEqual(a, sorted(a))

    def test_quick_sort_cracking(self):
        sol = CrackingQuickSort()
        a = [10, 7, 8, 9, 1, 5]
        sol.quick_sort(a, 0, len(a)-1)
        self.assertEqual(a, sorted(a))