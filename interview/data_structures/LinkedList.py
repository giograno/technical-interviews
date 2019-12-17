class LinkedListNode:

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class SingleLinkedList:
    """
    A linked list is a structure that represents a sequence of nodes.
    In a singly linked list, each node points to the next node in the linked list.
    It does not provide constant access time to a particular index, i.e., to find the 
    Kth element in the list, you need to iterate over k elements.
    However, it is possible to add and delete elements from the beginning of the list 
    in constant time. 
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, next_node=self.head)
    
    def delete_at_index(self, index):
        if index == 0:
            self.head = self.head.next
            return

        for i, node in enumerate(self):
            if i == index-1:
                prec_node = node
                break
        if prec_node.next.next: prec_node.next = prec_node.next.next
        else:
            prec_node.next = None
            self.tail = prec_node


class DoubleLinkedList(SingleLinkedList):

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail)
            self.tail = self.tail.next

import unittest

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SingleLinkedList()
        self.ll.add(5)
        self.ll.add(6)
        self.ll.add(7)

    def test_add(self):
        self.assertTrue(self.ll.head.value == 5)
        self.assertTrue(self.ll.tail.value == 7)
    
    def test_add_beginning(self):
        ll = SingleLinkedList()
        ll.add(6)
        ll.add_to_beginning(5)
        self.assertTrue(ll.head.value == 5)

    def test_delete(self):
        self.ll.delete_at_index(1)
        self.assertTrue(self.ll.head.next.value == 7)

    def test_delete_head(self):
        self.ll.delete_at_index(0)
        self.assertTrue(self.ll.head.value == 6)

    def test_delete_tail(self):
        self.ll.delete_at_index(2)
        self.assertTrue(self.ll.tail.value == 6)


class TestDoubleLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = DoubleLinkedList()
        self.ll.add(5)
        self.ll.add(6)
        self.ll.add(7)

    def test_add(self):
        self.ll.add(8)
        self.assertTrue(self.ll.tail.value == 8)
        self.assertTrue(self.ll.tail.prev.value == 7)


if __name__ == '__main__':
    unittest.main()
