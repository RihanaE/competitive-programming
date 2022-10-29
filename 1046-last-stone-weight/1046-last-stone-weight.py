class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        
        while len(stones) > 1:
            if stones[1] == stones[0]:
                stones.pop(0)
                stones.pop(0)
                
            else:
                stones.append(stones[0] - stones[1])
                stones.pop(0)
                stones.pop(0)
                stones.sort(reverse=True)
                
        if len(stones)==0:
            return 0
                
        return stones[0]