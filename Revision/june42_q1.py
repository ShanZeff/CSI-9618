# June 42 2022: Q1
# ADT: Stack

global StackData  # INTEGER
global StackPointer
StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # INTEGER
StackPointer = 0


def PrintArray():
    global StackData
    global StackPointer
    print("Pointer " + str(StackPointer))
    print("Output:")
    for x in range(0, 10):
        print(StackData[x])


def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = DataToPush
        StackPointer = StackPointer + 1
        return True


def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnData = StackData[StackPointer - 1]
        StackPointer = StackPointer - 1
        return ReturnData


def main():
    StackPointer = 0
    StackData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, 11):
        TempNumber = int(input("Enter a number: "))
        if Push(TempNumber) == True:
            print("Stored")
        else:
            print("Stack full")
    PrintArray()

    Pop()
    Pop()
    PrintArray()


main()
