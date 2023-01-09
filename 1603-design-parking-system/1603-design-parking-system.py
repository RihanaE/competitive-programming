class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.number_big = big
        self.number_medium = medium
        self.number_small = small
        

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.number_big != 0:
                self.number_big -= 1
                return True
            
            return False
        
        elif carType == 2:
            if self.number_medium != 0:
                self.number_medium -= 1
                return True
            
            return False
        
        elif carType == 3:
            if self.number_small != 0:
                self.number_small -= 1
                return True
            
            return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)