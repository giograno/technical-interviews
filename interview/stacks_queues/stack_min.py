class MinStack:
    """
    Pag 98, exercise 3.2 on cracking the coding interview
    Also https://leetcode.com/problems/min-stack/submissions/

    Design a stack which, in addition to push and pop, has a function min which returns the minimum element
    They should operate in O(1) time

    Tip:
        Sometime it might be convenient to push on the stack additional information (i.e., the minimum in this case)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
            return
        last_insert = self.stack[-1]
        self.stack.append(
            (x, min(last_insert[1], x))
        )

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]