class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        lst = len(mat) - 1
        
        for i in range(len(mat)):
            res += mat[i][i] + mat[0 + i][lst - i]
            
        if len(mat) % 2. != 0:
            res -= mat[lst // 2][lst // 2]
            
        return res