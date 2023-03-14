class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = 0
        for i in range(len(trips)):
            mx = max(mx, trips[i][2])
            
        res = [0] * (mx + 1)
        
        for numpass, frm, to in trips:
            res[frm] += numpass
            
            if to < len(res):
                res[to] -= numpass
                
        for i in range(1, len(res)):
            res[i] += res[i - 1]
            if res[i - 1] > capacity or res[i] > capacity:
                return False
            
        return True