class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        diction = {}
        
        for ind, val in enumerate(list1):
            diction[val] = ind
            
        for idx, val in enumerate(list2):
            if val in diction :
                res.append([val, idx + diction[val]])
                
        res.sort(key = lambda k: k[1])
        
        ans = []
        
        for i in range(len(res)):
            if i == 0:
                ans.append(res[i][0])
                
            else:
                if res[i][1] == res[0][1]:
                    ans.append(res[i][0])
                    
        return ans