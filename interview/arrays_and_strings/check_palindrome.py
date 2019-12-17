import unittest


def check_palindrome(word):
    """
    Check if a word is a palindrome
    Complexity: O(n)
    """
    if len(word) <= 1:
        return True

    s, e = 0, len(word) - 1

    while s < e:
        if word[s] != word[e]:
            return False
        else:
            s += 1
            e -= 1
    return True


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertFalse(check_palindrome("ciao"))
        self.assertTrue(check_palindrome("acca"))
        self.assertTrue(check_palindrome("acbca"))
        self.assertTrue(check_palindrome(""))


if __name__ == '__main__':
    unittest.main()
