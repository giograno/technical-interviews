import collections
import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution with usage of hash map
        Complexity:
            O(n) time
            O(n) memory

        Alternative: we could also use an array of size 25 (122-97)
        and use the ord() method to get the ascii value of every single
        letter. Hash is more general
        """
        ans = collections.defaultdict(int)
        for element in s:
            ans[element] += 1

        for element in t:
            ans[element] -= 1

        for val in ans:
            if ans[val] != 0:
                return False
        return True

    def isAnagramSlower(self, s: str, t: str) -> bool:
        """
        Accepted version with sorting
        Complexity Analysis:
            O(n log n) time
            O(1) memory
        """
        return sorted(s) == sorted(t)


class TestSolution(unittest.TestCase):

    def test_anagram(self):
        sol = Solution()
        self.assertTrue(sol.isAnagram("anagram", "nagaram"))
        self.assertFalse(sol.isAnagram("rat", "cat"))
