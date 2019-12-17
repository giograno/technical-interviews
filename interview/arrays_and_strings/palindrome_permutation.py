import unittest


def palindrome_permutation(palindrome):
    """
    Palindrome Permutation
    @chapter 1
    @exercise 1.4
    @page 91
    Given a string, write a function that check whether a permutation of the string that is a palindrome exists
    """
    table = [0] * (ord('z')-ord('a')+1)
    
    for elem in palindrome:
        val = get_char(elem)
        if val != 1:
            table[val] += 1

    odd = 0
    even = 0
    for elem in table:
        if elem % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True


def get_char(elem):
    val = ord(elem)
    if ord('z') <= val <= ord('a'):
        return val
    else:
        return -1


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(palindrome_permutation('tact coa'))


if __name__ == '__main__':
    unittest.main()
