class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(length):
            nums.append(int(str(nums[i])[::-1]))
            
        return len(set(nums))