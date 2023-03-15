class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = [0] * len(nums)
        for i, j in requests:
            res[i] += 1
            if j + 1 < len(res):
                res[j + 1] -= 1
                
        for i in range(1, len(res)):
            res[i] += res[i - 1]
            
        res.sort()
        nums.sort()
        out = 0
        
        for i in range(len(res) - 1, -1, -1):
            out += res[i] * nums[i]
            
        return out % ((10 ** 9) + 7)