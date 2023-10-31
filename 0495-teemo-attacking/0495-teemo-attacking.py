class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        
        for _ in range(len(timeSeries)):
            if _ < len(timeSeries) - 1 and timeSeries[_] + duration >= timeSeries[_ + 1]:
                total += timeSeries[_ + 1] - timeSeries[_]
                
            else:
                total += duration
                
        return total