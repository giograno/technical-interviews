import unittest


class Solution:
    """
    We first sort the intervals for the first element.
    Then, we iterate over the intervals using two arrays.
    2 intervals overlap if start(i+1) < end(i)
    We can have 3 possibilities:
        - not overlap: we just move the pointers
        - overlap and i+1 totally included in i: we skip the longer
            interval (i)
        - overlap and i+1 longer: we keep the first interval and skip
            the second (i+1)

    Complexity:
        - Time O(n *log n)
        - Memory O(1)
    """
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals = sorted(intervals)
        n = len(intervals)

        if n == 1: return 0

        i = 0
        j = 1

        skips = 0

        while j < n:
            s = intervals[i]
            e = intervals[j]
            if e[0] < s[1]:      # they overlap
                if e[1] < s[1]:  # second interval contained in the first
                    i = j
                skips += 1
            else:
                i = j
            j += 1
        return skips


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        a = [[1, 100], [11, 22], [1, 11], [2, 12]]
        ans = sol.eraseOverlapIntervals(a)
        self.assertTrue(ans == 2)
