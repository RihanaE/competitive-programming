class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid=[]
        minmum={"min" : [float('inf'),-1]}
        for index, i in enumerate(points):
            if i[0] == x or i[1] == y:
                if minmum["min"][0] > (abs(x - i[0]) + abs(y - i[1])):
                    minmum["min"] = [(abs(x - i[0]) + abs(y - i[1])) ,index]
                    
                
        return minmum["min"][1]