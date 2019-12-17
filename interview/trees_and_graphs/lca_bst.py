# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Intuition: the split point is when the two values are not in different subtrees
        """
        p_val = p.val
        q_val = q.val

        # look in the left subtree
        if p_val < root.val and q_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > root.val and q_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
