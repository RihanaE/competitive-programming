class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        less = []
        equal = []
        
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
                
            else:
                equal.append(i)
                
        return less + equal + greater