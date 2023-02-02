class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left_p = 0
        right_p = len(nums) - 1
        res = 0
        
        while left_p < right_p:
            
            if nums[left_p] + nums[right_p] == k:
                
                res += 1
                right_p -= 1
                left_p += 1
                
            elif nums[left_p] + nums[right_p] < k:
                left_p += 1
                
            elif nums[left_p] + nums[right_p] > k:
                right_p -= 1
                
        return res