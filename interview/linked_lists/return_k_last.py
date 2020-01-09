import collections 
from interview.data_structures.LinkedList import SingleLinkedList

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def k_to_the_last_iterative(linked_list, k):
    size_counter = 0
    for _ in linked_list:
        size_counter += 1

    index = size_counter-k-1

    index_counter = 0
    for el in linked_list:
        if index_counter == index:
            return el
        index_counter += 1


def k_to_the_last_indexes(linked_list, k):
    first_pointer = linked_list.get_head()
    second_pointer = linked_list.get_head()
    
    first_index = 0
    second_index = 0

    if first_index is None:
        return None

    n = 0
    while first_pointer.get_next() is not None:
        # move second pointer
        if second_pointer.get_next() is not None:
            second_index += 1
            second_pointer = second_pointer.get_next()
            if second_pointer.get_next() is not None:
                second_index += 1 
                second_pointer = second_pointer.get_next()
        else:
            n = second_index
        print(n)
        if n == 0:
            first_pointer = first_pointer.get_next()
            first_index += 1
        elif n-k-1 == first_index:
            return first_pointer.get_next().get_data()


if __name__ == '__main__':
    lst = collections.deque()
    lst.append(5)
    lst.append(4)
    lst.append(5)
    lst.append('ciao')
    print(lst)
    res = k_to_the_last_iterative(lst, 2)
    assert res == 4

    my_ll = SingleLinkedList()
    my_ll.append
    my_ll.append(5)
    my_ll.append(15)
    my_ll.append_to_head(1)
    my_ll.append(5)
    print(my_ll)
    res =  k_to_the_last_indexes(my_ll, 2)
    print(res)
