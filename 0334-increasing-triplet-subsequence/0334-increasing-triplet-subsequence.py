class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        mn_left = []
        mx_right = []
        
        for i in range(len(nums)):
            if not mn_left:
                mn_left.append([i, nums[i]])
                
            else:
                mn_left.append([i, min(mn_left[-1][1], nums[i])])
                
        for i in range(len(nums) - 1, -1, -1):
            if not mx_right:
                mx_right.append([i, nums[i]])
                
            else:
                mx_right.append([i, max(mx_right[-1][1], nums[i])])
                
        mx_right.reverse()
        
        for i in range(1, len(mx_right)):
            num = nums[mx_right[i][0]]
            
            if mn_left[i][1] < num < mx_right[i][1]:
                return True
            
        return False