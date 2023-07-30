class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        value = []
        for ind, val in enumerate(tasks):
            value.append([val[0], val[1], ind])
            
        value.sort()

        pointer = value[0][0]
        point = 0
        mn_heap = []
        res = []
      
            
        # for i in value:
        while point < len(value):
         
            if value[point][0] <= pointer:
                heappush(mn_heap, [value[point][1], value[point][2], value[point][0]])
                point += 1
            
            else:
                if mn_heap:
                    temp = heappop(mn_heap)
                    res.append(temp[1])

                    pointer += temp[0]
                    
                else:
                    pointer = value[point][0]
                
        
        while mn_heap:
            val = heappop(mn_heap)
            res.append(val[1])
            
        return res