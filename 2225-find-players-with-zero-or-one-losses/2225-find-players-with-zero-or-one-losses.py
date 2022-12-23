class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ivalues={}
        jvalues={}
        
        for i, j in matches:
            if i in ivalues:
                ivalues[i] +=1
                
            else:
                ivalues[i] =1
                
            if j in jvalues:
                jvalues[j] +=1
                
            else:
                jvalues[j]= 1
                
        output=[[],[]]
        for i in ivalues:
            if i not in jvalues.keys():
                output[0].append(i)
                
        for i, j in jvalues.items():
            if j == 1:
                output[1].append(i)
        
        output[0].sort()
        output[1].sort()
                
        return output