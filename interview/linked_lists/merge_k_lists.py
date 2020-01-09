class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Merge k sorted linked lists and return it as one sorted list
    """
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """Merge & Divide and Conquer Approach
        - Pair up k lists and merge each pair
        - After first pairing, k lists are merged into k/2 list with average 2N/k length, then k/4, k/8 and so on.
        - Repeat this procedure until we get the final sorted linked list
        We will traverse almost N nodes per pairing and merging and repeat this procedure about log2*k times.
        """
        def merge_lists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(-1)
            temp = dummy

            if not l1 and not l2:
                return None

            while l1 and l2:
                min_val = l1 if l1.val <= l2.val else l2
                temp.next = ListNode(min_val.val)
                if min_val == l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
                temp = temp.next

            left = l1 if l1 else l2
            temp.next = left
            return dummy.next

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge_lists(lists[0], lists[1])

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge_lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]
