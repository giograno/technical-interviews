import collections
import unittest


class Solution:
    """
    There are a total of n courses you have to take, labeled from 0 to n-1.
    Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
    which is expressed as a pair: [0,1]
    Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should
    take to finish all courses.
    There may be multiple correct orders, you just need to return one of them.
    If it is impossible to finish all courses, return an empty array.
    """
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        """
        Algorithm (Topological sort)

        1. Initialize a queue, Q to keep a track of all the nodes in the graph with 0 in-degree.
        2. Iterate over all the edges in the input and create an adjacency list and also a map of node v/s in-degree.
        3. Add all the nodes with 0 in-degree to Q.
        4. The following steps are to be done until the Q becomes empty.
            4.1 Pop a node from the Q. Let's call this node, N.
            4.2 For all the neighbors of this node, N, reduce their in-degree by 1. If any of the nodes' in-degree
                reaches 0, add it to the Q.
            4.3 Add the node N to the list maintaining topologically sorted order.
            4.4 Continue from step 4.1.
        """
        adj_list = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree[dest] + 1

        # Queue for maintaining list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertTrue(ans == [0, 1, 2, 3])
