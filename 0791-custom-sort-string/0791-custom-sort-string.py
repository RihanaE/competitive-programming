class Solution:
    def customSortString(self, order: str, s: str) -> str:
        store = Counter(s)
        pointer = 0
        ans = []
        
        while pointer < len(order):
            if store[order[pointer]] != 0:
                ans.append(order[pointer])
                store[order[pointer]] -= 1
                
            else:
                pointer += 1
                
            
        for val, key in store.items():
            if key != 0:
                temp = val * key
                ans.append(temp)
                
        return "".join(ans)