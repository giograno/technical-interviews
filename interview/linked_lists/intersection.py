import unittest


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def intersect(l1: Node, l2: Node) -> Node:
    """
    Exercise 2.7. pag. 95
    Given two singly linked lists, determine if the two lists intersect.
    Return the intersecting node.

    Complexity:
        - Time O(N + M) where N is |l1| and M is |l2|
        - Space O(1)
    """
    temp1 = l1
    len1 = 0
    while temp1:
        len1 += 1
        temp1 = temp1.next

    temp2 = l2
    len2 = 0
    while temp2:
        len2 += 1
        temp2 = temp2.next

    longer = l1 if len1 > len2 else l2
    shorter = l1 if len1 <= len2 else l2
    diff = abs(len1-len2)
    for i in range(diff):
        longer = longer.next

    while longer and shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next

    return None


class TestSolution(unittest.TestCase):

    def test_solution(self):
        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(3)
        a4 = Node(4)
        a1.next = a2
        a2.next = a3
        a3.next = a4

        b1 = Node(5)
        b2 = Node(6)
        b1.next = b2
        b2.next = a3

        self.assertTrue(intersect(a1, b1) == a3)
