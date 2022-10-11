class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=sum(cardPoints[len(cardPoints) - k:])
        res=s
        l=0
        r=len(cardPoints) - k - 1

        while r < len(cardPoints):
            r +=1
            if r < len(cardPoints):
                s= s - cardPoints[r]
                s= s + cardPoints[l]
                l +=1
                res= max(res, s)

        return res