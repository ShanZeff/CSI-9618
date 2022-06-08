#

import pickle
class CustomerRecord:
    def __init__(self):
        self.CustomerID = 0
        self.CustomerName = ''
        self.TelNumber = ''
        self.TotalOrders = 0


def Hash(CustomerID):
    Address = CustomerID % 1000
    return Address


def AddRecord(CustomerData, Customer):
    Address = Hash(Customer.CustomerID)
    while CustomerData[Address].CustomerID != 0:
        if Address == 1000:
            Address = 0
    CustomerData[Address] = Customer


def FindRecord(CustomerData, CustomerID):
    Address = Hash(CustomerID)
    while CustomerData[Address].CustomerID != 0:
        if Address == 1000:
            Address = 0
    return Address


def SaveData(CustomerData):
    CustomerFile = open('CustomerData.DAT', 'wb')
    for i in range(1000):
        pickle.dump(CustomerData[i], CustomerFile)
    CustomerFile.close()


def main():
    CustomerData = [CustomerRecord() for i in range(1000)]


main()
