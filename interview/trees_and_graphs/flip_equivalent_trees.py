class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    For a binary tree T, we can define a flip operation as follows: choose any node and swap the left and the
    right child subtrees.
    A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some
    number of flip operations.

    Write a function that determines whether two binary trees are flip equivalent.
    Thr trees are given by root nodes root1 and root2

    Complexity:
        Time: O(min(n1,n2)) where n1, n2 are the lengths of root1 and root2
        Space: O(min(h1,h2)) where h1, h2 are the heights of root1 and root2
    """
    def flipEquiv(self, root1, root2):
        # same leaf value
        if root1 is root2:
            return True
        # if one is null, also the others should be.
        # check the values otherwise
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # at least one of the flip should be equivalent
        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))

