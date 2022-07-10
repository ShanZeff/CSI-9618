# Summer 21 Q1
# ADT: Linked list -Finished

class Node:
    def __init__(self, TheData, NextNodeNumber):
        self.Data = TheData
        self.NextNode = NextNodeNumber


def OutputNodes(LinkedList, CurrentPointer):
    while CurrentPointer != -1:
        print(str(LinkedList[CurrentPointer].Data))
        CurrentPointer = LinkedList[CurrentPointer].NextNode


def AddNode(LinkedList, CurrentPointer, EmptyList):
    DataToAdd = input("Enter the data to add: ")
    if EmptyList < 0 or EmptyList > 9:
        return False
    else:
        NewNode = Node(int(DataToAdd), -1)
        LinkedList[EmptyList] = NewNode
        PreviousPointer = 0
        while CurrentPointer != -1:
            PreviousPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].NextNode
        LinkedList[PreviousPointer].NextNode = EmptyList
        EmptyList = LinkedList[EmptyList].NextNode
        return True


def main():
    LinkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2), Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]
    StartPointer = 0
    EmptyList = 5
    OutputNodes(LinkedList, StartPointer)
    ReturnValue = AddNode(LinkedList, StartPointer, EmptyList)
    if ReturnValue == True:
        print("Item successfully added.")
    else:
        print("Item not added, list full.")
    OutputNodes(LinkedList, StartPointer)


main()
