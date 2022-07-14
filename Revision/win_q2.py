# Winter 21 Q2
# OOP: Files -Finished

class Picture:
    def __init__(self, DescriptionP, WidthSizeP, HeightSizeP, FrameColourP):
        self.__Description = DescriptionP   # string
        self.__Width = WidthSizeP           # integer
        self.__Height = HeightSizeP         # integer
        self.__FrameColour = FrameColourP   # string

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, DescriptionP):
        self.__Description = DescriptionP


PictureArray = []
for i in range(100):
    PictureArray.append(Picture("", 0, 0, ""))

def ReadData(PictureArray):
    Filename = "C:/Users/shnaya/Desktop/9618 Practical/9618_win21_sf_41/Pictures.txt"
    Counter = 0
    try:
        File = open(Filename, "r")
        Description = (File.readline()).strip().lower()
        while Description != "":
            Width = int((File.readline()).strip())
            Height = int((File.readline()).strip())
            Frame = (File.readline()).strip().lower()
            PictureArray[Counter] = Picture(Description, Width, Height, Frame)
            Description = (File.readline()).strip().lower()
            Counter = Counter + 1
        File.close()
    except IOError:
        print("Could not find file")
    return Counter


def main():
    NumberPictureInArray = ReadData(PictureArray)
    FrameColour = input("Input the Frame colour: ").lower()
    MaxWidth = int(input("Input the Maximum Width: "))
    MaxHeight = int(input("Input the Maximum Height: "))
    print("Matches frames shown")
    for z in range(0, NumberPictureInArray):
        if PictureArray[z].GetColour() == FrameColour:
            if PictureArray[z].GetWidth() <= MaxWidth:
                if PictureArray[z].GetHeight() <= MaxHeight:
                    print(PictureArray[z].GetDescription(), " ", str(PictureArray[z].GetWidth()), str(PictureArray[z].GetHeight()))


main()
