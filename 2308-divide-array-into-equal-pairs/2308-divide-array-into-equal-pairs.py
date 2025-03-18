class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        amount = Counter(nums)
        
        for key, val_ in amount.items():
            if val_ % 2 != 0:
                return False

        return True