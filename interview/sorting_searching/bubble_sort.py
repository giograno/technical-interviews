import unittest


def bubble_sort(array: [], element: int) -> False:
    if len(array) == 0:
        return False
    return recursive_call(array=array, element=element, start=0, end=len(array)-1)


def recursive_call(array: [], element: int, start: int, end: int) -> bool:
    if start == end and array[start] == element:
        return True

    if start < end:
        middle = int((start+end)/2)
        return recursive_call(array, element, start, middle) or recursive_call(array, element, middle+1, end)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        a = [2, 5, 7, 8, 4]
        self.assertTrue(bubble_sort(array=a, element=8))

    def test_error(self):
        a = [2, 5, 7, 8, 4]
        self.assertFalse(bubble_sort(array=a, element=9))


if __name__ == '__main__':
    unittest.main()


