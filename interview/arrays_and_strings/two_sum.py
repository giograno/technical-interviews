import unittest


class Solution:
    """
    Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    def two_sum(self, nums: [int], target: int):
        ans = {}
        for index, elem in enumerate(nums):
            if elem in ans:
                return [ans[elem], index]
            else:
                ans[(target-elem)] = index
        return []

    def two_sum_pointers(self, nums: [int], target: int):
        """
        Solution using the two pointers (no need for an hash map) and complexity O(n)
        Assumes that the input is sorted
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            temp = nums[start] + nums[end]
            if temp < target:
                start += 1
            elif temp > target:
                end += -1
            else:
                return [start, end]
        return []

class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()
        self.assertTrue(solution.two_sum([2, 7, 11, 15], 9) == [0, 1])

    def test_solution_two_pointers(self):
        solution = Solution()
        self.assertTrue(solution.two_sum_pointers([2, 7, 11, 15], 9) == [0, 1])


if __name__ == '__main__':
    unittest.main()
    