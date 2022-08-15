class Balloon:
    # Private DefenceItem : STRING
    # Private Colour : STRING
    # Private Health : INTEGER

    def _init_(self, DefenceItemP, ColourP):
        self.__DefenceItem = DefenceItemP
        self.__Colour = ColourP
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, Number):
        NewHealth = self.__Health + Number
        return NewHealth

    def CheckHealth(self, NewHealth):
        if NewHealth == 0 or NewHealth < 0:
            return True
        else:
            return False


def Defend(BalloonUser):
    OpponentStrength = input("Enter in the strength of opponent: ")
    ChangeHealth(self, ?)


def main():
        ItemInput = input("Enter in a defence item: ")
        ColourInput = input("Enter in a colour: ")
        Balloon1 = Balloon(ItemInput, ColourInput)

    main()