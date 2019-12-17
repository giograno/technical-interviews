from interview.data_structures.Stack_Array import Stack
import unittest


class SetOfStacks:

    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = [Stack(threshold)]

    def push(self, value):
        # if self.stacks[-1].is_empty()
        pass

    def pop(self):
        pass

    def popAt(self, index):
        pass


class TestSetOfStacks(unittest.TestCase):

    def test_smoke(self):
        sos = SetOfStacks(5)
