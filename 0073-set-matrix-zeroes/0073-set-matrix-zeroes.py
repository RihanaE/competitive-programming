class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack_row = []
        stack_col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    stack_row.append(i)
                    stack_col.append(j)
        
        for i in range(len(stack_row)):
            matrix = self.helper(matrix, stack_row[i], stack_col[i])
            
            
        return matrix
        
    def helper(self,matrix,row,col):
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
            
        for j in range(len(matrix)):
            matrix[j][col] = 0
            
        return matrix