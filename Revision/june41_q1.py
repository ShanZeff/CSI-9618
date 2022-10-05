# June 41 2022: Q1
# Text file

FileData = [[""] * 2 for i in range(11)]  # STRING


def ReadHighScores():
    Filename = "C:/Users/shnaya/Desktop/9618 Practical/9618_sum22_sf_41/HighScore.txt"
    File = open(Filename, 'r')
    for x in range(0, 10):
        FileData[x][0] = File.readline()[:3]
        FileData[x][1] = File.readline()
    File.close()


def OutputHighScores():
    for x in range(0, 11):
        Output = FileData[x][0] + " " + FileData[x][1]
        print(Output)


def Arrange(Username, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = Username
            FileData[x][1] = Score
            Count = x + 1
            while Count < 10:
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2

                Temp1 = Second1
                Temp2 = Second2
                Count = Count + 1
                break


def WriteTopTen():
    Filename = "NewHighScore.txt"
    Filename = open(Filename, 'w')
    for x in range(0, 10):
        Filename.write(str(FileData[x][0]) + '\n')
        Filename.write(str(FileData[x][1]) + '\n')
        Filename.close


def main():
    ReadHighScores()
    OutputHighScores()
    # Username = "ABCD"
    # while len(Username) != 3:
    #     Username = input("Enter your Username: ")
    # Score = -1
    # while Score < 1 or Score > 100000:
    #     Score = int(input("Enter score:"))

    Username = input("Enter your Username: ")
    Score = -1
    while Score < 0 or Score > 100000:
        Score = int(input("Enter score: "))
    Arrange(Username, Score)
    OutputHighScores()


main()
