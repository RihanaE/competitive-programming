class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        temp = nums[0]
        count = 0
        visited = set()
        
        for i in range(1, len(nums)):
            temp = temp | nums[i] 
            
    
        
        def helper(num, pointer):
            nonlocal count
            if num == temp:
                count +=1
                
            for i in range(pointer, len(nums)):
                helper(num | nums[i], i + 1)
        
        
        helper(0 , 0)
        return count