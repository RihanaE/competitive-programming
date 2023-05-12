class MedianFinder:

    def __init__(self):
        self.heap_mn = []
        self.heap_mx = []

    def addNum(self, num: int) -> None:
        if not self.heap_mx:
            heappush(self.heap_mx, -1 * num)
            
        elif -self.heap_mx[0] > num:
            heappush(self.heap_mx, -1 * num)
            
            if len(self.heap_mx) > len(self.heap_mn) + 1:
                value = -1 * heappop(self.heap_mx)
                heappush(self.heap_mn, value)
                
        
            
        else:
            heappush(self.heap_mn,  num)
            
            if len(self.heap_mn) > len(self.heap_mx):
                value = heappop(self.heap_mn)
                heappush(self.heap_mx, -value)
                
                
        
        

    def findMedian(self) -> float:
        if len(self.heap_mn) == len(self.heap_mx):
            return (self.heap_mn[0] - self.heap_mx[0]) / 2
        
        return -self.heap_mx[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()