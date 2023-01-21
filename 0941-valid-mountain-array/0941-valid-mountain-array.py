class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        else:
            if arr[0] < arr[1]:
                increase = True
                decrease = False
                
            else:
                return False
            
            for i in range(1, len(arr)):
                if arr[i - 1] == arr[i]:
                    return False
                
                elif arr[i - 1] > arr[i]:
                    increase = False
                    decrease = True
                    
                elif decrease == True and arr[i - 1] < arr[i]:
                    return False
                
            if increase == True:
                return False
        return True