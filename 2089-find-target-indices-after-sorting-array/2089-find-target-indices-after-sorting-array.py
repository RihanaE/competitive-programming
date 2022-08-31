class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        store=[]
        for i in range (len(nums)):
            if nums[i]==target:
                store.append(i)
                
        return store