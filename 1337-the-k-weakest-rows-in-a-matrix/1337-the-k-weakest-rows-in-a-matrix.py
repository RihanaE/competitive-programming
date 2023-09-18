class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        smList = []
        pointer = 0
        
        for i in mat:
            sm_ = sum(i)
            smList.append([sm_, pointer])
            pointer += 1
            
        smList.sort()
        
        res = []
        
        for i in range(k):
            res.append(smList[i][1])
            
        return res