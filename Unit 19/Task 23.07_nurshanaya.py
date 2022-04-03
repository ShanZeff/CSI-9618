# Stack
# NullPointer should be set to -1 if using array element with index 0
null_pointer = -1


# Declare record type to store data and pointer
class Node:
    def __init__(self):
        self.data = ""
        self.pointer = null_pointer


def initialise_stack():
    Stack = [Node() for i in range(8)]
    TopOfStack = null_pointer               # set start pointer
    FreeListPtr = 0                         # set starting position of free list
    for index in range(7):                  # link all nodes to make free list
        Stack[index].pointer = index + 1
    Stack[7].pointer = null_pointer         # last node of free list
    return Stack, TopOfStack, FreeListPtr


def push(Stack, TopOfStack, FreeListPtr, new_item):
    if FreeListPtr != null_pointer:
        # there is space in the array
        # take node from free list and store data item
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].data = new_item
        FreeListPtr = Stack[FreeListPtr].pointer
        # insert new node at top of stack
        Stack[NewNodePtr].pointer = TopOfStack
        TopOfStack = NewNodePtr
    else:
        print("no space for more data")
    return Stack, TopOfStack, FreeListPtr


def pop(Stack, TopOfStack, FreeListPtr):
    if TopOfStack == null_pointer:
        print("no data on stack")
        value = ""
    else:
        value = Stack[TopOfStack].data
        ThisNodePtr = TopOfStack
        TopOfStack = Stack[TopOfStack].pointer
        Stack[ThisNodePtr].pointer = FreeListPtr
        FreeListPtr = ThisNodePtr
    return Stack, TopOfStack, FreeListPtr, value


def output_all_nodes(Stack, TopOfStack):
    CurrentNodePtr = TopOfStack                     # start at beginning of list
    if TopOfStack == null_pointer:
        print("No data on stack")
    while CurrentNodePtr != null_pointer:           # while not end of list
        print(CurrentNodePtr, " ", Stack[CurrentNodePtr].data)
        # follow the pointer to the next node
        CurrentNodePtr = Stack[CurrentNodePtr].pointer


def get_option():
    print("1: push a value")
    print("2: pop a value")
    print("3: output stack")
    print("4: end program")
    option = input("Enter your choice: ")
    return option


Stack, TopOfStack, FreeListPtr = initialise_stack()


option = get_option()
while option != "4":
    if option == "1":
        data = input("Enter the value: ")
        Stack, TopOfStack, FreeListPtr = push(Stack, TopOfStack, FreeListPtr, data)
        output_all_nodes(Stack, TopOfStack)
    elif option == "2":
        Stack, TopOfStack, FreeListPtr, value = pop(Stack, TopOfStack, FreeListPtr)
        print("Data popped: ", value)
        output_all_nodes(Stack, TopOfStack)
    elif option == "3":
        output_all_nodes(Stack, TopOfStack)
        print(TopOfStack, FreeListPtr)
        for i in range(8):
            print(i, " ", Stack[i].data, " ", Stack[i].pointer)
    option = get_option()
