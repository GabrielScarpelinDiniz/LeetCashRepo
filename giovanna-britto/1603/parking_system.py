class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.veiculo = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if (carType == 1):
            if self.veiculo[0] > 0:
                self.veiculo[0] -= 1
                return True
        elif (carType == 2):
            if self.veiculo[1] > 0:
                self.veiculo[1] -= 1
                return True
        elif (carType == 3):
            if self.veiculo[2] > 0:
                self.veiculo[2] -= 1
                return True
        
        return False