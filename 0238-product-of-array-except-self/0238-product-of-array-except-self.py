class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]
        l, p ,r= 0, 1, len(nums) - 1
        
        while l < len(nums) - 1:
            output.append(output[-1] * nums[l])
            l +=1
            
        while r >= 0:
            output[r]= output[r] * p
            p= p * nums[r]
            r -=1
            
        return output