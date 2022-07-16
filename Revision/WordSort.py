# sorts alphabetical order
# words in text file

class WordsCollection:
    def __init__(self, WordsP):
        self.__Words = WordsP


def OutputList(WordList):
    for i in range(0, 15):
        print(WordList[i])


WordList = []
for i in range(100):
    WordList.append(WordsCollection(""))

def LoadWords():
    FileName = "Words.txt"
    try:
        File = open(FileName, "r")
        DataFetched = (File.readline()).strip()
        while DataFetched != "":
            Words = (File.readline()).strip()
            WordList.append(WordsCollection(Words))
            DataFetched = (File.readline()).strip()
        File.close()
    except IOError:
        print("The file does not exist.")


LoadWords()
OutputList(WordList)
