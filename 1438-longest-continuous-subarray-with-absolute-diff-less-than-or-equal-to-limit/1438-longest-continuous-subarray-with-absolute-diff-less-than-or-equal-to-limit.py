class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec = []
        inc = []
        l, r = 0, 0
        res = 1
        if len(nums) == 1:
            return res

        while r < len(nums):
            if inc == [] and dec == []:
                inc.append([nums[r], r])
                dec.append([nums[r], r])
                r +=1
                
            while inc and nums[r] < inc[-1][0]:
                inc.pop()
                
            inc.append([nums[r], r])
            
            while dec and nums[r] > dec[-1][0]:
                dec.pop()
                
            dec.append([nums[r] , r])
            
            
            if dec[0][0] - inc[0][0] > limit:
                l +=1
                while inc[0][1] < l:
                    inc.pop(0)
                    
                while dec[0][1] < l:
                    dec.pop(0)
                    
            else:
                res=max(res, r - l + 1)
                
            r +=1
            
        return res