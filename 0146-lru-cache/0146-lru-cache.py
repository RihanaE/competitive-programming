class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d=collections.OrderedDict()
        
        
    def get(self, key: int) -> int:
        if key in self.d.keys():
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.d) <= self.capacity and key in self.d.keys():
            
            self.d.move_to_end(key)
            
        self.d[key]=value
            
       
            
        if len(self.d) > self.capacity:
            self.d.popitem(False)
            
            
            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)