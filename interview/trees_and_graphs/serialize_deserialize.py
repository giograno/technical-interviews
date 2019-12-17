import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tree_repr = "["
        temp = self.pre_order_visit(root, [])
        # need to implement a pass over the array
        clean = []
        # indexes to skip
        to_skip = []
        for i, val in enumerate():
            # for a parent at index p, the children are at index (p+1)*2 and (p+1)*2 + 1
            if val == 'null' and i not in to_skip:
                to_skip.append(i * 2)
                to_skip.append(i * 2 + 1)
            else:
                pass



        tree_repr += ','.join(temp)
        tree_repr += "]"
        return tree_repr

    def pre_order_visit(self, root, tree: []):
        if not root:
            tree.append("null")
            return
        else:
            tree.append("{}".format(root.val))
            self.pre_order_visit(root.left, tree)
            self.pre_order_visit(root.right, tree)
        return tree


class TestSolution(unittest.TestCase):

    def test_serialize(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        root.right.left = TreeNode(4)
        sol = Codec()
        ans = sol.serialize(root)
        print(ans)
        self.assertTrue(ans == '[1,2,3,null,null,4,5]')

    def test_serialize_deep(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        root.right.left = TreeNode(4)
        sol = Codec()
        ans = sol.serialize(root)
        print(ans)
        # self.assertTrue(ans == '[1,null,3,,4,5]')