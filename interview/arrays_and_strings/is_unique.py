import unittest


def check_unique_string(my_string):
    """
    Is Unique
    @chapter 1
    @exercise 1.1
    @page 90
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot yse additional data structures?
    """
    if len(my_string) > 128:
        return True

    char_set = [False] * 128
    for elem in my_string:
        val = ord(elem)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertFalse(check_unique_string('this is a test'))
        self.assertTrue(check_unique_string('thisagodr'))


if __name__ == '__main__':
    unittest.main()