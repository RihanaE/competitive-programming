class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        store = {}
        res = 0
        
        while right_pointer < len(fruits):
            if fruits[right_pointer] in store:
                store[fruits[right_pointer]] += 1
                
            else:
                store[fruits[right_pointer]] = 1
                
            if len(store) <= 2:
                res = max(res, right_pointer - left_pointer + 1)
                
            else:
                while len(store) > 2:
                    store[fruits[left_pointer]] -= 1
                    
                    if store[fruits[left_pointer]] == 0:
                        store.pop(fruits[left_pointer])
                        
                    left_pointer += 1
                    
            right_pointer += 1
            
            
        return res