class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left = 1
        right = 10 ** 6
        res = 0
        
        while right >= left:
            mid = (left + right) // 2
            
            if self.helper(nums, mid) > threshold:
                left = mid + 1
                
            else:
                right = mid - 1
                res = mid
                
                
        return res
                
                
    def helper(self, nums, mid):
        res = 0
        
        for i in nums:
            res += math.ceil(i / mid)
            
        return res