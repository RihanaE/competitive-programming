class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if len(tokens) == 0 or power < tokens[0]:
            return 0
        
        score=0
        res=0
        l, r=0 , len(tokens) - 1
        
        while l <= r:
            if tokens[l] <= power:
                score +=1
                power -=tokens[l]
                l +=1
                
            elif score > 0:
                res=max(score,res)
                power +=tokens[r]
                score -=1
                r -=1
                
        res=max(score,res)
        
        return res