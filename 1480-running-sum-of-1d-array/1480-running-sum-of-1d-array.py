class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        output = []
        
        for i in nums:
            res += i
            output.append(res)
            
        return output