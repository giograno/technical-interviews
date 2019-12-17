import unittest


class Stack:
    """
    Implementation of a stack using an array
    """
    def __init__(self, max_size):
        self.l = [-1] * max_size
        self.max_size = max_size
        self.dimension = 0

    def add(self, value) -> None:
        """Implement the add method in O(1)"""
        if self.dimension == self.max_size:
            print('array is full')
            return
        self.l[self.dimension] = value
        self.dimension += 1

    def pop(self) -> object:
        """Implement the pop in O(1)"""
        if self.dimension > 0:
            top = self.l[self.dimension - 1]
            self.l[self.dimension - 1] = -1
            self.dimension += -1
            return top

    def is_empty(self) -> bool:
        return self.dimension == 0

    def __str__(self):
        return str(self.l)


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack(10)

    def test_add(self):
        self.stack.add(5)
        self.assertTrue(self.stack.pop() == 5)
        self.assertTrue(self.stack.is_empty())

    def test_pop(self):
        self.stack.add(2)
        self.stack.add(4)
        self.assertTrue(self.stack.pop() == 4)
        self.assertTrue(self.stack.pop() == 2)
        self.assertTrue(self.stack.is_empty())

