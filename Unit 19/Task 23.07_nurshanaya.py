# ADT: Stack

# NullPointer should be set to -1 if using array element with Index 0
NullPointer = -1

# Declare record type to store Data and Pointer
class Node:
    def __init__(self):
        self.Data = ""
        self.Pointer = NullPointer


def InitialiseStack():
    Stack = [Node() for i in range(8)]
    TopOfStack = NullPointer            # set start Pointer
    FreeListPtr = 0                     # set starting position of free list
    for Index in range(7):              # link all nodes to make free list
        Stack[Index].Pointer = Index + 1
    Stack[7].Pointer = NullPointer      # last node of free list
    return Stack, TopOfStack, FreeListPtr


def Push(Stack, TopOfStack, FreeListPtr, NewItem):
    if FreeListPtr != NullPointer:
        # there is space in the array
        # take node from free list and store Data item
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].Data = NewItem
        FreeListPtr = Stack[FreeListPtr].Pointer
        # insert new node at top of stack
        Stack[NewNodePtr].Pointer = TopOfStack
        TopOfStack = NewNodePtr
    else:
        print("no space for more Data")
    return Stack, TopOfStack, FreeListPtr


def Pop(Stack, TopOfStack, FreeListPtr):
    if TopOfStack == NullPointer:
        print("no Data on stack")
        Value = ""
    else:
        Value = Stack[TopOfStack].Data
        ThisNodePtr = TopOfStack
        TopOfStack = Stack[TopOfStack].Pointer
        Stack[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    return Stack, TopOfStack, FreeListPtr, Value


def OutputAllNodes(Stack, TopOfStack):
    CurrentNodePtr = TopOfStack             # start at beginning of list
    if TopOfStack == NullPointer:
        print("No Data on stack")
    while CurrentNodePtr != NullPointer:    # while not end of list
        print(CurrentNodePtr, " ", Stack[CurrentNodePtr].Data)
        # follow the Pointer to the next node
        CurrentNodePtr = Stack[CurrentNodePtr].Pointer


def GetOption():
    print("1: Push a value")
    print("2: Pop a value")
    print("3: Output stack")
    print("4: End program")
    Option = input("Enter your choice: ")
    return Option


def main():
    Stack, TopOfStack, FreeListPtr = InitialiseStack()

    Option = GetOption()
    while Option != "4":
        if Option == "1":
            Data = input("Enter the Value: ")
            Stack, TopOfStack, FreeListPtr = Push(Stack, TopOfStack, FreeListPtr, Data)
            OutputAllNodes(Stack, TopOfStack)
        elif Option == "2":
            Stack, TopOfStack, FreeListPtr, Value = Pop(Stack, TopOfStack, FreeListPtr)
            print("Data popped: ", Value)
            OutputAllNodes(Stack, TopOfStack)
        elif Option == "3":
            OutputAllNodes(Stack, TopOfStack)
            print(TopOfStack, FreeListPtr)
            for i in range(8):
                print(i, " ", Stack[i].Data, " ", Stack[i].Pointer)
        Option = GetOption()


main()
