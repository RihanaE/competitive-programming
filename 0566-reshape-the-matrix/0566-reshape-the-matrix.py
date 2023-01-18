class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        length = len(mat)
        length_row = len(mat[0])
        
        if r * c < length * length_row or r * c > length * length_row:
            return mat
        else:
            output = [[0] * c for row in range(r)]
            pointer_l = 0
            pointer_r = 0
            
            for i in range(length):
                for j in range(length_row):
                    output[pointer_l][pointer_r] = mat[i][j]
                    pointer_r +=1
                    
                    if pointer_r == c:
                        pointer_l += 1
                        pointer_r = 0
                        
            return output