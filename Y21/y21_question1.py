# NumberOfItems = 9
# TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

# def InsertionData(TheData):
#    for Count in range(FirstElement, NumberOfItems - 1):
#        Data

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue+1] = DataToInsert
            else:
                Inserted = 1


def PrintArray(TheData):
    for Count in range(0, len(TheData)):
        print(TheData[Count])


def Search(TheData):
    NumberInput = int(input("Enter a whole number: "))
    for Count in range(0, len(TheData)):
        if TheData[Count] == NumberInput:
            print("Found")
            return True
    print("False")
    return False


def main():
    print("Before")
    PrintArray(TheData)
    InsertionSort(TheData)
    print("After")
    PrintArray(TheData)


main()
