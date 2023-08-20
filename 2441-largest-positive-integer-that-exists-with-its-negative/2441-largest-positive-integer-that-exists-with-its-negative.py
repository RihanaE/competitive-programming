class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mx = -1
        dic = set()
        
        for i in nums:
            if -1 * i in dic and abs(i) > mx:
                mx = abs(i)
                
            dic.add(i)
            
        return mx