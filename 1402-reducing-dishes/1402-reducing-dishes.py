class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        prefixsum = 0
        res = 0
        
        for i in satisfaction:
            prefixsum += i
            
            if prefixsum >= 0:
                res += prefixsum
                
                
        return res