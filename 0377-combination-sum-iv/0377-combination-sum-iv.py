class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        diction = defaultdict(int)
        diction[0] = 1
        
        for tot in range(1, target + 1):
            diction[tot] = 0
            
            for n in nums:
                diction[tot] += diction[tot - n]
                
        return diction[target]