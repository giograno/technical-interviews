import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res

    # def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
    #     roots = []
    #     roots.append(root)
    #     for node in to_delete:
    #         for tree in roots:
    #             # find node
    #             temp = self.search(tree, node)
    #             if not temp:
    #                 continue
    #             candidate_node = temp[0]
    #             parent_node = temp[1]
    #             # check if is a parent node
    #             has_nodes, kids = self.has_nodes(candidate_node)
    #             # if so, the children become leafs
    #             if has_nodes:
    #                 roots.extend(kids)
    #
    #             if parent_node and parent_node.left and parent_node.left.val == node:
    #                 parent_node.left = None
    #             elif parent_node:
    #                 parent_node.right = None
    #             # update the roots
    #             if candidate_node in roots:
    #                 roots.remove(candidate_node)
    #             break
    #     return roots
    #
    # def has_nodes(self, root) -> tuple:
    #     kids = [node for node in [root.left, root.right] if node]
    #     return (
    #         len(kids) > 0,
    #         kids
    #     )
    #
    # def search(self, root: TreeNode, look: int) -> tuple:
    #     return self.helper(root=root, look=look)
    #
    # def helper(self, root: TreeNode, look: int, parent: TreeNode = None) -> tuple:
    #     if root:
    #         if root.val == look:
    #             return root, parent
    #         r = self.helper(root.left, look, root)
    #         if r:
    #             return r
    #         r = self.helper(root.right, look, root)
    #         if r:
    #             return r


class TestSolution(unittest.TestCase):

    def test_base(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        b = [3, 5]
        sol = Solution()
        sol.delNodes(root, b)

    def test_failing(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(3)
        b = [2, 3]
        sol = Solution()
        sol.delNodes(root, b)


if __name__ == '__main__':
    unittest.main()
