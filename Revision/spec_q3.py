# Specimen 21 Q3
# ADT: Queue, Files
# Not Finished

import os
QueueData = ["" for i in range(0, 20)]

def Enqueue(DataToAdd, QueueData, EndP):
    if EndP == 20:
        return False, EndP
    else:
        QueueData[EndP] = DataToAdd
        EndP = EndP + 1
        return True, EndP


def ReadFile(QueueData, StartP, EndP):
    FileName = input("Enter a filename: ")
    if os.path.isfile(FileName):
        f = open(FileName, "r")
        Flag = True
        DataToInsert = (f.readline()).strip()
        while Flag == True and DataToInsert != None:
            Flag, EndP = Enqueue(QueueData, EndP)
            DataToInsert = (f.readline()).strip()
        if Flag == False:
            f.close()
            return 1, EndP
        else:
            f.close()
            return 2, EndP
    else:
        return -1, EndP


def Remove(QueueData, StartP, EndP):
    if EndP - StartP < 2:
        return "No Items", StartP, EndP
    else:
        Value1 = QueueData[StartP]
        StartP = StartP + 1
        Value2 = QueueData[StartP]
        StartP = StartP + 1
        return (Value1 + " " + Value2), StartP, EndP


def main():
    StartPointer = 0
    EndPointer = 0
    ReturnValue, EndPointer = ReadFile(QueueData, StartPointer, EndPointer)
    if ReturnValue == -1:
        print("The file could not be found.")
    elif ReturnValue == 1:
        print("The queue was full, not all items were read.")
    else:
        print("All items successfully added.")


main()
