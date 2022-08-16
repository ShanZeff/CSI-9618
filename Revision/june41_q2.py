# Summer 41 2022 Q2
# OOP
# Corrections made on initial code w/o ms

class Balloon:
    # Private DefenceItem : STRING
    # Private Colour : STRING
    # Private Health : INTEGER

    def __init__(self, DefenceItemP, ColourP):
        self.__DefenceItem = DefenceItemP
        self.__Colour = ColourP
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Number):
        self.__Health = self.__Health + Number  # no need return (procedure), changed variable name

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False  # should've been in class b4, removed variable


def Defend(MyBalloon):
    OpponentStrength = int(input("Enter the opponent's strength: "))
    MyBalloon.ChangeHealth(-OpponentStrength)  # simplified it by using "-OpponentStrength"
    print("You defended with", str(MyBalloon.GetDefenceItem()))

    ReturnValue = MyBalloon.CheckHealth()
    if ReturnValue == True:
        print("Your balloon has no health remaining.")
    else:
        print("Your balloon has health remaining.")
    return MyBalloon


def main():
    ItemInput = input("Enter the defence item: ")
    ColourInput = input("Enter the balloon colour: ")
    Balloon1 = Balloon(ItemInput, ColourInput)
    Balloon1 = Defend(Balloon1)  # storing return value over object


main()
