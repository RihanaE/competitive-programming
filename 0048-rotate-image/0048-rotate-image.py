class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1
        
        while l < r:
            b = r
            t = l
            
            for i in range(r - l):
                temp = matrix[t][l + i]
                
                temp, matrix[t + i][r] = matrix[t + i][r], temp
                
                temp, matrix[b][r - i] = matrix[b][r - i], temp
                
                temp, matrix[b - i][l] = matrix[b - i][l], temp
                
                matrix[t][l + i] = temp
                
                
            l += 1
            r -= 1
            
            
        