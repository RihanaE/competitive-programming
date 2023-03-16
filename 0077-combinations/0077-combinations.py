class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def helper(temp , lst = []):
            if len(lst) == k:
                res.append(lst[:])
                return
            
            if temp > n:
                return
            
            lst.append(temp)
            helper(temp + 1, lst)
            lst.pop()
            
            helper(temp + 1, lst)
            
            
        helper(1)
        return res