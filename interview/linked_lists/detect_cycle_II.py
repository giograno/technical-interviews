class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode.com/problems/linked-list-cycle-ii/

    Given a linked list, return the node where the cycle begins. If there is no cycle, return None.
    To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
    the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Floid's Tortoise and Hare Algorithm

        Floyd's algorithm is separated into two distinct phases.
        - In the first phase, it determines whether a cycle is present in the list. If no cycle is present,
        it returns null immediately, as it is impossible to find the entrance to a non-existing cycle.
        Otherwise, it uses the located "intersection node" to find the entrance to the cycle.
        - Given that phase 1 finds an intersection, phase 2 proceeds to find the node that is the entrance to the cycle.
        To do so, we initialize two more pointers: ptr1, which points to the head of the list, and ptr2, which points
        to the intersection. Then, we advance each of them by 1 until they meet; the node where they meet is the
        entrance to the cycle, so we return it.
        """
        def findLoop(head: ListNode) -> ListNode:
            if not head:
                return None
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return slow
            return None

        def findNode(head: ListNode) -> ListNode:
            end = findLoop(head)
            if not end:
                return None

            start = head
            while start != end:
                start = start.next
                end = end.next
            return start

        return findNode(head)

