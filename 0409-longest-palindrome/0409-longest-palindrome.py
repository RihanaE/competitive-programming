class Solution:
    def longestPalindrome(self, s: str) -> int:
        mx = 0
        count = Counter(s)
        res = 0
    
        for key, val in count.items():
            if val % 2 == 0:
                res += val
                
            else:
                if mx < val:
                    if mx != 0:
                        res += mx - 1
                    mx = val
                    
                else:
                    res += val - 1
                
                
        res += mx
        return res