class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        mx=k % s
        i = 0
        l=len(chalk)
        
        while i < l:
            if mx - chalk[i] >= 0:
                mx -=chalk[i]
            else:
                return i
            
            i+=1

           