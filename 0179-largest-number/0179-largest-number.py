class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, val in enumerate(nums):
            nums[i] = str(val)
            
        nums.sort(key = cmp_to_key(self.compare))
            
        
        return str(int("".join(nums)))
    
    def compare(self, n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1