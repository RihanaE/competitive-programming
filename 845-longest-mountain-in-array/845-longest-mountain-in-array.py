class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        output=0
        
        for ind in range(1 , len(arr) - 1):
            if arr[ind - 1] < arr[ind] > arr[ind + 1]:
                l = r = ind
                
                while l > 0 and arr[l - 1] < arr[l]:
                    l -=1
                    
                while r < len(arr) - 1 and arr[r + 1] < arr[r]:
                    r +=1
                    
                output=max(output, (r - l + 1))
                
        return output