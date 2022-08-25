class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        
        
        else:
            
            store=0
            count=1
            difference=nums[1]-nums[0]
            elements=2
        
            for i in range (2,len(nums)):
                
                if difference == nums[i] - nums[i-1]:
                    
                    elements=elements+1
                    
                    if elements >= 3:
                        store+=count
                        count+=1

                else:
                    difference=nums[i]-nums[i-1]
                    count=1
                    elements=2

        
        return store
        