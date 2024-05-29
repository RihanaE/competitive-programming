class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if nums[0] % 2 == 0:
            parity = True
            
        else:
            parity = False
            
        for i in range(1, len(nums)):
            if parity == (nums[i] % 2 == 0):
                return False
            
            parity = nums[i] % 2 == 0
            
        return True