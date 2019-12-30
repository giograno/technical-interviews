import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some starting node to any node in the
    tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the root.
    """
    def maxPathSum(self, root):
        """
        - Initiate max_sum as the smallest possible integer and call max_gain(node = root).
        - Implement max_gain(node) with a check to continue the old path/to start a new path:
            - Base case : if node is null, the max gain is 0.
            - Call max_gain recursively for the node children to compute max gain from the left and right subtrees:
            left_gain = max(max_gain(node.left), 0) and right_gain = max(max_gain(node.right), 0).
            - Now check to continue the old path or to start a new path. To start a new path would cost
            price_newpath = node.val + left_gain + right_gain. Update max_sum if it's better to start a new path.
            - For the recursion return the max gain the node and one/zero of its subtrees could add to the current path:
            node.val + max(left_gain, right_gain).
        """

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.right = TreeNode(7)
        root.right.left = TreeNode(15)
        ans = sol.maxPathSum(root)
        self.assertTrue(ans == 42)
