class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.nums = nums
        self.k = k
        
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
            
        elif self.nums[0] < val:
            heappop(self.nums)
            heappush(self.nums, val)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)