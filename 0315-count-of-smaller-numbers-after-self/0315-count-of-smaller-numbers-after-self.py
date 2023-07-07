from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_arr = SortedList([])
        result = []
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            index = sorted_arr.bisect_left(num)
            result.append(index)
            sorted_arr.add(num)
            
            
        return result[::-1]