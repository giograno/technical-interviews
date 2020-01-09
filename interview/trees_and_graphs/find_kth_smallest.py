import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given a binary search tree, write a function `kthSmallest` to find the kth smallest element in it.
    Complexity:
        - Time O(H+k): where H is tree height. The complexity is defined by the stack, which contains at least H+k
        elements since before starting to pop out one has to go down to a leaf.
        - Memory O(H+k) same as time

    """
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def traversal(root):
            nonlocal nodes

            if root:
                traversal(root.left)
                if len(nodes) == k:
                    return
                nodes.append(root.val)
                traversal(root.right)

        nodes = []
        traversal(root)
        return nodes[k - 1]


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        tree = TreeNode(3)
        tree.left = TreeNode(1)
        tree.left.right = TreeNode(2)
        tree.right = TreeNode(4)
        ans = sol.kthSmallest(tree, k=1)
        self.assertEqual(1, ans)
