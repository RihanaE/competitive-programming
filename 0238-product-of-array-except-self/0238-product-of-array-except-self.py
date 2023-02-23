class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        
        for i in range(1, len(nums)):
            out[i] = out[i - 1] * nums[i - 1]
    
        temp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            out[i] *= temp
            temp *= nums[i]
            
        return out
#         pre = [1]
#         post = [1]
        
#         for i in nums:
#             pre.append(pre[-1] * i)
            
#         for i in range(len(nums) - 1, -1.-1):
#             post.append(post[-1] * nums[i])
            
#         left = 0
#         right = len(nums) - 1
        
#         while left < right