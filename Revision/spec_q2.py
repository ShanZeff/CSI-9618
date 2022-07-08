# Specimen 21 Q2

class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10] [2] String
    # __Active Boolean

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


TheBoxes = [HiddenBox("", "", "", "") for i in range(0, 10000)]

def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Enter the name of the box: ")
    Creator = input("Enter the creator's name: ")
    DateHidden = input("Enter the date the box was hidden: ")
    GameLocation = input("Enter the location of the box: ")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return NumBoxes + 1


NumBoxes = NewBox(TheBoxes, NumBoxes)

class PuzzleBox(HiddenBox):
    # __PuzzleText String
    # __Solution String

    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution):
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation)
        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution
