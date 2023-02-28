class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = {}
        left_pointer = 0
        right_pointer = 0
        res = 0
        
        while right_pointer < len(s):
            
            if s[right_pointer] in store:
                store[s[right_pointer]] += 1
                
            else:
                store[s[right_pointer]] = 1
            
                
            if right_pointer - left_pointer + 1 - k <= max(store.values()):
                

                res = max(res, right_pointer - left_pointer + 1)
                right_pointer += 1
                
            else:
                store[s[left_pointer]] -= 1
                left_pointer += 1
                res = max(res, right_pointer - left_pointer + 1)
                right_pointer += 1
                
                
        return res