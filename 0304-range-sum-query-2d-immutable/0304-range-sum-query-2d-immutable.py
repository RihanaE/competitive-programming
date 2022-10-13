class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c=len(matrix), len(matrix[0])

        self.s_matrix=[]

        for i in range(r + 1):
            self.s_matrix.append([0] * (c + 1))

        for i in range(r):
            pre=0
            for j in range(c):
                pre +=matrix[i][j]
                abv =self.s_matrix[i][j + 1]
                self.s_matrix[i + 1][j + 1]= pre + abv

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2=row1 + 1, row2 + 1, col1 + 1, col2 + 1

        BR=self.s_matrix[r2][c2]
        abv=self.s_matrix[r1 - 1][c2]
        l=self.s_matrix[r2][c1 - 1]
        TL=self.s_matrix[r1 - 1][c1 - 1]

        return BR - abv -l + TL


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)