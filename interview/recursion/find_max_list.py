import unittest


def get_max(a_list: []) -> int:
    if len(a_list) == 0: return
    if len(a_list) == 1:
        if isinstance(a_list[0], list):
            return get_max(a_list[0])
        else:
            return a_list[0]
    else:
        return max(get_max(a_list[:1]), get_max(a_list[1:]))


class TestSolution(unittest.TestCase):

    def test_solution(self):
        test_list = [2, 4, 6, 8, [[11, 585], 100, [9, 7]], 5, 3, 1]
        self.assertTrue(get_max(test_list) == 585)

    def test_empty(self):
        self.assertTrue(get_max([]) == 0)


if __name__ == '__main__':
    unittest.main()
