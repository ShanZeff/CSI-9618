# Specimen 21 Q2
# OOP -Finished

class HiddenBox:
    # Private BoxName : String
    # Private Creator : String
    # Private DateHidden : String
    # Private GameLocation : String
    # Private LastFinds [10] [2] : String
    # Private Active : Boolean

    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation):
        self.__BoxName = NewBoxName
        self.__Creator = NewCreator
        self.__DateHidden = NewDateHidden
        self.__GameLocation = NewLocation
        self.__LastFinds = [["" for j in range(0, 2)] for i in range(0, 10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetLocation(self):
        return self.__GameLocation


def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Enter the name of the box: ")
    Creator = input("Enter the creator's name: ")
    DateHidden = input("Enter the date the box was hidden: ")
    GameLocation = input("Enter the location of the box: ")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return NumBoxes + 1


class PuzzleBox(HiddenBox):
    # __PuzzleText String
    # __Solution String

    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution):
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution


def main():
    TheBoxes = [HiddenBox("", "", "", "") for i in range(0, 10000)]
    NumBoxes = 0
    NewBox(TheBoxes, NumBoxes)


main()
