class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l , r, output, sum=0 , 0 , 0 ,0
        
        while r < len(nums) :
            sum +=nums[r]
            while nums[r] * (r - l +1) > sum + k:
                sum -=nums[l]
                l +=1

            output=max(output, r - l + 1)
            r +=1

        return output
        