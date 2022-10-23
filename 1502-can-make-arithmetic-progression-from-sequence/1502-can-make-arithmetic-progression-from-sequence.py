class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        diff=arr[1] - arr[0]
        l=1
        
        while l < len(arr):
            if arr[l - 1] + diff != arr[l]:
                return False
            
            l +=1
        else:
            return True