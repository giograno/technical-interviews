class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Leetcode: https://leetcode.com/problems/path-sum/
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
    along the path equals the given sum.
    Note: A leaf is a node with no children.

    Complexity:
        - Time O(n)
        - Memory O(n)
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def dfs(root: TreeNode, temp: int) -> bool:
            if not root:
                return False
            if root.val == temp and (not root.left and not root.right):
                return True

            return dfs(root.left, temp - root.val) or dfs(root.right, temp - root.val)

        return dfs(root, sum)
