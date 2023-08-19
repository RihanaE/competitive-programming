class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visit = set()
        
        for i in nums:
            if i != 0:
                visit.add(i)
                
        return len(visit)