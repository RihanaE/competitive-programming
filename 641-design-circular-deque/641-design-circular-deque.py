class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[None]*k
        self.head=self.tail=0
        self.k=k
        self.size=0
        

    def insertFront(self, value: int) -> bool:
        if self.size == 0:
            self.queue[self.head]=value
            self.size +=1
            return True
        
        elif self.size < self.k :
            self.head=(self.head - 1) % self.k
            self.queue[self.head]=value
            self.size +=1
            
            
            return True
      
        
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.size == 0:
            self.queue[self.tail]=value
            self.size +=1
            return True
        
        elif self.size < self. k:
            self.tail=(self.tail + 1) % self.k
            self.queue[self.tail]=value
            self.size +=1
            return True
        
        else:
            return False
        

    def deleteFront(self) -> bool:
        if self.size !=0:
            self.queue[self.head]=None
            if self.size != 1:
                self.head= (self.head + 1) % self.k
            self.size -=1
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if self.size !=0:
            self.queue[self.tail]=None
            if self.size != 1:
                self.tail=(self.tail - 1) % self.k
            self.size -=1
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if self.size !=0:
            return self.queue[self.head]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.size !=0:
            return self.queue[self.tail]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        
        


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