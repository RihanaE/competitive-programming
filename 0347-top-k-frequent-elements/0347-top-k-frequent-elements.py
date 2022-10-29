class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        store=[]
        res=[]
        
        for key,val in d.items():
            store.append([key,val])
            
        store.sort(key=lambda k:k[1])
        
        for i in range(k):
            res.append(store[::-1][i][0])
            
        return res