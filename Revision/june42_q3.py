# June 42 2022: Q3
# OOP

global NumbersChosen


class Card:
    # Private Number : INTEGER
    # Private Colour : STRING
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP
        self.__Colour = ColourP

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


def ChooseCard():
    FlagContinue = True
    while FlagContinue == True:
        CardSelected = int(input("Select a card from 1 to 30: "))
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30")
        elif NumbersChosen(CardSelected - 1) == True:
            print("Already taken")
        else:
            print("Valid")
            FlagContinue = False
    NumbersChosen[CardSelected - 1] = True
    return CardSelected - 1


def main():
    CardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # INTEGER
    NumbersChosen = [False for i in range(30)]

    try:
        Filename = "CardValues.txt"
        File = open(Filename, 'r')
        for x in range(0, 30):
            NumberRead = int(File.readline())
            ColourRead = File.readline()
            CardArray[x] = Card(NumberRead, ColourRead)
            File.close()
    except IOError:
        print("Could not find file")

    Player1 = []  # of type Card
    for x in range(0, 4):
        ReturnNumber = ChooseCard()
        Player1.append(CardArray[ReturnNumber])
    for x in range(0, 4):
        print(Player1[x].GetColour())
        print(Player1[x].GetNumber())


main()
