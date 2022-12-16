class MyQueue:
    def __init__(self):
        self.item = []

    def push(self, x: int) -> None:
        self.item.append(x)

    def pop(self) -> int:
        return self.item.pop(0)

    def peek(self) -> int:
        return self.item[0]

    def empty(self) -> bool:
        return self.item == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1) 
print(myQueue.item)
myQueue.push(2)
print(myQueue.item)
print(myQueue.peek()) 
print(myQueue.pop()) 
print(myQueue.item)
print(myQueue.empty()) 
