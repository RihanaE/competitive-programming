class Node():
    def __init__(self, val= 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.home = self.head
        

    def visit(self, url: str) -> None:
        temp = Node(url)
        temp.prev = self.home
        self.home.next = temp
        self.home = self.home.next

    def back(self, steps: int) -> str:

        while steps and self.home.prev:
            self.home = self.home.prev
            steps -=1
            
        return self.home.val

    def forward(self, steps: int) -> str:
        while steps and self.home.next:
            self.home = self.home.next
            steps -=1
            
        return self.home.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)