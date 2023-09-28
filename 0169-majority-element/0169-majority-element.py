class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = Counter(nums)
        
        for num, amount in store.items():
            if amount > len(nums) // 2:
                return num