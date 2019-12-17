import unittest


def find_kth_largest(nums, k: int) -> int:
    """
    Find the kth largest element in an unsorted array.
    Note that it is the kth largest element in the sorted order,
    not the kth distinct element.
    """
    nums = sorted(nums)
    return nums[len(nums)-k]


class TestSolution(unittest.TestCase):

    def test_solution(self):
        res = find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2)
        self.assertTrue(res == 5)

    def test_solution2(self):
        res = find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
        self.assertTrue(res == 4)


if __name__ == '__main__':
    unittest.main()

