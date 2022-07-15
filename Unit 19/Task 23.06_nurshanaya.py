# ADT: Binary Search Tree

# NullPointer should be set to -1 if using array element with Index 0
NullPointer = -1

# Declare record type to store Data and pointer
class TreeNode:
    def __init__(self):
        self.Data = ""
        self.LeftPointer = NullPointer
        self.RightPointer = NullPointer


def InitialiseTree():
    Tree = [TreeNode() for i in range(8)]
    RootPointer = NullPointer       # set Root pointer
    FreePtr = 0                     # set starting position of free list
    for Index in range(7):          # link all nodes to make free list
        Tree[Index].LeftPointer = Index + 1
    return Tree, RootPointer, FreePtr


def InsertNode(Tree, RootPointer, FreePtr, NewItem):
    if FreePtr != NullPointer:
        # there is space in the array
        # take node from free list and store Data item
        NewNodePtr = FreePtr
        Tree[NewNodePtr].Data = NewItem
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr].LeftPointer = NullPointer

        # check if empty Tree
        if RootPointer == NullPointer:
            # insert new node at root
            RootPointer = NewNodePtr
        else:   # find insertion point
            ThisNodePtr = RootPointer
            while ThisNodePtr != NullPointer:   # while not a leaf node
                PreviousNodePtr = ThisNodePtr   # remember this node
                if Tree[ThisNodePtr].Data > NewItem:
                    TurnedLeft = True
                    ThisNodePtr = Tree[ThisNodePtr].LeftPointer
                else:
                    TurnedLeft = False
                    ThisNodePtr = Tree[ThisNodePtr].RightPointer
                if TurnedLeft:
                    Tree[PreviousNodePtr].LeftPointer = NewNodePtr
                else:
                    Tree[PreviousNodePtr].RightPointer = NewNodePtr
    else:
        print("No space for more Data")
    return Tree, RootPointer, FreePtr


def FindNode(Tree, RootPointer, SearchItem):
    ThisNodePtr = RootPointer    # start at the root of the Tree
    while ThisNodePtr != NullPointer and Tree[ThisNodePtr].Data != SearchItem:
        # while there is a pointer to follow and search item not found
        if Tree[ThisNodePtr].Data > SearchItem:
            ThisNodePtr = Tree[ThisNodePtr].LeftPointer    # follow left pointer
        else:
            ThisNodePtr = Tree[ThisNodePtr].RightPointer   # follow right pointer
    return ThisNodePtr


def TraverseTree(Tree, RootPointer):
    if RootPointer != NullPointer:
        TraverseTree(Tree, Tree[RootPointer].LeftPointer)
        print(Tree[RootPointer].Data)
        TraverseTree(Tree, Tree[RootPointer].RightPointer)


def GetOption():
    print("1: add Data")
    print("2: find Data")
    print("3: traverse Tree")
    print("4: end program")
    Option = input("Enter your choice: ")
    return Option


def main():
    Tree, RootPointer, FreePtr = InitialiseTree()

    Option = GetOption()
    while Option != "4":
        if Option == "1":
            Data = input("Enter the value: ")
            Tree, RootPointer, FreePtr = InsertNode(Tree, RootPointer, FreePtr, Data)
            TraverseTree(Tree, RootPointer)
        elif Option == "2":
            Data = input("Enter search value: ")
            ThisNodePtr = FindNode(Tree, RootPointer, Data)
            if ThisNodePtr == NullPointer:
                print("Value not found")
            else:
                print("value found at ", ThisNodePtr)
            print(RootPointer, FreePtr)
            for i in range(8):
                print(1, " ", Tree[i].LeftPointer, " ", Tree[i].Data, " ", Tree[i].RightPointer)
        elif Option == "3":
            TraverseTree(Tree, RootPointer)
        Option = GetOption()


main()
