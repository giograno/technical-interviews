# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        hash_map = set()

        def visit(root, k):
            if root:
                comp = k - root.val
                if comp in hash_map:
                    return True
                hash_map.add(root.val)
                return visit(root.left, k) or visit(root.right, k)

        found = visit(root, k)
        return True if found else False