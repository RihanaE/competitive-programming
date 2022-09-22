class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key= lambda i: int(i),reverse=True)
        return nums[k - 1]