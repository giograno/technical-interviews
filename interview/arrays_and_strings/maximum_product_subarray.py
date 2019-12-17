class Solution:
    """
    Maximum Product Subarray

    https://leetcode.com/problems/maximum-product-subarray/

    Given an integer array nums, find a contiguous subarray within an array (containing at least one number)
    which has the largest product.

    Solution:
        this is a variation of the Kadane Algorithm. The difficult part comes in when dealing with negative
        numbers (a multiplication between two big negative numbers is a big positive number).
        For this reason, we keep trace of the local minimum and we check the local maximum also multiplying the
        current num to the local minimum.

    Complexity:
        Time O(n)
        Space O(1)
    """
    def maxProduct(self, nums: [int]) -> int:
        global_max = nums[0]
        local_max = nums[0]
        local_min = nums[0]

        for i in range(1, len(nums)):
            t = local_max
            local_max = max(max(local_max * nums[i], local_min * nums[i]), nums[i])
            local_min = min(min(local_min * nums[i], t * nums[i]), nums[i])
            global_max = max(local_max, global_max)
        return global_max

import unittest

class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.maxProduct([2, 3, -2, 4])
        self.assertTrue(ans == 6)

    def test_solution_2(self):
        sol = Solution()
        ans = sol.maxProduct([-1, 0, -1])
        self.assertTrue(ans == 0)
