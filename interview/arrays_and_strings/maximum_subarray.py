import unittest

class Solution:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
    sum and return its sum.

    Complexity:
        Time O(n)
        Space O(1)

    Greedy Approach:
        The problem to find maximum (or minimum) element (or sum) with a single array as the input is a good
        candidate to be solved by the greedy approach in linear time.
        The algorithm is general and straightforward: iterate over the array and update at each step the
        standard set for such problems:
        - current element
        - current local maximum sum (at this given point)
        - global maximum sum seen so far.
    """
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        a = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertTrue(a == 6)
