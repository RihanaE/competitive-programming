class BrowserHistory:

    def __init__(self, homepage: str):
        self.store = {0:homepage}
        self.pointer = 0
        self.length = 1

    def visit(self, url: str) -> None:
        self.store[self.pointer + 1] = url
        self.pointer += 1
        self.length = self.pointer + 1
    

    def back(self, steps: int) -> str:
        self.pointer = max(self.pointer - steps, 0)
        return self.store[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer + steps, self.length - 1)
        return self.store[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)