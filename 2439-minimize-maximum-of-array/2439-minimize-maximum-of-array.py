class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]
        pointer = 2
        
        for i in range(1, len(nums)):
            total += nums[i]
            
            if total % pointer == 0:
                candi = total // pointer
                
            else:
                candi = (total // pointer) + 1
                
            
            if candi > ans:
                ans = candi
                
                
            pointer += 1
                
        return ans