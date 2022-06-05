# Task 27.02 OOP Inheritance
# Copy the class definition from LibraryItem, Book and CD into your IDE
# Write the additional get methods
# Write a simple program to test that each method works

import datetime
class LibraryItem:
    def __init__(self, t, a, i):    # initialiser method
        self.__Title = t            # DECLARE Title             : STRING
        self.__Author__Artist = a   # DECLARE Author__Artist    : STRING
        self.__ItemID = i           # DECLARE ItemID            : INTEGER
        self.__OnLoan = False       # DECLARE OnLoan            : BOOLEAN
        self.__DueDate = datetime.date.today()  # DECLARE DueDate: DATE

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

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title, ' ; ', self.__Author__Artist, end='')
        print(' ; ', self.__ItemID, ' ; ', self.__OnLoan, end='')
        print(' ; ', self.__DueDate)


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

def main():
    ThisBook = Book("Computing", "Sylvia", 1234)
    ThisBook.PrintDetails()     # just personally added this
    ThisCD = CD("Let it be", "Beatles", 2345)
    ThisCD.PrintDetails()


main()
