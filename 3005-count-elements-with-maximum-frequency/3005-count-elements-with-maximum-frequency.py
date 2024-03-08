class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = Counter(nums)
        val = max(arr.values())
        res = 0
        
        for key, value in arr.items():
            if value == val:
                res += val
                
        return res