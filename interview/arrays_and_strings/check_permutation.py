import unittest


def sort_permutation(string_a, string_b):
    """
    @chapter 1
    @exercise 1.2
    @page 90
    Given two strings, write a method that decides if one is a permutation of the other.
    """
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)


def smart_permutation(string_a, string_b):
    """
    We use an array that works like an hash table, mapping each character to its frequency.
    We assume that the set of character is ASCII.
    We increment through the first string, we then decrement through the second. If they are permutation,
    then the array will be all zeros at the end.
    """
    if len(string_a) != len(string_b):
        return False

    counter = [0] * 128
    for elem in string_a:
        val = ord(elem)
        counter[val] += 1

    for elem in string_b:
        val = ord(elem)
        counter[val] -= 1
        if counter[val] < 0:
            return False
    return True


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(smart_permutation("ciao", "oiac"))
        self.assertFalse(smart_permutation("ciao", "ciap"))


if __name__ == '__main__':
    unittest.main()
