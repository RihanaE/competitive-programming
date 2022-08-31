class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store=[]
        count=0
        for i in range(len(nums)):
            j=0
            while j<len(nums):
                if nums[i]!=nums[j] and nums[j] < nums[i]:
                    count+=1
                j+=1

            store.append(count)
            count=0

        return store