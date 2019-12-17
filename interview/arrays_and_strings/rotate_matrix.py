import unittest


def rotate_matrix(matrix: []) -> []:
    """
    Exercise 1.7 cracking the coding interview
    Write a method to rotate a matrix by 90 degrees
    """
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            matrix[first][i], matrix[last-offset][first], matrix[last][last-offset], matrix[i][last] = \
                matrix[last-offset][first], matrix[last][last-offset], matrix[i][last], matrix[first][i]
    return matrix

class TestSolution(unittest.TestCase):

    def test_solution(self):
        m = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.assertTrue(rotate_matrix(m) == expected)
