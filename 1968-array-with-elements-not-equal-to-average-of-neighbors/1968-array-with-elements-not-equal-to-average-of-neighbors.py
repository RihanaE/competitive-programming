class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        store=[]
        left=0
        right=len(nums)-1
        
        while len(store) != len(nums):
            store.append(nums[left])
            left+=1
            if left <= right:
                store.append(nums[right])
                right-=1

        return store

