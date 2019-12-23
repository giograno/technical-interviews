class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        if l == 1:
            return

        if sorted(nums) == nums:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return

        if reversed(sorted(nums)) == nums:
            nums = sorted(nums)
            return

        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i += -1
            else:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                return

import unittest

class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        sol.nextPermutation([1, 2, 3])

    def test_solution_2(self):
        sol = Solution()
        sol.nextPermutation([2, 3, 1])
