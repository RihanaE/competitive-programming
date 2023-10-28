class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        diction = defaultdict(str)

        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] not in diction and s[i] not in diction.values():
                diction[pattern[i]] = s[i]
                
            else:
                if diction[pattern[i]] != s[i] or (pattern[i] not in diction and s[i] in diction.values()):
                    return False
                
        return True