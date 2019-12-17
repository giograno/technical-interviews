import unittest


def merge_sort(array: [int]) -> [int]:
    aux_merge_sort(array, [0]*len(array), 0, len(array)-1)


def aux_merge_sort(array: [int], temp: [int], start: int, end: int) -> [int]:
    if start < end:
        middle = int((start + end) / 2)
        aux_merge_sort(array, temp, start, middle)
        aux_merge_sort(array, temp, middle+1, end)
        merge_arrays(array, temp, start, middle, end)


def merge_arrays(array, temp, start, middle, end):
    for i in range(start, end+1):
        temp[i] = array[i]

    left_temp: int = start
    right_temp: int = middle + 1
    index: int = start

    while left_temp <= middle and right_temp <= end:
        if temp[left_temp] <= temp[right_temp]:
            array[index] = temp[left_temp]
            left_temp += 1
        else:
            array[index] = temp[right_temp]
            right_temp += 1
        index += 1

    remain: int = middle - left_temp
    for i in range(0, remain+1):
        array[index+i] = temp[left_temp+i]


class TestMerge(unittest.TestCase):

    def test_merge(self):
        a = [4, 1, 7, 2]
        merge_sort(a)
        self.assertTrue(a == sorted(a))

    def test_merge_empty(self):
        a = []
        merge_sort(a)
        self.assertTrue(a == [])

    def test_merge_two(self):
        a = [5, 3, 1, 7, 8, 9, 10, 1]
        merge_sort(a)
        self.assertTrue(a == sorted(a))

    def test_merge_sorted(self):
        a = [1, 2, 3, 4, 5]
        merge_sort(a)
        self.assertTrue(a == sorted(a))


if __name__ == '__main__':
    unittest.main()
