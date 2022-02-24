null_pointer = -1


class ListNode:
    def __init__(self):
        self.data = ""
        self.pointer = null_pointer


def initialise_list():
    list = [ListNode() for i in range(8)]
    start_pointer = null_pointer
    free_list_ptr = 0
    for Index in range(7):
        list[Index].pointer = Index + 1
    list[7].pointer = null_pointer
    return list, start_pointer, free_list_ptr


def insert_node(list, start_pointer, free_list_ptr, new_item):
    if free_list_ptr != null_pointer:
        new_node_ptr = free_list_ptr
        list[new_node_ptr].data = new_item
        free_list_ptr = list[free_list_ptr].pointer
        previous_node_ptr = null_pointer
        this_node_ptr = start_pointer
        while this_node_ptr != null_pointer and list[this_node_ptr].data < new_item:
            previous_node_ptr = this_node_ptr
            this_node_ptr = list[this_node_ptr].pointer
        if previous_node_ptr == null_pointer:
            list[new_node_ptr].pointer = start_pointer
            start_pointer = new_node_ptr
        else:
            list[new_node_ptr].pointer = list[previous_node_ptr].pointer
            list[previous_node_ptr].pointer = new_node_ptr
    else:
        print("no space for more data")
    return list, start_pointer, free_list_ptr


def find_node(list, start_pointer, data_item):
    current_node_ptr = start_pointer
    while current_node_ptr != null_pointer and list[current_node_ptr].data != data_item:
        current_node_ptr = list[current_node_ptr].pointer
    return current_node_ptr


def delete_node(list, start_pointer, free_list_ptr, data_item):
    this_node_ptr = start_pointer
    while this_node_ptr != null_pointer and list[this_node_ptr].data_item:
        previous_node_ptr = this_node_ptr
        this_node_ptr = list[this_node_ptr].pointer
    if this_node_ptr != null_pointer:
        if this_node_ptr == start_pointer:
            start_pointer == list[start_pointer].pointer
        else:
            list[previous_node_ptr].pointer = list[this_node_ptr].pointer
        list[this_node_ptr].pointer = free_list_ptr
        free_list_ptr = this_node_ptr
    else:
        print("data does not exist in list")
    return list, start_pointer, free_list_ptr


def output_all_nodes(list, start_pointer):
    current_node_ptr = start_pointer
    if start_pointer == null_pointer:
        print("no data in list")
    while current_node_ptr != null_pointer:
        print(current_node_ptr, " ", list[current_node_ptr].data)
        current_node_ptr = list[current_node_ptr].pointer


def get_option():
    print("1: insert a value")
    print("2: delete a value")
    print("3: find a value")
    print("4: output list")
    print("5: end program")
    option = input("Enter your choice: ")
    return option
list, start_pointer, free_list_ptr = initialise_list()

option = get_option()
while option != "5":
    if option == "1":
        data = input("Enter the value: ")
        list, start_pointer, free_list_ptr = insert_node(list, start_pointer, free_list_ptr, data)
        output_all_nodes(list, start_pointer)
    elif option == "2":
        data = input("Enter the value: ")
        list, start_pointer, free_list_ptr = delete_node(list, start_pointer, free_list_ptr, data)
        output_all_nodes(list, start_pointer)
    elif option == "3":
        data = input("Enter the value: ")
        current_node_ptr = find_node(list, start_pointer, data)
        if current_node_ptr == null_pointer:
            print("data not found")
        print(start_pointer, free_list_ptr)
        for i in range(8):
            print(i, " ", list[i].data, " ", list[i].pointer)
    elif option == "4":
        output_all_nodes(list, start_pointer)
    option = get_option()