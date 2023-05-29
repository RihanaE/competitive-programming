class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(list)
        
        def backtrack(pointer, sm):
            if pointer == len(nums):
                if sm == target:
                    return 1
                
                return 0
            
            elif (pointer, sm) in memo:
                return memo[(pointer, sm)]
            
            else:
                memo[(pointer, sm)] = backtrack(pointer + 1, sm + nums[pointer]) + backtrack(pointer + 1, sm - nums[pointer])
                return memo[(pointer, sm)]
            
        return backtrack(0, 0)