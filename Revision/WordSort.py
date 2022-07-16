# Array WordList holds 15 elements
# Print all words in index order
# LoadWords: store file content to WordList

def OutputList(WordList):
    for i in range(0, 15):
        print(WordList[i])


def LoadWords(WordList):
    FileName = "Words.txt"
    try:
        File = open(FileName, "r")
        DataFetched = (File.readline()).strip()
        while DataFetched != "":
            Words = (File.readline()).strip()
            WordList.append(Words)
            DataFetched = (File.readline()).strip()
        File.close()
    except IOError:
        print("The file does not exist.")


def main():
    WordList = []
    LoadWords(WordList)
    OutputList(WordList)


main()
