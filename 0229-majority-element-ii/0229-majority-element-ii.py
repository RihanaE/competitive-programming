class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        
        for i in counter:
            if len(nums) // 3 < counter[i]:
                res.append(i)
                
        return res