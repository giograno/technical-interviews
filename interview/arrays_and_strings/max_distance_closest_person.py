import unittest


def max_dist_to_closest(seats: [int]) -> int:
    """
    In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
    There is at least one empty seat, and at least one person sitting.
    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
    Return that maximum distance to closest person

    Complexity: O(n)
    """
    n = len(seats)
    if n == 2:
        return 1
    left = [0] * n
    right = [0] * n

    for i in range(n):
        if seats[i] == 1:
            left[i] = 0
        elif i > 0:
            left[i] = left[i - 1] + 1

    for j in range(n - 1, -1, -1):
        if seats[j] == 1:
            right[j] = 0
        elif j < n - 1:
            right[j] = right[j + 1] + 1

    max_d = max(right[0], left[n-1])
    for l, r in zip(left[1:-1], right[1:-1]):
        d = min(l, r)
        if d > max_d:
            max_d = d
    return max_d


class TestSolution(unittest.TestCase):

    def test_solution(self):
        res = max_dist_to_closest([1, 0, 0, 0, 1, 0, 1])
        self.assertTrue(res == 2)

    def test_solution2(self):
        res = max_dist_to_closest([1, 0, 0, 0])
        self.assertTrue(res == 3)


if __name__ == '__main__':
    unittest.main()
