class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        while self.stack and self.pointer != len(self.stack) - 1:
            self.stack.pop()
        
        self.stack.append(url)
        self.pointer = len(self.stack) - 1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.stack[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(len(self.stack) - 1, self.pointer + steps)
        return self.stack[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)