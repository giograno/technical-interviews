import unittest
from interview.data_structures.BinaryTree import TreeNode, example_tree, initiate_array_to_binary


class Solution:
    """
    Check Balanced
    @chapter 4
    @exercise 4.4
    @page 110
    Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced tree is
    defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
    - Time Complexity O(n)
    - Space Complexity O(h) where h is the height of the tree
    """
    def check_balance(self, root: TreeNode) -> bool:
        ans = self.get_level(root, 0)
        return False if ans == -1 else True

    def get_level(self, root: TreeNode, level: int):
        if not root:
            return level-1
        left = self.get_level(root.left, level+1)
        right = self.get_level(root.right, level+1)
        if left == -1 or right == -1:
            return -1
        is_bal = abs(left-right)
        return -1 if is_bal >= 1 else level


class TestSolution(unittest.TestCase):

    def test_balance(self):
        solution: Solution = Solution()
        tree = initiate_array_to_binary([1, 2, 3])
        self.assertTrue(solution.check_balance(tree))

    def test_balance_two(self):
        solution: Solution = Solution()
        tree = initiate_array_to_binary([1, 2, 3, 5, 6, 7, 8])
        self.assertTrue(solution.check_balance(tree))

    def test_solution(self):
        solution: Solution = Solution()
        tree = example_tree()
        self.assertFalse(solution.check_balance(tree))

    def test_not_balanced(self):
        solution: Solution = Solution()
        root = TreeNode(5)
        root.right = TreeNode(10)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(7)
        root.right.left = TreeNode(2)
        root.left = TreeNode(2)
        self.assertFalse(solution.check_balance(root))


if __name__ == '__main__':
    unittest.main()
