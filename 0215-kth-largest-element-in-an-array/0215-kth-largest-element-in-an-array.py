class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
            
        heapify(nums)
        
        for i in range(k):
            res = heappop(nums)
            
        return -1 * res