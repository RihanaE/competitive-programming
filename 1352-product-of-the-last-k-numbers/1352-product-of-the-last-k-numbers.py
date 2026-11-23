class ProductOfNumbers:

    def __init__(self):
        self.arr = []


    def add(self, num: int) -> None:
        if self.arr == [] and num != 0:
            self.arr.append(num)

        elif num == 0:
            self.arr = []
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k: int) -> int:
        l = len(self.arr)
        if k > l:    
            return 0
        if -l <= -1 - k:
            return self.arr[-1] // self.arr[-1-k]

        return self.arr[-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)