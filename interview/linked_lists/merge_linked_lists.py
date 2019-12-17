class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    index = dummy
    while l1 is not None or l2 is not None:
        val1 = l1.val if l1 is not None else -1
        val2 = l2.val if l2 is not None else -1
        if val1 < val2 or val2 == -1:
            index.next = ListNode(val1)
            l1 = l1.next if l1 is not None else l1
        elif val1 >= val2 or val1 == -1:
            index.next = ListNode(val2)
            l2 = l2.next if l2 is not None else l2
        index = index.next

    return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    res = merge_two_list(l1,l2)

    print(res.val)