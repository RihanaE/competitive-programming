class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        diction = {}
        count = 0
        
        for i in deliciousness:
            for j in range(22):
                if (2 ** j) - i in diction:
                    count += diction[(2 ** j) - i]
                    
                    
            if i not in diction:        
                diction[i] = 1
            else:
                diction[i] += 1
                
        return count % (10**9 + 7)