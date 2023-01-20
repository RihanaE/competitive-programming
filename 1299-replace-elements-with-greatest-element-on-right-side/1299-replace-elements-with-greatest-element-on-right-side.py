class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            
            if arr[i] > num:
                arr[i], num = num, arr[i]
                
            else:
                arr[i] = num
                
        arr[-1] = -1
        
        return arr
                