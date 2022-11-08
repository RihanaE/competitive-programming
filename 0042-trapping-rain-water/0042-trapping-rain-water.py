class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        l , r=0 , len(height) - 1
        sl, sr=0, 0
        
        while l <= r:
            if sl < sr:
                if sl - height[l] > 0:
                    res +=sl - height[l]
                    
                sl=max(sl,height[l])
                l +=1
                
            elif sr <= sl:
                if sr - height[r] > 0:
                    res +=sr - height[r]
                    
                sr=max(sr, height[r])
                r -=1
                
        return res