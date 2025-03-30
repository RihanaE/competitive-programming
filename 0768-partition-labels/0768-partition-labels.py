class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        res = []
        
        for ind, val in enumerate(s):
            store[val] = ind
            
        left_pointer = 0
        right_pointer = store[s[0]]
        start = 0
        
        while right_pointer < len(s) and left_pointer < len(s):
            if store[s[left_pointer]] <= right_pointer and left_pointer == right_pointer:
                res.append(right_pointer - start + 1)
                if left_pointer < len(s) - 1:
                    right_pointer = store[s[left_pointer + 1]]
                    start = left_pointer + 1
                    
                left_pointer += 1
                
             
            
            elif store[s[left_pointer]] <= right_pointer and left_pointer < right_pointer:
                left_pointer += 1
                
            else:
                right_pointer = store[s[left_pointer]]
                left_pointer += 1
                
                
        return res