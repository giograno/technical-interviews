import collections
import unittest


class Solution:
    """
    Given a non-empty array of integers, return the k most frequent elements.
    Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
    Note:
        Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    """
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        hm = collections.Counter(nums)
        hm = {k: v for k, v in sorted(hm.items(), key=lambda item: item[1])}
        return list(hm.keys())[-k:]

        # return heapq.nlargest(k, hm.keys(), key=hm.get)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
        self.assertTrue(ans == [1, 2] or ans == [2, 1])
