class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mn_, mx_ = logs[0]
        
        for i in range(1, len(logs)):
            if mn_ > logs[i][0]:
                mn_ = logs[i][0]
                
            if mx_ < logs[i][1]:
                mx_ = logs[i][1]
                
        prefixSm = [0 for i in range(mx_ - mn_ + 1)]
        
        for lw, hi in logs:
            prefixSm[lw - mn_] += 1
            prefixSm[hi - mn_] -= 1
            
        for i in range(1, len(prefixSm)):
            prefixSm[i] += prefixSm[i - 1]
            
        res = mn_
        
        for i in range(len(prefixSm)):
            if prefixSm[i] > prefixSm[res - mn_]:
                res = i + mn_
                
        return res
       
       