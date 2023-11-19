class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.res = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src, time = self.checkInMap[id]
        route = (src, stationName)
        
        if route not in self.res:
            self.res[route] = [0, 0]
            
        self.res[route][0] += t - time
        self.res[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.res[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)