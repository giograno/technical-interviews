# Triple Step: a child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs


def staircase(n: int) -> int:
    """
    Brutal force solution; O(3^n) complexity (a bit less in truth), each branches calls out three more calls
    """
    if n == 0:
        return 1
    if n == 2 or n == 1:
        return n
    if n >= 3:
        return staircase(n-1) + staircase(n-2) + staircase(n-3)


def staircase_memoization(n: int) -> int:
    """
    Memoization solution; O(n) complexity
    """
    return memo_call(n, [-1] * (n+1))


def memo_call(n: int, memo: [int]) -> int:
    if n == 0:
        return 1
    if n == 2 or n == 1:
        return n
    if memo[n] == -1:
        memo[n] = memo_call(n-1, memo) + memo_call(n-2, memo) + memo_call(n-3, memo)
    return memo[n]


if __name__ == '__main__':
    assert staircase(3) == 4
    assert staircase_memoization(3) == 4
