TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
Count = 0

def InsertionSort(TheData):
    for Count in range(1):
        DataToInsert = TheData[i]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = TheData
            else:
                Inserted = 1
