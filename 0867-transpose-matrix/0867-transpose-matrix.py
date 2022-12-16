class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(len(matrix[0])):
            result.append([0] * len(matrix))
        l = 0
        c = 0

        for i in range(len(result)):
            for j in range(len(result[0])):
                result[i][j] = matrix[l][c]
                l += 1
                if l == len(matrix):
                    l = 0
                    c += 1

        return result