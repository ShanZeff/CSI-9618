# Stack

null_pointer = -1

class node:
    def __init__(self):
        self.data = ""
        self.pointer = null_pointer


def initialise_stack():
    stack = [node() for i in range(8)]
    top_of_stack = null_pointer
    free_list_ptr = 0
    for index in range(7):
        stack[index].pointer = index + 1
    stack[7].pointer = null_pointer
    return stack, top_of_stack, free_list_ptr


def push(stack, top_of_stack, free_list_ptr, new_item):
    if free_list_ptr != null_pointer:
        new_node_ptr = free_list_ptr
        stack[new_node_ptr].data = new_item
        free_list_ptr = stack[free_list_ptr].pointer
        stack[new_node_ptr],pointer = top_of_stack
        top_of_stack = new_node_ptr
    else:
        print("no space for more data")
    return stack, top_of_stack, free_list_ptr


def pop(stack, top_of_stack, free_list_ptr):
    if top_of_stack == null_pointer:
        print("no data on stack")
        value = ""
    else:
        value = stack[top_of_stack].data
        this_node_ptr = top_of_stack
        top_of_stack = stack[top_of_stack].pointer
        stack[this_node_ptr].pointer = free_list_ptr
        free_list_ptr = this_node_ptr
    return stack, top_of_stack, free_list_ptr, value


def output_all_nodes(stack, top_of_stack):
    current_node_ptr = top_of_stack
    if top_of_stack == null_pointer:
        print("No data on stack")
    while current_node_ptr != null_pointer:
        print(current_node_ptr, " ", stack[current_node_ptr].data)
        current_node_ptr = stack[current_node_ptr].pointer


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
        data = input("Enter the value:")
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
