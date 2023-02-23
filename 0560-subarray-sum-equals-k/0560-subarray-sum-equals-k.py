class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        res = 0
        for i in nums:
            pre.append(pre[-1] + i)
            
        store = {}
        
        for i in pre:
            if i - k in store:
                res += store[i - k]
                
            if i in store:
                store[i] += 1
                
            else:
                store[i] = 1
                
        return res