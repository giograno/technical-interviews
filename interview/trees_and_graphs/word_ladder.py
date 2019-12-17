import collections
import unittest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:

        adj_matrix = collections.defaultdict(list)

        len_w = len(beginWord)
        # keys are the intermediate representations
        for word in wordList:
            for index in range(len_w):
                intermediate = word[:index] + '*' + word[index+1:]
                adj_matrix[intermediate].append(word)

        queue = collections.deque()
        visited = set()

        # we also need to keep the level of a node into considerations
        def bfs(queue, start, target) -> int:
            queue.append((start, 1))
            visited.add(start)
            while len(queue) > 0:
                q, l = queue.popleft()

                # all possible intermediate
                for i in range(len_w):
                    intermediate_w = q[:i] + '*' + q[i+1:]

                    for n in adj_matrix[intermediate_w]:
                        print(n)
                        if n == target:
                            return l + 1
                        if n not in visited:
                            queue.append((n, l+1))
                            visited.add(n)
                # adj_matrix[intermediate_w] = []
            return 0

        count = bfs(queue, beginWord, endWord)
        return count


class TestSolution(unittest.TestCase):

    def test_solution(self):
        solution = Solution()
        ans = solution.ladderLength('a', 'c', ['a', 'b', 'c'])
        print(ans)
        self.assertTrue(ans == 2)

    def test_solution2(self):
        s = "hot"
        e = "dog"
        w = ["hot", "dog", "dot"]
        sol = Solution()
        ans = sol.ladderLength(s, e, w)
        print(ans)
        self.assertTrue(ans == 3)
