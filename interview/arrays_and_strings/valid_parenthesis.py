class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        pairs = {')': '(',
                 ']': '[',
                 '}': '{'}

        for i, val in enumerate(s):
            is_open = val in opening
            if is_open:
                stack.append(val)
            elif not is_open and len(stack) > 0:
                top = stack.pop()
                if top != pairs[val]:
                    return False
            else:
                return False
        return len(stack) == 0


import unittest

class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.isValid("()")
        self.assertTrue(ans)

    def test_not_valid(self):
        sol = Solution()
        ans = sol.isValid("{[}]")
        self.assertFalse(ans)
