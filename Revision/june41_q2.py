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
        NewHealth = self.__Health + Number
        return NewHealth


def CheckHealth(Health):
    if Health == 0 or Health < 0:
        return True
    else:
        return False


def Defend(BalloonUser):
    OpponentStrength = int(input("Enter in the opponent's strength: "))
    # change health
    MinusValue = OpponentStrength * -1
    CurrentHealth = BalloonUser.ChangeHealth(MinusValue)

    # output item
    print(BalloonUser.GetDefenceItem())

    # check health
    ReturnValue = CheckHealth(CurrentHealth)
    if ReturnValue == True:
        print("Your balloon has no health remaining.")
    else:
        print("Your balloon has health remaining.")

    return BalloonUser


def main():
    ItemInput = input("Enter in the defence item: ")
    ColourInput = input("Enter in the balloon colour: ")
    Balloon1 = Balloon(ItemInput, ColourInput)
    Defend(Balloon1)


main()
