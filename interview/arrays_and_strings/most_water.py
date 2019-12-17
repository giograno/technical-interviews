class Solution:
    """
    Container with most water

    https://leetcode.com/problems/container-with-most-water/

    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Complexity:
        space O(1)
        time O(n)

    Core intuition:
        The intuition behind this approach is that the area formed between the lines will always be limited by the
        height of the shorter line. Further, the farther the lines, the more will be the area obtained.
    """
    def maxArea(self, height: [int]) -> int:

        s = 0
        j = len(height) - 1

        area = 0
        while s <= j:
            area = max(min(height[s], height[j]) * (j - s), area)

            if height[s] < height[j]:
                s += 1
            else:
                j -= 1
        return area

import unittest

class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        ans = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertTrue(ans == (7*7))
