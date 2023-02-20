class Node():
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = Node()

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        
        for i in range(index):
            curr = curr.next
            
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        
        if self.head.next == None:
            self.head.next = Node(val)
            
        else:
            curr = self.head.next

            while curr.next:
                curr = curr.next

            curr.next = Node(val)
            
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        pre = self.head
        
        for i in range(index):
            pre = pre.next
            
        temp = pre.next
        pre.next = Node(val)
        pre.next.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        curr = self.head
        
        for i in range(index):
            curr = curr.next
            
        curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)