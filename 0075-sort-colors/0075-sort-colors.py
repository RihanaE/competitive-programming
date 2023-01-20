class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j - 1] > nums[j]:
                    nums[j - 1],  nums[j] = nums[j], nums[j - 1]
                    flag = True
                    
            if flag == False:
                break