class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = [0]
        for i in self.nums:
            res.append(res[-1] + i)
            
            
        return res[right + 1] - res[left]
#         res = [0] * (len(self.nums) + 1)
        
#         for i in range(len(self.nums)):
#             res[i + 1] = res[i] + self.nums[i]
            
         
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)