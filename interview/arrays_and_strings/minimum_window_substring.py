import collections
import unittest


class Solution:
    """
    Given a string S and a string T, find the minimum window in S which will contain all the characters in
    T in complexity O(n).

    Example:

    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    """
    def minWindow(self, s: str, t: str) -> str:
        char_count = collections.defaultdict(int)
        chars = collections.Counter(t)
        # number of distict chars in t
        k = len(chars)
        l_s = len(s)
        start = 0
        min_str = float('+inf')
        max_index = min_index = 0

        seen = 0
        for end in range(l_s):
            temp_char = s[end]
            if temp_char in chars:
                if char_count[temp_char] == chars[temp_char] - 1:
                    seen += 1
                char_count[temp_char] += 1

            while seen == k:  # the window is complete
                if end - start + 1 < min_str:
                    min_str = end - start + 1
                    max_index, min_index = end + 1, start
                temp_start = s[start]
                start = start + 1
                if temp_start in chars:
                    if char_count[temp_start] == chars[temp_start]:
                        seen += -1
                    char_count[temp_start] += -1

        if min_str == float('+inf'): return ""
        return s[min_index:max_index]


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.minWindow("ADOBECODEBANC", 'ABC')
        self.assertEqual('BANC', ans)
