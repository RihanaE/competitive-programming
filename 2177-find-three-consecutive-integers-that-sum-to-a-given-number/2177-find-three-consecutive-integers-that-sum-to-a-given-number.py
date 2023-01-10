class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        temp=num - 3
        
        if temp % 3 != 0:
            return []
        
        else:
            result = temp // 3
            
            return [result, result + 1, result + 2]