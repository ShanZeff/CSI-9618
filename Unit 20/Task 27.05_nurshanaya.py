# Task 27.05 Polymorphism
# From 27.03, add another attribute BorrowerID to the LibraryItem class.

import datetime
class LibraryItem:
    def __init__(self, t, a, i):    # initialiser method
        self.__Title = t            # DECLARE Title             : STRING
        self.__Author__Artist = a   # DECLARE Author__Artist    : STRING
        self.__ItemID = i           # DECLARE ItemID            : INTEGER
        self.__OnLoan = False       # DECLARE OnLoan            : BOOLEAN
        self.__DueDate = datetime.date.today()  # DECLARE DueDate: DATE
        self.__BorrowerID = 0       # DECLARE BorrowerID        : INTEGER

    def GetTitle(self):
        return self.__Title

    def GetAuthor_Artist(self):
        return self.__Author__Artist

    def GetItemID(self):
        return self.__ItemID

    def GetOnLoan(self):
        return self.__OnLoan

    def GetDueDate(self):
        return self.__DueDate

    def Borrowing(self, b):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
        self.__BorrowerID = b

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author__Artist, ' ; ', end='')
        print(self.__ItemID, ' ; ', self.__OnLoan)
        print(self.__DueDate, ' ; Borrower: ', self.__BorrowerID)


class Book(LibraryItem):
    def __init__(self, t, a, i):  # initialiser method
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False

    def GetIsRequested(self):
        return self.__IsRequested

    def SetIsRequested(self):
        self.__IsRequested = True


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return self.__Genre

    def SetGenre(self, g):
        self.__Genre = g


class Borrower:
    def __init__(self, n, e, b):
        self.__BorrowerName = n     # DECLARE BorrowerName  : STRING
        self.__EmailAddress = e     # DECLARE EmailAddress  : STRING
        self.__BorrowerID = b       # DECLARE BorrowerID    : INTEGER
        self.__ItemsOnLoan = 0      # DECLARE ItemsOnLoan   : INTEGER

    def GetBorrowerName(self):
        return self.__BorrowerName

    def GetEmailAddress(self):
        return self.__EmailAddress

    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetItemsOnLoan(self):
        return self.__ItemsOnLoan

    def UpdateItemsOnLoan(self, n):
        self.__ItemsOnLoan += n

    def PrintDetails(self):
        print("Borrower         : ", self.__BorrowerName)
        print("ID               : ", self.__BorrowerID)
        print("Email            : ", self.__EmailAddress)
        print("Items on  loan   : ", self.__ItemsOnLoan)


def main():
    ThisBook = Book("Computing", "Sylvia", 1234)
    ThisBook.PrintDetails()
    NewBorrower = Borrower("Fred", "adc@cie", 123)
    ThisBook.Borrowing(123)
    NewBorrower.UpdateItemsOnLoan(1)
    ThisBook.PrintDetails()
    NewBorrower.PrintDetails()


main()
