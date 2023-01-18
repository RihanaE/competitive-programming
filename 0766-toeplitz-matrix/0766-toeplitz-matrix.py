class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        temp = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j - i not in temp.keys():
                    temp[j - i] = matrix[i][j]
                    
                else:
                    if matrix[i][j] != temp[j - i]:
                        return False
        return True