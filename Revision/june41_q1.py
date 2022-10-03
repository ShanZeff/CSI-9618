# June 41 2022: Q1
# Text file

FileData = [[""] * 2 for i in range(11)]  # STRING


def ReadHighScores():
    Filename = "HighScore.txt"
    File = open(Filename, 'r')
    for x in range(0, 10):
        FileData[x][0] = File.readline()[:3]
        FileData[x][1] = File.readline()
    File.close()


def OutputHighScores():
    for x in range(0, 11):
        Output = FileData[x][0] + " " + FileData[x][1]
        print(Output)


def main():
    ReadHighScores()
    OutputHighScores()


main()
