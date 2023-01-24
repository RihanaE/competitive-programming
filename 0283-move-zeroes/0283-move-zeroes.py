class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
    Do not return anything, modify nums in-place instead.
    
    """
        
        if len(nums) == 1:
            return nums
        
        else:
            l = 0
            r = 1
            
            while r < len(nums):
                if l < r and nums[l] == 0 and nums[r] != 0:
                    nums[l], nums[r] = nums[r] , nums[l]
                    l += 1
                    r += 1
                    
                elif l < r and nums[l] != 0:
                    l += 1
                    
                else:
                    r += 1
                    
                    
                    
                    
#         if len(nums) == 1:
#             return nums
#         l = 0
#         r = 1

#         while r < len(nums) and l < len(nums):
#             if l <= r and nums[l] == 0 and nums[r] != 0:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 l += 1
#                 r += 1

#             elif l > r and nums[l] == 0 and nums[r] != 0:
#                 r +=1

#             if r < len(nums) and nums[r] == 0:
#                 r += 1

#             if l < len(nums) and nums[l] != 0:
#                 l += 1

