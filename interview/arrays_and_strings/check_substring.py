import unittest



def check_substring(src: [str], key: str) -> [str]:
    """
    Suppose you an an array os strings 'src' and a string 'key'.
    Now return all the string from the 'src' array that contains the key as substring in them.
    """
    answer = [res for res in src if is_in(res, key)]
    return answer


def pythonic_solution(src: [str], key: str) -> [str]:
    """
    Same solution, very compact and pythonic way, it hides the details
    """
    return [res for res in src if key in res]


def is_in(src: str, key: str) -> bool:
    """
    The complexity is O(m*n)  where m and n are the lengths of src and key respectively.
    More efficient solutions, O(n) exists, like the KMP algorithm.
    :param src: the original string
    :param key: substring to check in the string
    """
    len_string = len(src)
    len_key = len(key)

    for i in range(len_string-len_key-1):
        for j in range(len_key):
            if src[i+j] != key[j]:
                break
        if j+1 == len_key: return True
    return False


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.key = 'craft'
        self.src = ["minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"]

    def test_solution(self):
        self.assertTrue(check_substring(self.src, self.key) == ['minecraftgame', 'innercrafttalent', 'stonecrafter'])

    def test_pythonic(self):
        self.assertTrue(pythonic_solution(self.src, self.key) == ['minecraftgame', 'innercrafttalent', 'stonecrafter'])


if __name__ == '__main__':
    unittest.main()
