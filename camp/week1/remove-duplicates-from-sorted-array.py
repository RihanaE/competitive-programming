class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = list(set(nums))
        res.sort()
        for i in range(len(res)):
            nums[i] = res[i]
            
        return len(res)