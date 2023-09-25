class Solution:
    def longestPalindromeSubseq(self, s: str) -> int: 
        reverse = s[::-1]
        table = []
        
        for i in range(len(s) + 1):
            tempStore = [0] * (len(s) + 1)
            table.append(tempStore)
            
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):            
                if s[i] == reverse[j]:
                    table[i][j] = 1 + table[i + 1][j + 1]
                    
                else:
                    table[i][j] = max(table[i][j + 1], table[i + 1][j])
                    
        return table[0][0]