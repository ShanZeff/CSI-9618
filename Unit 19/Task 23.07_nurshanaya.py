# Stack

null_pointer = -1


class Node:
    def __init__(self):
        self.data = ""
        self.pointer = null_pointer


def initialise_stack():
    Stack = [Node() for i in range(8)]
    TopOfStack = null_pointer
    FreeListPtr = 0
    for index in range(7):
        Stack[index].pointer = index + 1
    Stack[7].pointer = null_pointer
    return Stack, TopOfStack, FreeListPtr


def push(Stack, TopOfStack, FreeListPtr, new_item):
    if FreeListPtr != null_pointer:
        NewNodePtr = FreeListPtr
        Stack[NewNodePtr].data = new_item
        FreeListPtr = Stack[FreeListPtr].pointer
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
    CurrentNodePtr = TopOfStack
    if TopOfStack == null_pointer:
        print("No data on stack")
    while CurrentNodePtr != null_pointer:
        print(CurrentNodePtr, " ", Stack[CurrentNodePtr].data)
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
