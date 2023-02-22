class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1) - 1
        pdict = Counter(s1)
        temp = {}
        left = 0
    
        for right in range(len(s2)):
            if s2[right] in temp:
                temp[s2[right]] += 1
                
            else:
                temp[s2[right]] = 1
                
            if right - left == length:
                if temp == pdict:
                    return True
                    
                temp[s2[left]] -= 1
                if temp[s2[left]] == 0:
                    del(temp[s2[left]])
                    
                left += 1
                
        return False