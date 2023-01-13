class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        for i in range(len(strs[0])):
            offset = ord(strs[0][i])
            for j in range(len(strs)):
                if offset > ord(strs[j][i]):
                    count += 1
                    break
                    
                elif offset < ord(strs[j][i]):
                    offset = ord(strs[j][i])
                    
        return count