class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=len(strs[0])
        len_array=len(strs)
        pointer=1
        if len(strs) == 1:
            return strs[0]
        
        else:
            s=""
            while pointer <= length:
                for i in range(1,len_array):
                    if strs[0][:pointer] != strs[i][:pointer]:
                        return s
                    
                s=strs[0][:pointer]        
                pointer +=1
                
            return s