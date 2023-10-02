class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        turn = False
        countA = 0
        countB = 0
        leftPointer = 0
        rightPointer = 0
        
        while rightPointer < len(colors):
            if colors[leftPointer] != colors[rightPointer]:
                if rightPointer - leftPointer >= 3:
                    if colors[leftPointer] == "A":
                        countA += rightPointer - leftPointer - 2
                        
                    else:
                        countB += rightPointer - leftPointer - 2
                        
                leftPointer = rightPointer
                
            else:
                rightPointer += 1
                
        if rightPointer - leftPointer >= 3:
            if colors[leftPointer] == "A":
                countA += rightPointer - leftPointer - 2
                        
            else:
                countB += rightPointer - leftPointer - 2
                
                
        return countA > countB