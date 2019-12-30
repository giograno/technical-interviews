import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        # first element in predorder is root, then find the root index in inorder
        # whatever comes before root in inorder is left subtree
        # whatever comes after root in inorder is right subtree
        # do this recursively
        root = TreeNode(preorder[0])
        inorder_root_idx = inorder.index(preorder[0])
        left_len = inorder_root_idx
        root.left = self.buildTree(preorder[1:(1+left_len)], inorder[0:inorder_root_idx])
        root.right = self.buildTree(preorder[1+left_len:], inorder[inorder_root_idx+1:])
        return root


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        print('done')

    def test_empty(self):
        sol = Solution()
        ans = sol.buildTree([], [])
        print('done')