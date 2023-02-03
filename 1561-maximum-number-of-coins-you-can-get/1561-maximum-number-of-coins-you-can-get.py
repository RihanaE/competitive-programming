class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        left_pointer = 0
        right_pointer = len(piles) - 2
        
        while left_pointer < right_pointer:
            total += piles[right_pointer]
            right_pointer -= 2
            left_pointer += 1
            
        return total