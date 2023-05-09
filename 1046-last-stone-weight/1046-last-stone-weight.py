class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
            
        heapify(stones)
        
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            
            if x != y:
                heappush(stones, -1 * ((y * -1) - (x * -1)))
                
        if stones:
            return stones[0] * -1
        
        return 0