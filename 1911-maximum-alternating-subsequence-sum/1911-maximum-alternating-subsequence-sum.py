class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        
        def backtrack(idx, even):
            if idx == len(nums):
                return 0
            if (idx, even) in dp:
                return dp[(idx, even)]
            
            if even:
                curr = nums[idx]
                
            else:
                curr = -1 * nums[idx]
                
            dp[(idx, even)] = max(curr + backtrack(idx + 1, not even), backtrack(idx + 1, even))
            
            return dp[(idx, even)]
        
        return backtrack(0, True)