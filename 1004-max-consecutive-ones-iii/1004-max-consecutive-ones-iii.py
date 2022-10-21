class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        count, res=0 , 0
        while r < len(nums):
            if nums[r] == 1:
                count +=1
                r +=1
                
            elif k > 0 and nums[r] == 0:
                k -=1
                count +=1
                r +=1
            elif k <= 0:
                res=max(count, res)
                if nums[l] == 0:
                    k +=1
                    l +=1
                    
                else:
                    l +=1
                    
                count -=1
                
        res=max(count, res)
        return res