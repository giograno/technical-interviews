# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # check the same object
        seen_nodes = set()

        while head:
            if head in seen_nodes:
                return True
            seen_nodes.add(head)
            # update the pointer
            head = head.next
        return False


    def has_cycle_recursive(self, head: ListNode) -> bool:
        # return False if we are at the end of the list
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True