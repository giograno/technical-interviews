import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
    with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
    The tree s could also be considered as a subtree of itself.

    Complexity:
        - Time O(M*N)
        - Memory O(M*N)
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def equals(s, t):
            if not s and not t: return True
            if not s or not t: return False

            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)

        def traverse(s, t):
            sub = s and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))
            return sub

        return traverse(s, t)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        solution = Solution()
        ans = solution.isSubtree(s, t)
        self.assertTrue(ans)