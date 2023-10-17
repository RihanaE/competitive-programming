class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        mx = max(nums)
        mn = min(nums)
        
        if (mx - k) <= (mn + k):
            return 0
        
        else:
            return (mx - k) - (mn + k)