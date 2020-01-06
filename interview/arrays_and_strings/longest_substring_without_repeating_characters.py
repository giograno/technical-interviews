import unittest
import collections


class Solution:
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Given a string, find the length of the longest substring without repeating characters
    Example:
        Input: "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Input: "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    def length_of_longest_substring(self, s: str) -> int:
        """
        Solution with sliding window
        Complexity:
            - O(2n) -> O(n)
        """
        hash_map = collections.defaultdict(int)
        l = len(s)
        max_len = start = 0

        for end in range(l):
            hash_map[s[end]] += 1

            # there is a repetition of characters
            while hash_map[s[end]] > 1:
                hash_map[s[start]] += -1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len

    def improved_longest_substring(self, s: str) -> int:
        """
        The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps.
        Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to
        its index. Then we can skip the characters immediately when we found a repeated character.

        The reason is that if s[j] has a duplicate in the range [i,j) with index j', we don't need to increase
        i little by little. We can skip all the elements in the range [i,j'] and let i to be j+1 directly.
        """
        hash_map = collections.defaultdict(int)
        l = len(s)
        max_len = start = 0

        for end in range(l):
            if s[end] in hash_map:
                start = max(hash_map[s[end]], start)

            max_len = max(max_len, end - start + 1)
            hash_map[s[end]] = end + 1

        return max_len


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.length_of_longest_substring("abcabcbb") == 3)

    def test_solution2(self):
        self.assertTrue(self.solution.length_of_longest_substring("bbbbb") == 1)

    def test_solution3(self):
        self.assertTrue(self.solution.length_of_longest_substring("pwwkew") == 3)

    def test_improved_solution(self):
        self.assertTrue(self.solution.improved_longest_substring("pwwkew") == 3)


if __name__ == '__main__':
    unittest.main()

