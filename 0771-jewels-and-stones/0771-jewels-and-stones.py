class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map_ = defaultdict(int)
        for i in stones:
            map_[i] += 1
            
        res = 0
        
        for i in jewels:
            res += map_[i]
            
        return res