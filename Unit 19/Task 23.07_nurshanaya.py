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
        FreeListPtr = stack[FreeListPtr].pointer
        stack[NewNodePtr], pointer = TopOfStack
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
        this_node_ptr = TopOfStack
        TopOfStack = Stack[TopOfStack].pointer
        Stack[this_node_ptr].pointer = FreeListPtr
        FreeListPtr = this_node_ptr
    return Stack, TopOfStack, FreeListPtr, value


def output_all_nodes(Stack, TopOfStack):
    current_node_ptr = TopOfStack
    if TopOfStack == null_pointer:
        print("No data on stack")
    while current_node_ptr != null_pointer:
        print(current_node_ptr, " ", Stack[current_node_ptr].data)
        current_node_ptr = Stack[current_node_ptr].pointer


def get_option():
    print("1: push a value")
    print("2: pop a value")
    print("3: output stack")
    print("4: end program")
    option = input("Enter your choice: ")
    return option


stack, top_of_stack, free_list_ptr = initialise_stack()


option = get_option()
while option != "4":
    if option == "1":
        data = input("Enter the value: ")
        stack, top_of_stack, free_list_ptr = push(stack, top_of_stack, free_list_ptr, data)
        output_all_nodes(stack, top_of_stack)
    elif option == "2":
        stack, top_of_stack, free_list_ptr, value = pop(stack, top_of_stack, free_list_ptr)
        print("Data popped: ", value)
        output_all_nodes(stack, top_of_stack)
    elif option == "3":
        output_all_nodes(stack, top_of_stack)
        print(top_of_stack, free_list_ptr)
        for i in range(8):
            print(i, " ", stack[i].data, " ", stack[i].pointer)
    option = get_option()
