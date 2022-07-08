# Summer 21 Q3

class TreasureChest:
    # Private Question : String
    # Private Answer   : Integer
    # Private Points   : Integer

    def __init__(self, QuestionP, AnswerP, PointsP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Points = PointsP


# ArrayTreasure(5) as TreasureChest
def ReadData():
    Filename = "TreasureChestData.txt"
    try:
        File = open(Filename, "r")
        DataFetched = (File.readline()).strip()
        while DataFetched != "":
            Question = DataFetched
            Answer = (File.readline()).strip()
            Points = (File.readline()).strip()
            ArrayTreasure.append(TreasureChest(Question, Answer, Points))
            DataFetched = (File.readline()).strip()
        file.close()
    except IOError:
        print("Could not find file")


def GetQuestion(self):
    return self.__Question


def CheckAnswer(self, AnswerP):
    if int(self.__Answer) == AnswerP:
        return True
    else:
        return False


def GetPoints(self, Attempts):
    if Attempts == 1:
        return int(self.__Points)
    elif Attempts == 2:
        return int(self__Points) // 2
    elif Attempts == 3 or Attempts == 4:
        return int(self.__Points) // 4
    else:
        return 0


def main():
    ReadData()
    Choice = int(input("Pick a treasure chest to open: "))
    if Choice > 0 and Choice < 6:
        Result = False
        Attempts = 0
        while Result == False:
            Answer: int(input(ArrayTreasure[Choice-1]).GetQuestion())
            Result = ArrayTreasure[Choice-1].CheckAnswer(Answer)
            Attempts = Attempts + 1
        print(int(ArrayTreasure[Choice-1].GetPoints(Attempts)))
