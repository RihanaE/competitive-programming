class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        
        for x, y in self.points:
            if (abs(x - point[0])) != (abs(y - point[1])) or x == point[0] or y == point[1]:
                continue
                
            ans += self.ptsCount[(x, point[1])] * self.ptsCount[(point[0], y)]
            
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)