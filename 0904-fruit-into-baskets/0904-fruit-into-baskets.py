class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l , r= 0 ,0
        res=0
        d={}

        while r < len(fruits):
            d[fruits[r]]=r
            if len(d) == 3:
                val=min(d.values())
                del d[fruits[val]]
                l=val + 1

            res=max(res, r - l + 1)
            r +=1

        return res