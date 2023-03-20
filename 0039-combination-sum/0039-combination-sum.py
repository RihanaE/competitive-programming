class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(target, lst, idx):
            if target < 0:
                return
            if target == 0:
                res.append(lst[:])
                return
            
            for i in range(idx, len(candidates)):
                lst.append(candidates[i])
                helper(target - candidates[i], lst, i)
                lst.pop()
                
            
            
        helper(target,[],0)
        
        return res