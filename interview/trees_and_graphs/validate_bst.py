import unittest
from interview.data_structures.BinaryTree import *


def validate_bst(root):
    """
    Validate BST
    Implement a function to check if a binary tree is a binary search tree
    @chapter 4
    @exercise 4.5
    @page 110
    """
    return check_BST(root, None, None)


def check_BST(root: TreeNode, min: int, max: int):
    if not root:
        return True
    if (not min and root.value <= min) or (not max and root.value > max):
        return False
    if (check_BST(root.left, min, root.value)) or (check_BST(root.right, root.value, max)):
        return False
    return True


def is_valid_BST(root: TreeNode):
    """
    Solution of leetcode same problem.
    We can simply to an in-order visit and check whether the oerder
    """
    ans = []

    def in_order(root):
        if root:
            in_order(root.left)
            ans.append(root.val)
            in_order(root.right)

    in_order(root)
    for i in range(len(ans) - 1):
        if ans[i] >= ans[i + 1]:
            return False
    return True


class TestSolution(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
