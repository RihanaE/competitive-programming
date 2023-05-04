#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    
    def heapify(self,arr, n, i):
        # code here
        
        self.heapify_up(arr, n, i)
        self.heapify_down(arr, n, i)
       
    def heapify_up(self, arr, n, i):
        while i > 0 and arr[(i - 1) // 2] > arr[i]:
            arr[(i - 1) // 2], arr[i] = arr[i], arr[(i - 1) // 2]
            i = (i - 1) // 2
            
    def heapify_down(self, arr, n, i):
        while (2 * i) + 2 < n and (arr[i] > arr[((2 * i) + 1)] or arr[i] > arr[((2 * i) + 2)]):
            if arr[((2 * i) + 2)] > arr[((2 * i) + 1)]:
                arr[((2 * i) + 1)], arr[i] = arr[i], arr[((2 * i) + 1)]
                i = (2 * i) + 1
                
            else:
                arr[((2 * i) + 2)], arr[i] = arr[i], arr[((2 * i) + 2)]
                i = (2 * i) + 2
            
        while (2 * i) + 1 < n and arr[(2 * i) + 1] < arr[i]: 
            arr[i], arr[(2 * i) + 1] = arr[(2 * i) + 1], arr[i]
            i = (2 * i) + 1
                
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n - 1, -1, -1):
            heapify(arr, n, i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        arr.sort()

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends