class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array=[i + 1 for i in range(n)]
        i = 0
        
        while len(array) > 1:
            i = (i + k - 1) % len(array)
            array.remove(array[i])
            
        return array[0]