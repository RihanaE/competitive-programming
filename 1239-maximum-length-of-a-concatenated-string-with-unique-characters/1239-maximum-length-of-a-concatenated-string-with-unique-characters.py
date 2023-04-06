class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        
    
        def helper(word, pointer):
            nonlocal res
            
            if len(set(word)) != len(word):
                return 
            
            if pointer >= len(arr):
                res = max(res, len(word))
                return
            
            res = max(res, len(word))
            
            helper(word + arr[pointer], pointer + 1)
            helper(word, pointer + 1)
            
        helper("", 0)
        return res