class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = None
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if res == None:
                    res = nums[i]
                    
                else:
                    res = res ^ nums[i]
                    
        if res == None:
            return 0
        
        return res