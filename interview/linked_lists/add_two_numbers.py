import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    """
    carry = 0
    dummy_head = ListNode(0)
    index = dummy_head

    while l1 is not None or l2 is not None:
        val1 = 0 if l1 is None else l1.val
        val2 = 0 if l2 is None else l2.val

        val = val1 + val2 + carry
        carry = 0 if val < 10 else 1
        val = val if val < 10 else val-10
        index.next = ListNode(val)
        index = index.next

        l1 = l1.next if l1 is not None else l1
        l2 = l2.next if l2 is not None else l2

    if carry > 0:
        index.next = ListNode(carry)

    return dummy_head.next


class TestSolution(unittest.TestCase):

    def test_solution(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        ans = add_two_numbers(l1, l2)
        self.assertTrue(ans.val == 7)
        self.assertTrue(ans.next.val == 0)
        self.assertTrue(ans.next.next.val == 8)


if __name__ == '__main__':
    unittest.main()
