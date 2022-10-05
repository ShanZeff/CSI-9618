# June 42 2022: Q3
# OOP

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


def main():
    CardArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # INTEGER

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


main()
