# Given the root node of a binary search tree, return the sum of values of all nodes with value
# between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)

        dfs(root)
        return self.ans