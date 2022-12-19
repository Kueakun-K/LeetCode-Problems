class MinStack:

    def __init__(self):
        self.value = []

    def push(self, val: int) -> None:
        self.value.append((val, min(self.getMin(), val)))

    def pop(self) -> None:
        self.value.pop()

    def top(self) -> int:
        return self.value[-1][0]

    def getMin(self) -> int:
        if self.value:
            return self.value[-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()