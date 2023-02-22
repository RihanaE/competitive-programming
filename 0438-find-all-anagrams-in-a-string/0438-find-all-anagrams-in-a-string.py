class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p) - 1
        pdict = Counter(p)
        temp = {}
        left = 0
        res = []
    
        for right in range(len(s)):
            if s[right] in temp:
                temp[s[right]] += 1
                
            else:
                temp[s[right]] = 1
                
            if right - left == length:
                if temp == pdict:
                    res.append(left)
                    
                temp[s[left]] -= 1
                if temp[s[left]] == 0:
                    del(temp[s[left]])
                    
                left += 1
                
        return res