# Summer 21 Q3
# OOP: Files -Finished
# 2nd test

class TreasureChest:
    # Private Question : String
    # Private Answer   : Integer
    # Private Points   : Integer

    def __init__(self, QuestionP, AnswerP, PointsP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Points = PointsP

    def GetQuestion(self):
        return self.__Question + " "

    def CheckAnswer(self, AnswerP):
        if int(self.__Answer) == AnswerP:
            return True
        else:
            return False

    def GetPoints(self, Attempts):
        if Attempts == 1:
            return int(self.__Points)
        elif Attempts == 2:
            return int(self.__Points) // 2
        elif Attempts == 3 or Attempts == 4:
            return int(self.__Points) // 4
        else:
            return 0


# ArrayTreasure(5) as TreasureChest
ArrayTreasure = []
def ReadData():
    Filename = "C:/Users/shnaya/Desktop/9618 Practical/9618_sum21_sf_41/TreasureChestData.txt"
    try:
        File = open(Filename, "r")
        DataFetched = (File.readline()).strip()
        while DataFetched != "":
            Question = DataFetched
            Answer = (File.readline()).strip()
            Points = (File.readline()).strip()
            ArrayTreasure.append(TreasureChest(Question, Answer, Points))
            DataFetched = (File.readline()).strip()
        File.close()
    except IOError:
        print("Could not find file")


def main():
    ReadData()
    Choice = int(input("Pick a treasure chest to open: "))
    if Choice > 0 and Choice < 6:
        Result = False
        Attempts = 0
        while Result == False:
            Answer = int(input(ArrayTreasure[Choice-1].GetQuestion()))
            Result = ArrayTreasure[Choice-1].CheckAnswer(Answer)
            Attempts = Attempts + 1
        print(int(ArrayTreasure[Choice-1].GetPoints(Attempts)))


main()
