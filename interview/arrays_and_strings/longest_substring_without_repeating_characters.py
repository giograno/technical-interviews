import unittest


class Solution:
    """
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
        j = 0
        i = 0
        my_set = set()
        len_string = len(s)
        max_value = 0
        while i < len_string and j < len_string:
            if s[j] not in my_set:
                my_set.add(s[j])
                j += 1
                max_value = max(max_value, j-i)
            else:
                my_set.remove(s[i])
                i += 1

        return max_value


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_solution(self):
        self.assertTrue(self.solution.length_of_longest_substring("abcabcbb") == 3)

    def test_solution2(self):
        self.assertTrue(self.solution.length_of_longest_substring("bbbbb") == 1)

    def test_solution3(self):
        self.assertTrue(self.solution.length_of_longest_substring("pwwkew") == 3)


if __name__ == '__main__':
    unittest.main()

