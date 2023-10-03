class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        collection = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                collection[nums[i][j]] += 1
                
        output = []
        
        for key, val in collection.items():
            if val == len(nums):
                output.append(key)
        
        output.sort()
        return output