class Solution:
    def longestPrefix(self, s: str) -> str:
        prev, curr = 0, 1
        lps = [0] * len(s)
        
        while curr < len(s):
            if s[prev] == s[curr]:
                lps[curr] = prev + 1
                prev += 1
                curr += 1
                
            elif prev == 0:
                lps[curr] = 0
                curr += 1
                
            else:
                prev = lps[prev - 1]
                
#         mx_, idx = -1, 0
        

#         for val in lps:
#             if val > mx_:
               
#                 mx_ = val
              
        mx_ = 0
        mx_ = max(mx_, lps[-1])    
        
        if mx_ == 0:
            return ""
        
        else:
            return s[: mx_]