class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def helper(nums, pointer, lst):
            nonlocal res
            
            if pointer >= len(nums):
                res.append(lst[:])
                
                return
            
            helper(nums, pointer + 1, lst + [nums[pointer]])
            helper(nums, pointer + 1, lst)
            
        helper(nums, 0, [])
        return res