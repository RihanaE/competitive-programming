class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        
        def helper(target, lst, idx):
            if target < 0:
                return 
            
            if target == 0:
                res.append(lst[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                    
                elif target - candidates[i] < 0:
                    return
                
                else:    
                    lst.append(candidates[i])
                    helper(target - candidates[i], lst, i + 1)
                    lst.pop()
                
                
        helper(target, [], 0)
        
        return res