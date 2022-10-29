class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        for i in range(k):
            if i == k - 1:
                return nums[::-1][i]
            