class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if tokens and tokens[0] > power:
            return 0
        
        elif not tokens or power == 0:
            return 0
        
        res=0
        l, r=0, len(tokens)
        output=0
        
        while l < r:
            if power >= tokens[l]:
                res +=1
                power -=tokens[l]
                l +=1
                
            else:
                r -=1
                output=max(output,res)
                res -=1
                power +=tokens[r]
                
        output=max(output,res)
        
        return output