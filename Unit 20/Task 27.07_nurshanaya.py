# Task 27.07 Polymorphism
# From 27.06. Write the program to implement a library system.
# Write code to provide the user with a menu option.

import datetime

# Borrower class ***********************************************************
class TBorrower:
    def __init__(self, n, e, i):
        self.__BorrowerName = n
        self.__EmailAddress = e
        self.__BorrowerID = i
        self.__ItemsOnLoan = 0

    def GetBorrowerName(self):
        return self.__BorrowerName

    def GetEmailAddress(self):
        return self.__EmailAddress

    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan

    def UpdateItemsOnLoan(self, n):
        self.__ItemsOnLoan = self.__ItemsOnLoan + n

    def PrintDetails(self):
        print(self.__BorrowerName, ';', self.__BorrowerID, ';', end='')
        print(self.__EmailAddress, ';', self.__ItemsOnLoan)


# Library Item class *******************************************************
class TLibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t            # DECLARE Title             : STRING
        self.__Author__Artist = a   # DECLARE Author__Artist    : STRING
        self.__ItemID = i           # DECLARE ItemID            : INTEGER
        self.__OnLoan = False       # DECLARE OnLoan            : BOOLEAN
        self.__BorrowerID = 0       # DECLARE BorrowerID        : INTEGER
        self.__DueDate = datetime.date.today()  # DECLARE DueDate: DATE

    def GetTitle(self):
        return self.__Title

    def GetAuthor_Artist(self):
        return self.__Author__Artist

    def GetItemID(self):
        return self.__ItemID

    def GetOnLoan(self):
        return self.__OnLoan

    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetDueDate(self):
        return self.__DueDate

    def Borrowing(self, i, x):
        if x.GetItemsOnLoan() < 5:
            self.__OnLoan = True
            self.__BorrowerID = x.GetBorrowerID()
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
            x.UpdateItemsOnLoan(1)
        else:
            print("Too many books on loan")

    def Returning(self, i, x):
        self.__OnLoan = False
        x.UpdateItemsOnLoan(-1)

    def PrintDetails(self):
        print(self.__Title, ';', self.__Author__Artist, end=' ')
        print(self.__ItemID, ';', self.__OnLoan, ';', end=' ')
        print(self.__BorrowerID, ';', self.__DueDate)


# Book class ***************************************************************
