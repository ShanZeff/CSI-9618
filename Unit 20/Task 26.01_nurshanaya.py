# Task 26.01 Record and Sequential file
# 1. Write a complete program to save several car records to a
#    sequential file
# 2. Write another program to read the file and display the
#    contents on screen

# For exception line 36
# Record Number?: 0 will cause an error w/o exception
# bcuz the file has reached its end w no content

import pickle   # this library is required to create binary files
from datetime import date

class CarRecord:
    def __init__(self):
        self.VehicleID = "dummy"
        self.Registration = " "
        self.DateOfRegistration = date(1990, 1, 1)
        self.EngineSize = 0
        self.PurchasePrice = 0.0


def SaveData(Car):
    # file channel for car records
    CarFile = open("CarFile.DAT", "wb")
    for i in range(100):    # loop for each array element
        # write a whole record to the binary file
        pickle.dump(Car[i], CarFile)
    CarFile.close()     # close file


def LoadData():
    CarFile = open("CarFile.DAT", "rb")    # open file for binary read
    Car = []    # start with empty list
    EoF = False
    while not EoF:      # check for end of file
        try:
            Car.append(pickle.load(CarFile))  # append record from file to end of list
        except:
            EoF = True
    CarFile.close()
    return Car


def OutputRecords(Car):
    for i in range(100):    # loop for each array element
        print(Car[i].VehicleID)     # write one field


def main():
    ThisCar = CarRecord()
    Car = [ThisCar for i in range(100)]     # only run this 1st time
    SaveData(Car)           # only run this 1st time
    Car = LoadData()        # from existing file
    # OutputRecords(Car)
    # add more records
    i = int(input("Record Number?: "))
    while i != 0:
        Car[i].VehicleID = input("Vehicle ID: ")
        Car[i].Registration = input("Registration: ")
        Car[i].DateOfRegistration = input("Registration Date: ")
        Car[i].EngineSize = int(input("Engine size: "))
        Car[i].PurchasePrice = float(input("Purchase price: "))
        i = int(input("next Record Number?: "))
    OutputRecords(Car)
    SaveData(Car)


main()
