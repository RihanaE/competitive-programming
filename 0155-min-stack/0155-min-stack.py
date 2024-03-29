class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = []
        self.min_val = float("inf")
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        self.min_val = min(self.min_val, val)
        
        self.mn.append(self.min_val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.mn.pop()
        
        if self.mn:
            self.min_val = self.mn[-1]
            
        else:
            self.min_val = float("inf")
            
        
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.mn:
            return self.mn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()