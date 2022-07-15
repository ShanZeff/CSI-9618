# ADT: Linked List

# NullPointer should be set to -1 if using array element with index 0
NullPointer = -1


# Declare record type to store Data and Pointer
class ListNode:
    def __init__(self):
        self.Data = ""
        self.Pointer = NullPointer


def InitialiseList():
    List = [ListNode() for i in range(8)]
    StartPointer = NullPointer    # set start Pointer
    FreeListPtr = 0               # set starting position of free List
    for Index in range(7):          # link all nodes to make free List
        List[Index].Pointer = Index + 1
    List[7].Pointer = NullPointer  # last node of free List
    return List, StartPointer, FreeListPtr


def InsertNode(List, StartPointer, FreeListPtr, NewItem):
    if FreeListPtr != NullPointer:
        # there is space in the array
        # take node from free List and store Data item
        NewNodePtr = FreeListPtr
        List[NewNodePtr].Data = NewItem
        FreeListPtr = List[FreeListPtr].Pointer
        # find insertion point
        PreviousNodePtr = NullPointer
        ThisNodePtr = StartPointer   # start at beginning of List
        while ThisNodePtr != NullPointer and List[ThisNodePtr].Data < NewItem:

            # while not end of List
            PreviousNodePtr = ThisNodePtr   # remember this node
            # follow the Pointer to the next node
            ThisNodePtr = List[ThisNodePtr].Pointer

        if PreviousNodePtr == NullPointer:
            # insert new node at start of List
            List[NewNodePtr].Pointer = StartPointer
            StartPointer = NewNodePtr
        else:   # insert new node between previous node and this node
            List[NewNodePtr].Pointer = List[PreviousNodePtr].Pointer
            List[PreviousNodePtr].Pointer = NewNodePtr
    else:
        print("no space for more Data")
    return List, StartPointer, FreeListPtr


def FindNode(List, StartPointer, data_item):  # returns Pointer to node
    CurrentNodePtr = StartPointer    # start at beginning of List
    while CurrentNodePtr != NullPointer and List[CurrentNodePtr].Data != data_item:
        # not end of List, item not found
        # follow the Pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer
    return CurrentNodePtr     # return NullPointer if item not found


def DeleteNode(List, StartPointer, FreeListPtr, data_item):
    ThisNodePtr = StartPointer       # start at beginning of List
    while ThisNodePtr != NullPointer and List[ThisNodePtr].Data != data_item:
        # while not end of List and item not found
        PreviousNodePtr = ThisNodePtr   # remember this node
        # follow the Pointer to the next node
        ThisNodePtr = List[ThisNodePtr].Pointer
    if ThisNodePtr != NullPointer:       # node exists in List
        if ThisNodePtr == StartPointer:  # first node to be deleted
            StartPointer == List[StartPointer].Pointer
        else:
            List[PreviousNodePtr].Pointer = List[ThisNodePtr].Pointer
        List[ThisNodePtr].Pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    else:
        print("Data does not exist in List")
    return List, StartPointer, FreeListPtr


def OutputAllNodes(List, StartPointer):
    CurrentNodePtr = StartPointer    # start at beginning of List
    if StartPointer == NullPointer:
        print("No Data in List")
    while CurrentNodePtr != NullPointer:     # while not end of List
        print(CurrentNodePtr, " ", List[CurrentNodePtr].Data)
        # follow the Pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer


def GetOption():
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output List")
    print("5: end program")
    option = input("Enter your choice: ")
    return option


List, StartPointer, FreeListPtr = InitialiseList()

option = GetOption()
while option != "5":
    if option == "1":
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = InsertNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif option == "2":
        Data = input("Enter the value: ")
        List, StartPointer, FreeListPtr = DeleteNode(List, StartPointer, FreeListPtr, Data)
        OutputAllNodes(List, StartPointer)
    elif option == "3":
        Data = input("Enter the value: ")
        CurrentNodePtr = FindNode(List, StartPointer, Data)
        if CurrentNodePtr == NullPointer:
            print("Data not found")
        print(StartPointer, FreeListPtr)
        for i in range(8):
            print(i, " ", List[i].Data, " ", List[i].Pointer)
    elif option == "4":
        OutputAllNodes(List, StartPointer)
    option = GetOption()
