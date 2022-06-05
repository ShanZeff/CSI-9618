# Task 27.01: 2 OOP Instantiation
# A business wants to store data about companies they supply
# The data to be stored: company name, email address, date of last contact

from datetime import *
class Company:
    def __init__(self, n, e):   # constructor
        self.__CompanyName = n              # DECLARE CompanyName   	: STRING
        self.__EmailAddress = e             # DECLARE EmailAddress  	: STRING
        self.__DateOfLastContact = None     # DECLARE DateOfLastContact	: DATE

    def SetDateOfLastContact(self, d):
        self.__DateOfLastContact = d

    def GetCompanyName(self):
        return self.__CompanyName

    def GetEmailAddress(self):
        return self.__EmailAddress

    def GetDateOfLastContact(self):
        return self.__DateOfLastContact


ThisCompany = Company("SLimited", "abc@slimited.cie")
ThisCompany.SetDateOfLastContact(date(2016, 2, 1))
print(ThisCompany.GetDateOfLastContact())
