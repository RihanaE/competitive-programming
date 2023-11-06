class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        pointer = 0
        currNum = 1
        
        while pointer < len(arr):
            if arr[pointer] == currNum:
                pointer += 1
                currNum += 1
                
            else:
                k -= 1
                if k == 0:
                    return currNum
                
                currNum += 1
                
        if k > 0:
            while k > 0:
                k -= 1
                if k == 0:
                    return currNum
                
                currNum += 1
                
        return currNum
            
            