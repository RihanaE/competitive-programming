class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        res = 0
        s = []

        while r <= len(chars):
            if s == []:
                s.append(chars[r])
                r += 1
                res += 1

            elif r < len(chars) and chars[l] == chars[r]:
                res += 1
                l += 1
                r += 1

            else:
                if 1 < res < 10:
                    s.append(str(res))
                    
                elif res >= 10:
                    temp=str(res)
                    for i in temp:
                        s.append(i)
                        
                res = 0
                if r < len(chars):
                    s.append(chars[r])
                res +=1
                l += 1
                r += 1

        for i in range(len(s)):
            chars[i]=s[i]
        
        
        return len(s)