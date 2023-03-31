class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        
        def helper(a, b):
            if b == 0:
                return a
            else:
                return helper(b, a % b)
            
            
        return helper(mx, mn)