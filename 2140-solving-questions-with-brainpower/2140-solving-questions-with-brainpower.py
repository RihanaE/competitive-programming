class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l=len(questions)
        store=[0] * (l + 1)
        
        for i in range(l - 1,-1,-1):
            store[i]=store[i + 1]
            
            r= questions[i][1] + i + 1
            
            if r < l:
                store[i]=max(store[i + 1], questions[i][0] + store[r])
                
            else:
                store[i]=max(store[i + 1], questions[i][0])
                
        return store[0]