class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
        
        for ind, value in enumerate(nums):
            if value == target:
                output.append(ind)
        
        return output