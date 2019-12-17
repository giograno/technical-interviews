class Solution:

    def oddEvenJumps(self, A) -> int:
        if len(A) == 1:
            return 1

        possibilities = 0
        for index in range(len(A) - 1):
            val = A[index]
            jumps = 1
            possibilities += self.check(jumps, val, A[index + 1:])

    def check(self, jumps, old_val, A):
        if len(A) == 1:
            return 1

        if jumps % 2 == 0 and old_val >= A[0] and max(A) == A[0]:
            self.check(jumps + 1, A[0], A[1:])
        elif jumps % 2 != 0 and old_val <= A[0] and min(A) == A[0]:
            self.check(jumps + 1, A[0], A[1:])
        return 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.oddEvenJumps([10, 13, 12, 14, 15])
    print(res)
