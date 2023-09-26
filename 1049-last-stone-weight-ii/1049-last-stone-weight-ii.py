class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sm_ = sum(stones)
        if sm_ % 2 != 0:
            point = (sm_ // 2) + 1
            
        else:
            point = sm_ // 2
            
        dp = {}
        
        print(sm_, point)
        def backtrack(i, total):
            if total >= point or i == len(stones):
                return abs(total - (sm_ - total))
            
            elif (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(backtrack(i + 1, total + stones[i]), backtrack(i + 1, total))
            return dp[(i, total)]
        
        
        return backtrack(0, 0)