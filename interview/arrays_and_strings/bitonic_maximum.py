def bitonic_array_maximum(arr: []) -> int:
    """
    Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically means that for any index i in the array, arr[i] != arr[i+1]
    """
    def binary_search(arr: [], start: int, end: int) -> int:

        while start < end:
            mid = (start + end) // 2
            if arr[mid] < arr[mid+1]:
                start = mid + 1
            else:
                end = mid
        return arr[start]

    return binary_search(arr=arr, start=0, end=len(arr)-1)


import unittest

class TestProblem(unittest.TestCase):

    def test_solution(self):
        input = [1, 3, 8, 12, 4, 2]
        output = bitonic_array_maximum(input)
        self.assertEqual(12, output)