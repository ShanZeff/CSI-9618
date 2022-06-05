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
class TBook(TLibraryItem):
    def __init__(self, t, a, i):
        TLibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return self.__IsRequested

    def GetRequestedBy(self):
        return self.__RequestedBy

    def RequestBook(self, i, x):
        self.__IsRequested = True
        self.__RequestedBy = x.GetBorrowerID()

    def PrintDetails(self):
        TLibraryItem.PrintDetails(self)
        print(self.__IsRequested, ';', self.__RequestedBy)


# CD class *****************************************************************
class T_CD(TLibraryItem):
    def __init__(self, t, a, i):
        TLibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g

    def PrintDetails(self):
        TLibraryItem.PrintDetails(self)
        print(self.__Genre)


# Display menu *************************************************************
def DisplayMenu():
    print("1 - Add a new borrower")
    print("2 - Add a new book")
    print("3 - Add a new CD")
    print("4 - Borrow book")
    print("5 - Return book")
    print("6 - Borrow CD")
    print("7 - Return CD")
    print("8 - Request book")
    print("9 - Print all details")
    print("99 - Exit program")
    print(" ")
    print("Enter your menu choice: ")


# Main program ************************************************************
