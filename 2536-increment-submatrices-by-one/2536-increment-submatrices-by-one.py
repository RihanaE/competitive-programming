class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        p_sum = [[ 0 for i in range(n) ] for j in range(n) ]

        for query in queries:
            start_row = query[0]
            end_row = query[2]
            start_col = query[1]
            end_col = query[3]

            for row in range(start_row, end_row+1):
                p_sum[row][start_col]+=1
                if(end_col < n-1 ):
                    p_sum[row][end_col+1]-=1 

        for row in range(n):
            for col in range(1,n):
                p_sum[row][col]+=p_sum[row][col-1]


        return p_sum