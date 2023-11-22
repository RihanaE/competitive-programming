class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        store = defaultdict(list)
        for ind, val in enumerate(strs):
            store[tuple(sorted(val))].append(ind)
            
        for key, val in store.items():
            temp = []
            for ind in val:
                temp.append(strs[ind])
                
            res.append(temp[:])
            
        return res