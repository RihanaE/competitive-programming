class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r=0 , len(height) - 1
        
        output=0
        
        while l < r:
            a= (r - l) * min(height[l] , height[r])
            output=max(output,a)
            
            if height[l] > height[r]:
                r -=1
                
            else:
                l +=1
                
        return output
        