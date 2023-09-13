class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = len(ratings)
        store = [[i, 1] for i in ratings]
        
        for i in range(1, len(ratings)):
            if (store[i][0] > store[i - 1][0]) and (store[i][1] <= store[i - 1][1]):
                res += max(store[i - 1][1] - store[i][1] + 1, 1)
                store[i][1] += max(store[i - 1][1] - store[i][1] + 1, 1)
                
            elif (store[i][0] < store[i - 1][0]) and (store[i][1] >= store[i - 1][1]):
                res += max(store[i][1] - store[i - 1][1] + 1, 1)
                store[i - 1][1] += max(store[i][1] - store[i - 1][1] + 1, 1)
                
    
       
        for i in range(len(ratings) - 1, 0, -1):
            
            
            if (store[i][0] > store[i - 1][0]) and (store[i][1] <= store[i - 1][1]):
            
                
                res += max(store[i - 1][1] - store[i][1] + 1, 1)
                store[i][1] += max(store[i - 1][1] - store[i][1] + 1, 1)
                
            elif (store[i][0] < store[i - 1][0]) and (store[i][1] >= store[i - 1][1]):
              
                
                res += max(store[i][1] - store[i - 1][1] + 1, 1)
                store[i - 1][1] += max(store[i][1] - store[i - 1][1] + 1, 1)
        return res