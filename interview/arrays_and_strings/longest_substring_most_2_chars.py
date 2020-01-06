import collections
import unittest


class Solution:
    """
    Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
    Example:
        Input: "eceba"
        Output: 3
        Explanation: t is "ece" which its length is 3.
    """
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        Sliding Window Algorithm:
            - Return N if the string length N is smaller than 3.
            - Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring
            length max_len = 2.
            - While right pointer is less than N:
                - If hashmap contains less than 3 distinct characters, add the current character s[right] in the
                hashmap and move right pointer to the right.
                - If hashmap contains 3 distinct characters, remove the leftmost character from the hashmap and move
                the left pointer so that sliding window contains again 2 distinct characters only.
                - Update max_len.

        Complexity:
            - Both time and space O(N)
        """
        hash_map = collections.defaultdict(int)
        n = len(s)
        distinct_chars = start = end = ans = 0

        while end < n:
            # 0 for that letter
            if hash_map[s[end]] == 0:
                distinct_chars += 1
            hash_map[s[end]] += 1
            end += 1
            while distinct_chars > 2:
                # move start up
                if hash_map[s[start]] == 1:
                    distinct_chars += -1
                hash_map[s[start]] += -1
                start += 1
            ans = max(ans, end - start)
        return ans


class TestSolution(unittest.TestCase):

    def test_case(self):
        sol = Solution()
        ans = sol.lengthOfLongestSubstringTwoDistinct("ccaabbb")
        self.assertEqual(5, ans)

