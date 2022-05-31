# Task 26.02 Record and Random-access file
# 1. Write a complete program to save several car records to a random-access file.
# Write another program to find a record in the random-access file using the record key.
# Display the record data on screen.

import pickle   # this library is required to create binary files
from datetime import date
RECORDSIZE = 50     # 20 + 10 + 8 + 4 + 8
class CarRecord:
    def __init__(self):
        VehicleID = "dummy"
        VehicleID = VehicleID.ljust(20)
        self.VehicleID = VehicleID.encode("utf-8")
        Registration = " "
        Registration = Registration.ljust(10)
        self.Registration = Registration.encode("utf-8")
        self.DateOfRegistration = date(1990, 1, 1)
        self.EngineSize = 0
        self.PurchasePrice = 0.0


def InitialiseFile():
    CarFile = open("CarFile.DAT", "wb")     # file for car records
    for i in range(100):    # loop for each array element
        Address = i * RECORDSIZE + 1
        CarFile.seek(Address, 0)
        # write a whole record to the binary file
        pickle.dump(CarRecord(), CarFile)
    CarFile.close()     # close file


def InputNewRecordData():
    ThisCar = CarRecord()
    VehicleID = input("Vehicle ID: ")
    VehicleID = VehicleID.ljust(20)
    ThisCar.VehicleID = VehicleID.encode("utf-8")
    Registration = input("Registration: ")
    Registration = Registration.ljust(10)
    ThisCar.Registration = Registration.encode("utf-8")
    ThisCar.DateOfRegistration = (input("Registration Date: "))
    ThisCar.EngineSize = int(input("Engine size: "))
    ThisCar.PurchasePrice = float(input("Purchase price: "))
    return ThisCar


def Hash(reg):
    result = ord(reg[0]) * RECORDSIZE + 1
    print("Hashed to", result)
    return result


def SaveToFile(ThisCar, CarFile):
    Address = Hash(ThisCar.Registration.decode("utf-8"))
    CarFile.seek(Address, 0)
    pickle.dump(ThisCar, CarFile)   # write a whole record to the binary file


def OpenFileForUpdate():
    CarFile = open("CarFile.DAT", "rb+")    # open file for update
    return CarFile


def FindRecord(reg, CarFile):
    Address = Hash(reg)
    CarFile.seek(Address, 0)
    ThisCar = pickle.load(CarFile)      # load record from file
    return ThisCar


def OutputData(ThisCar):
    print(ThisCar.VehicleID)    # write one field


def main():
    InitialiseFile()    # only run this procedure the 1st time
    CarFile = OpenFileForUpdate()
    ThisCar = CarRecord()

    # add records
    Answer = input("add a record? (Y/N) ")
    while Answer != "N":
        ThisCar = CarRecord()
        ThisCar = InputNewRecordData()
        SaveToFile(ThisCar, CarFile)
        Answer = input("add a record? (Y/N) ")

    # find records
    Answer = input("find a record? (Y/N) ")
    while Answer != "N":
        Reg = input("Give vehicle registration: ")
        ThisCar = FindRecord(Reg, CarFile)
        OutputData(ThisCar)
        Answer = input("find a record? (Y/N) ")
    CarFile.close()


main()
