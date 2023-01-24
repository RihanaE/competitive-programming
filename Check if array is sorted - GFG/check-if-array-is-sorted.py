#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        left_pointer = 0
        right_pointer = 1
        
        while right_pointer < n:
            if arr[left_pointer] > arr[right_pointer]:
                return 0
                
            left_pointer += 1
            right_pointer += 1
            
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends