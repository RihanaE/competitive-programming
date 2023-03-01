class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.right = 0
        self.left = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.deque[(self.left - 1) % self.k] == None:
            self.deque[(self.left - 1) % self.k] = value
            
            self.left = (self.left - 1) % self.k
            return True
            
        return False

    def insertLast(self, value: int) -> bool:
        if self.deque[(self.right) % self.k] == None:
            self.deque[(self.right) % self.k] = value
            self.right = (self.right + 1) % self.k
            return True
        
        return False
#         if self.deque[(self.right + 1) % self.k] == None:
            
#             self.deque[(self.right + 1) % self.k] = value
#             self.right = (self.right + 1) % self.k
#             return True
        
#         return False
        

    def deleteFront(self) -> bool:
        if self.deque[self.left] != None:
            self.deque[self.left] = None
            self.left = (self.left + 1) % self.k
            return True
        
        return False
        

    def deleteLast(self) -> bool:
        if self.deque[(self.right - 1) % self.k] != None:
            self.deque[(self.right - 1) % self.k] = None
            self.right = (self.right - 1) % self.k
            return True
        
        return False
    
            
        
#         if self.deque[self.right] != None:
#             self.deque[self.right] = None
#             self.right = (self.right - 1) % self.k
#             return True
        
#         return False
            
        

    def getFront(self) -> int:
        if self.deque[self.left] != None:
            return self.deque[self.left]
        
        return -1
        

    def getRear(self) -> int:
        if self.deque[(self.right - 1) % self.k] != None:
            return self.deque[(self.right - 1) % self.k]
        
        return -1
        

    def isEmpty(self) -> bool:
        if self.deque[(self.right - 1) % self.k] == None and self.deque[self.left] == None:
            return True
        
        return False

    def isFull(self) -> bool:
        if self.deque[(self.right + 1) % self.k] != None and self.deque[(self.left - 1) % self.k] != None:
            return True
        
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()