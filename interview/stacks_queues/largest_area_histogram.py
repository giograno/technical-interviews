import unittest


class Solution:
    """
    Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
    find the area of largest rectangle in the histogram.

    LeetCode: https://leetcode.com/problems/largest-rectangle-in-histogram

    Complexity:
        O(n) both space and time

    YouTube video:
        https://www.youtube.com/watch?time_continue=2&v=RVIh0snn4Qc&feature=emb_logo
    """
    def largestRectangleArea(self, heights: [int]) -> int:

        stack = list()
        max_area = 0  # Initialize max area

        # Run through all bars of
        # given histogram
        index = 0
        while index < len(heights):

            # If this bar is higher
            # than the bar on top
            # stack, push it to stack

            if (not stack) or (heights[stack[-1]] <= heights[index]):
                stack.append(index)
                index += 1

            # If this bar is lower than top of stack,
            # then calculate area of rectangle with
            # stack top as the smallest (or minimum
            # height) bar.'i' is 'right index' for
            # the top and element before top in stack
            # is 'left index'
            else:
                # pop the top
                top_of_stack = stack.pop()

                # Calculate the area with
                # histogram[top_of_stack] stack
                # as smallest bar
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1)
                         if stack else index))

                # update max area, if needed
                max_area = max(max_area, area)

                # Now pop the remaining bars from
        # stack and calculate area with
        # every popped bar as the smallest bar
        while stack:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack]
            # stack as smallest bar
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)

            # Return maximum area under
        # the given histogram
        return max_area


class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        ans = sol.largestRectangleArea([1, 1])
        self.assertTrue(ans == 2)

    def testPreSolution(self):
        sol = Solution()
        ans = sol.largestRectangleArea([2,1,5,6,2,3])
        self.assertTrue(ans == 10)