class Solution:
    def numTeams(self, rating: List[int]) -> int:
        leftArray = [0] * len(rating)
        rightArray = [0] * len(rating)
        
        
        rightPointer = 1
        
        while rightPointer < len(rating):
            count = 0
            for leftPointer in range(rightPointer):
                if rating[leftPointer] < rating[rightPointer]:
                    count += 1
                    
            leftArray[rightPointer] = count
            rightPointer += 1
            
        leftPointer = len(rating) - 2
        
        while leftPointer >= 0:
            count = 0
            
            for rightPointer in range(len(rating) - 1, leftPointer, -1):
                if rating[leftPointer] > rating[rightPointer]:
                    count += 1
                    
            rightArray[leftPointer] = count
            leftPointer -= 1
            
        res = 0
        
        rightPointer = 1
        
        while rightPointer < len(rating):
            for leftPointer in range(rightPointer):
                if rating[leftPointer] < rating[rightPointer]:
                    res += leftArray[leftPointer]
                    
            rightPointer += 1
            
        leftPointer = len(rating) - 2
        
        while leftPointer >= 0:
            for rightPointer in range(len(rating) - 1, leftPointer, -1):
                if rating[leftPointer] > rating[rightPointer]:
                    res += rightArray[rightPointer]
                    
            leftPointer -= 1
            
        return res