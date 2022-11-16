class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        nb=[0] * len(security)
        na=[0] * len(security)
        res=[]
        
        for i in range (1,len(security)):
            if security[i - 1] >= security[i]:
                nb[i]=nb[i - 1] + 1
                
        for i in range(len(security) - 2, -1,-1):
            if security[i + 1] >= security[i]:
                na[i]=na[i + 1] + 1
                
        for i in range(len(security)):
            if nb[i] >= time and na[i] >= time:
                res.append(i)
                
        return res