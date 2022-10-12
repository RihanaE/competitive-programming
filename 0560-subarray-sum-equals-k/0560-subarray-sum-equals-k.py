class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = [0]
        res = 0
        d={0:1}

        for i in nums:
            store.append(store[-1] + i)

        l= 1

        while l < len(store):
            if store[l] - k in d:
                res =res + d[store[l] - k]
                
                
                
                    
            if store[l] in d.keys():
                    d[store[l]] +=1
                    
            else:
                d[store[l]] =1
                
            l +=1
            
        return res