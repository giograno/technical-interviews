import numpy as np
import unittest


class Solution:
    def gardenNoAdj(self, N: int, paths: [[int]]) -> [int]:
        adj_list = {garden: [] for garden in range(1, N+1)}
        for connection in paths:
            adj_list[connection[0]].append(connection[1])
            adj_list[connection[1]].append(connection[0])

        possible_values = {}
        for val in range(1, N+1):
            possible_values[val] = set([1, 2, 3, 4])

        ans = []
        for garden in range(1, N+1):
            assign = min(possible_values[garden])
            # remove for connected lists
            for adj in adj_list[garden]:
                if assign in possible_values[adj]:
                    possible_values[adj].remove(assign)
            ans.append(assign)
        return ans




class TestSolution(unittest.TestCase):

    def test_sol1(self):
        sol = Solution()
        ans = sol.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]])
        self.assertTrue(ans==[1,2,3])

    def test_sol2(self):
        sol = Solution()
        ans = sol.gardenNoAdj(4, [[1,2],[3,4]])
        self.assertTrue(ans==[1,2,1,2])


    def test_sol3(self):
        sol = Solution()
        ans = sol.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
        self.assertTrue(ans==[1,2,3,4])


    def test_sol4(self):
        sol = Solution()
        ans = sol.gardenNoAdj(5, [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]])
        # self.assertTrue(ans==[1,2,3,4])

    def test_sol5(self):
        sol = Solution()
        ans = sol.gardenNoAdj(1000, [])
        # self.assertTrue(ans==[1,2,3,4])

if __name__ == '__main__':
    unittest.main()
