class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        store = []
        memo = {}
        res = 0
        mn = float('inf')
        
        for i in range(len(scores)):
            store.append([ages[i], scores[i]])
            
            
        store.sort()
        
        for i in range(len(store)):
            val = store[i][1]
            for j in range(i - 1, -1, -1):
                if store[i][1] >= store[j][1] and store[i][0] != store[j][0]:
                    val = max(val, store[i][1] + memo[j])
                    
                elif store[i][0] == store[j][0]:
                    val = max(val, store[i][1] + memo[j])
                    
            memo[i] = val
            
        print(store)
        print(memo)
        return max(memo.values())