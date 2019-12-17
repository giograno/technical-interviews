class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answers = set()
        self.dfs(answers, tiles, "", len(tiles))
        return len(answers)

    def dfs(self, answers, possible_tiles, curr, n):
        if len(curr) <= n and curr != '':
            answers.add(curr)

        for i in range(0, len(possible_tiles)):
            self.dfs(answers, possible_tiles[:i] + possible_tiles[i + 1:], curr + possible_tiles[i], n)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.numTilePossibilities("AAB")
    print(ans)
