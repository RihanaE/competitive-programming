class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        numNeg = 0
        
        for i in nums:
            if i < 0:
                numNeg += 1
                
        amount = numNeg // 2
        pointer = 0
        res = 0
        for i in range(amount):
            if res == 0:
                res = nums[pointer] *nums[pointer + 1]
                
            else:
                res *= nums[pointer] *nums[pointer + 1]
                
            pointer += 2
            
        for i in range(numNeg, len(nums)):
            if nums[i] != 0:
                if res == 0:
                    res = nums[i]
                    
                else:
                    res *= nums[i]
                
                
        return res