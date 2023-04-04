class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        store = set()
        val = nums[left]
        count = 0
        
        while left < len(nums):
            right = left
            while right < len(nums):
                
                if val > nums[right]:
                    val = self.helper(val, nums[right])
                    
                    
                else:
                    val = self.helper(nums[right], val)
                    
                right += 1
                if val == k:
                    count += 1
                
            left += 1
            
            if left < len(nums):
                val = nums[left]
            
        return count
        
    def helper(self, a, b):
        if b == 0:
            # print(a)
            return a
        
        else:
            return self.helper(b, a % b)