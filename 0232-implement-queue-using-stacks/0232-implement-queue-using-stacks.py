class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # self.stack_2.append(x)
       

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop(0)
           
        
    def peek(self) -> int:
        if self.stack:
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()