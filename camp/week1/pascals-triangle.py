class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(2, numRows + 1):
            temp = [1] * i
            
            for j in range(1, i - 1):
             
                temp[j] = res[-1][j - 1] + res[-1][j]
                
            res.append(temp)
            
        return res