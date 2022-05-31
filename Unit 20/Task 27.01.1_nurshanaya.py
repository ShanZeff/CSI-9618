# task 27.01: 1 OOP Class
# Copy the car class definition into your IDE and
# write a simple program to test that each method works

class Car:
    def __init__(self, n, e):   # constructor
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.0

    def SetPurchasePrice(self, p):
        self.__PurchasePrice = p

    def SetRegistration(self, r):
        self.__Registration = r

    def SetDateOfRegistration(self, d):
        self.__DateOfRegistration = d

    def GetVehicleID(self):
        return self.__VehicleID

    def GetRegistration(self):
        return self.__Registration

    def GetDateOfRegistration(self):
        return self.__DateOfRegistration

    def GetEngineSize(self):
        return self.__EngineSize

    def GetPurchasePrice(self):
        return self.__PurchasePrice


ThisCar = Car("ABC1234", 2500)
ThisCar.SetPurchasePrice(12000)
print(ThisCar.GetVehicleID())
