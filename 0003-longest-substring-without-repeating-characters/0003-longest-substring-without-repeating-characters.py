class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        right = 0
        res = 0
        
        while right < len(s):
            if s[right] in store:
                store.remove(s[left])
                left += 1
                
            else:
                store.add(s[right])
                res = max(res, right - left + 1)
                right += 1
                
        return res