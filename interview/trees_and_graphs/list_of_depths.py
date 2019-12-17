from interview.data_structures.LinkedList import SingleLinkedList
from interview.data_structures.BinaryTree import initiate_array_to_binary, TreeNode
import unittest


class Solution:
    """
    List of Depths
    @chapter 4
    @exercise 4.3
    @page 109
    Given a binary tree, design an algorithm, which creates a linked list of all the nodes at each depth (e.g.,
    if you have a tree with depth D, you'll have D linked lists)
    """
    def __init__(self):
        self.ll_list = {}

    def list_of_depths(self, root: TreeNode, level: int):
        if root:
            if level not in self.ll_list:
                ll = SingleLinkedList()
                ll.add(root.value)
                self.ll_list[level] = ll
            else:
                self.ll_list[level].add(root.value)
            self.list_of_depths(root.left, level+1)
            self.list_of_depths(root.right, level+1)

    def __str__(self):
        values = [str(self.ll_list[ll]) for ll in self.ll_list]
        return '\n'.join(values)


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def testSolution(self):
        l_graph = initiate_array_to_binary([1, 2, 3, 4, 5, 6, 7, 8])
        self.solution.list_of_depths(l_graph, 0)
        print(self.solution)
        self.assertTrue(len(self.solution.ll_list) == 4)

    def testEmptyInput(self):
        l_graph = initiate_array_to_binary([])
        self.solution.list_of_depths(l_graph, 0)
        self.assertTrue(len(self.solution.ll_list) == 0)


if __name__ == '__main__':
    unittest.main()

