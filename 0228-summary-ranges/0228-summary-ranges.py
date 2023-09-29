class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        elif len(nums) == 1:
            return [f"{nums[0]}"]
        
        leftPointer = 0
        rightPointer = 1
        res = []
        
        while rightPointer < len(nums):
            if nums[rightPointer - 1] + 1 == nums[rightPointer]:
                rightPointer += 1
                
            elif nums[rightPointer - 1] == nums[rightPointer]:
                rightPointer += 1
                
            else:
                if nums[leftPointer] != nums[rightPointer - 1]:
                    res.append(f"{nums[leftPointer]}->{nums[rightPointer - 1]}")
                    
                else:
                    res.append(f"{nums[leftPointer]}")
                    
                leftPointer = rightPointer
                rightPointer += 1
                
        if nums[leftPointer] != nums[rightPointer - 1]:
            res.append(f"{nums[leftPointer]}->{nums[rightPointer - 1]}")
                    
        else:
            res.append(f"{nums[leftPointer]}")
                
        return res