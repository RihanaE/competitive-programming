class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)
        value=0

        while i < j:
            value+=piles[j-2]
            j -=2
            i+=1

        return value