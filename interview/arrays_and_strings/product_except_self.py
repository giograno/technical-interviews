class Solution:
    """
    Complexity O(n) both time and space

    We can reduce the memory to O(1) if we use the answer array to store first the left and then the product
    between the left and the right
    """
    def productExceptSelf(self, nums: [int]) -> [int]:
        l = len(nums)

        right, left = [0] * l, [0] * l

        left[0] = 1
        right[l - 1] = 1

        for i in range(1, l):
            left[i] = nums[i - 1] * left[i - 1]

        for i in reversed(range(l - 1)):
            right[i] = nums[i + 1] * right[i + 1]

        ans = [left[i] * right[i] for i in range(l)]
        return ans


import unittest


class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        ans = sol.productExceptSelf([1, 2, 3, 4])
        self.assertTrue(ans == [24, 12, 8, 6])