class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        candidate = []
        res = []
        
        for ind, val in enumerate(s):
            if val == c:
                candidate.append(ind)
                
        pointer = 0
        cPointer = 0
        
        while pointer < len(s):
            if pointer <= candidate[cPointer]:
                res.append(candidate[cPointer] - pointer)
                
            elif pointer > candidate[cPointer]:
                if cPointer + 1 < len(candidate) and (pointer - candidate[cPointer] > abs(candidate[cPointer + 1] - pointer)):
                    res.append(abs(candidate[cPointer + 1] - pointer))
                    cPointer += 1
                    
                else:
                    res.append(pointer - candidate[cPointer])
                    
            pointer += 1
            
        return res