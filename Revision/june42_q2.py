# June 42 2022: Q2
# Bubble Sort

import random

def Printarray(ArrayData):
    for x in range(0, 10):
        for y in range(0, 10):
            print(ArrayData[x][y], " ", end='')
        print("")


def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= 0:
        Mid = int((Lower + (Upper - 1)) / 2)
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1


def main():
    ArrayData = [[0] * 10 for i in range(10)]  # INTEGER
    for x in range(0, 10):
        for y in range(0, 10):
            ArrayData[x][y] = random.randint(1, 100)

    print("Before")
    Printarray(ArrayData)

    ArrayLength = 10
    for X in range(0, ArrayLength):
        for Y in range(0, ArrayLength - 1):
            for Z in range(0, ArrayLength - Y - 1):
                if ArrayData[X][Z] > ArrayData[X][Z + 1]:
                    TempNumber = ArrayData[X][Z]
                    ArrayData[X][Z] = ArrayData[X][Z + 1]
                    ArrayData[X][Z + 1] = TempNumber

    # ArrayData[X][Z], ArrayData[X][Z+1] = ArrayData[X][Z+1], ArrayData[X][Z]
    print("After")
    Printarray(ArrayData)


main()
