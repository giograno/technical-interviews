# Reverse a singly linked list.
# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:
#
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        first = None

        while head:
            next_node = head.next
            head.next = first
            first = head
            head = next_node
        return first

    def reverseRecursively(self, head: ListNode) -> ListNode:
        # traverse till the end to find the new head
        if not head or not head.next:
            return head
        p = self.reverseRecursively(head.next)
        # reverse the indexes
        head.next.next = head
        head.next = None
        return p

