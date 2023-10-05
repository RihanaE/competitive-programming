class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        store = Counter(nums)
        
        res = -1
        
        for key, val in store.items():
            if key % 2 == 0:
                if res in store:
                    if store[res] < val:
                        res = key
                        
                    elif store[res] == val and key < res:
                        res = key
                        
                else:
                    res = key
                    
        return res