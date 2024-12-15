class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        ans = 0
        
        for num, val in frequency.items():
            if num + 1 in frequency:
                ans = max(ans, val + frequency[num + 1])
                
        return ans