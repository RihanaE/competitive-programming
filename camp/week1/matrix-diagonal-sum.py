class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sm = 0
        
        for i in range(len(mat)):
            sm += mat[i][i]
            
        l, r = 0, len(mat) - 1
        
        for i in range(len(mat)):
            sm += mat[i + l][r - i]
            
        if len(mat) % 2 != 0:
            sm -= mat[(len(mat) - 1) // 2][(len(mat) - 1) // 2]
            
        return sm