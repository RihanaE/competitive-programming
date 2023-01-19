#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        self.selectionSort(arr,len(arr))
        
           
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            num = arr[i]
            key = i
            for j in range(i + 1, n):
                if num > arr[j]:
                    num = arr[j]
                    key = j
                    
            arr[i] ,arr[key] = arr[key], arr[i]
            
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends