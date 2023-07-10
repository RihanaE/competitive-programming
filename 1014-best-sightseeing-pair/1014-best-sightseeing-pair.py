class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n =  len(values)
        track = [-1]
        for i in range(n):
            track.append(-1) 
            
        track[-1] = values[-1]
        res = values[-1]-1
        i = n-2
        
        while i >= 0:
            track[i] = max(track[i+1],res+values[i])
            res = max(values[i], res)-1
            i-=1
        return track[0]