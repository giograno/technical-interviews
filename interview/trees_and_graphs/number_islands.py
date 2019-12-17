class Solution:
    """
    Intuition
        Treat the 2d grid map as an undirected graph and there is an edge between two horizontally or vertically
        adjacent nodes of value '1'.
    Algorithm
        Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First
        Search. During DFS, every visited node should be set as '0' to mark as visited node.
        Count the number of root nodes that trigger DFS, this number would be the number of
        islands since each DFS starting at some root identifies an island.
    Complexity:
        O(MxN): M number of rows and N number of columns
    """
    def numIslands(self, grid: [[str]]) -> int:
        if len(grid) == 0:
            return 0
        # size of the grid
        h = len(grid) - 1
        w = len(grid[0]) - 1

        def dfs(row, col):
            if row < 0 or row > h or col < 0 or col > w or grid[row][col] == '0':
                return

            # mark as visited
            grid[row][col] = '0'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        islands = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands


import unittest

class TestSolution(unittest.TestCase):

    def testSolution(self):
        sol = Solution()
        input = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
        ans = sol.numIslands(input)
        self.assertTrue(ans == 1)

    def testTrivial(self):
        sol = Solution()
        input = [["1", "0"], ["0", "1"]]
        ans = sol.numIslands(input)
        self.assertTrue(ans == 2)




