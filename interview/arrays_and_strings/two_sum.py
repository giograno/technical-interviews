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


class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()
        self.assertTrue(solution.two_sum([2, 7, 11, 15], 9) == [0, 1])


if __name__ == '__main__':
    unittest.main()
    