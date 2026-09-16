class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.minimums: List[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimums or self.minimums[-1] > val:
            self.minimums.append(val)
        else:
            self.minimums.append(self.minimums[-1])
    def pop(self) -> None:
        val = self.stack.pop()
        self.minimums.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
