import unittest
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given a binary tree, return the level order traversal of its nodes' values.
    (ie, from left to right, level by level).
    https://leetcode.com/problems/binary-tree-level-order-traversal/

    Complexity:
        - O(n) time
        - O(n) memory
    """
    def levelOrder(self, root: TreeNode) -> [[int]]:

        def bfs(root: TreeNode):
            if not root:
                return None
            nonlocal ans
            visited = set()

            queue = collections.deque()
            queue.append((root, 0))
            visited.add(root)

            while len(queue) > 0:
                elem, level = queue.popleft()
                ans[level].append(elem.val)
                for children in [elem.left, elem.right]:
                    if children and children not in visited:
                        queue.append((children, level + 1))
                        visited.add(children)

        ans = collections.defaultdict(list)
        bfs(root)
        return ans.values()


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.right = TreeNode(7)
        root.right.left = TreeNode(15)
        ans = sol.levelOrder(root)
        self.assertTrue(str(ans) == 'dict_values([[3], [9, 20], [15, 7]])')
