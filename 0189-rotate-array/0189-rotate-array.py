class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        output=nums[:]
        l=len(nums)
        i=0
        
        while i < l:
            nums[(i + k) % l] =output[i]
            i +=1
            
        
        