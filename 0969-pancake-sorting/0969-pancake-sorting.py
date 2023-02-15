class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n=len(arr)
        output=[]
        
        for i in range (n):
            mx=max(arr[:n - i])
            ind=arr.index(mx) + 1
            arr[:ind]=reversed(arr[:ind])
            output.append(ind)
            
            arr[:n - i]=reversed(arr[:n - i])
            output.append(n - i)
            
        return output
        
