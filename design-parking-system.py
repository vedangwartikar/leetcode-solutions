class ParkingSystem:
​
    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]
​
    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.parking[0] > 0:
            self.parking[0] -= 1
            return True
        if carType == 2 and self.parking[1] > 0:
            self.parking[1] -= 1
            return True
        if carType == 3 and self.parking[2] > 0:
            self.parking[2] -= 1
            return True
            
​
​
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
