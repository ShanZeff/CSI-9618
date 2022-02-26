# Linked list

# NullPointer should be set to -1 if using array element with index 0
null_pointer = -1


# Declare record type to store data and pointer
class ListNode:
    def __init__(self):
        self.data = ""
        self.pointer = null_pointer


def initialise_list():
    list = [ListNode() for i in range(8)]
    start_pointer = null_pointer    # set start pointer
    free_list_ptr = 0               # set starting position of free list
    for Index in range(7):          # link all nodes to make free list
        list[Index].pointer = Index + 1
    list[7].pointer = null_pointer  # last node of free list
    return list, start_pointer, free_list_ptr


def insert_node(list, start_pointer, free_list_ptr, new_item):
    if free_list_ptr != null_pointer:
        # there is space in the array
        # take node from free list and store data item
        new_node_ptr = free_list_ptr
        list[new_node_ptr].data = new_item
        free_list_ptr = list[free_list_ptr].pointer
        # find insertion point
        previous_node_ptr = null_pointer
        this_node_ptr = start_pointer   # start at beginning of list
        while this_node_ptr != null_pointer and list[this_node_ptr].data < new_item:

            # while not end of list
            previous_node_ptr = this_node_ptr   # remember this node
            # follow the pointer to the next node
            this_node_ptr = list[this_node_ptr].pointer

        if previous_node_ptr == null_pointer:
            # insert new node at start of list
            list[new_node_ptr].pointer = start_pointer
            start_pointer = new_node_ptr
        else:   # insert new node between previous node and this node
            list[new_node_ptr].pointer = list[previous_node_ptr].pointer
            list[previous_node_ptr].pointer = new_node_ptr
    else:
        print("no space for more data")
    return list, start_pointer, free_list_ptr


def find_node(list, start_pointer, data_item):  # returns pointer to node
    current_node_ptr = start_pointer    # start at beginning of list
    while current_node_ptr != null_pointer and list[current_node_ptr].data != data_item:
        # not end of list, item not found
        # follow the pointer to the next node
        current_node_ptr = list[current_node_ptr].pointer
    return current_node_ptr     # return NullPointer if item not found


def delete_node(list, start_pointer, free_list_ptr, data_item):
    this_node_ptr = start_pointer       # start at beginning of list
    while this_node_ptr != null_pointer and list[this_node_ptr].data != data_item:
        # while not end of list and item not found
        previous_node_ptr = this_node_ptr   # remember this node
        # follow the pointer to the next node
        this_node_ptr = list[this_node_ptr].pointer
    if this_node_ptr != null_pointer:       # node exists in list
        if this_node_ptr == start_pointer:  # first node to be deleted
            start_pointer == list[start_pointer].pointer
        else:
            list[previous_node_ptr].pointer = list[this_node_ptr].pointer
        list[this_node_ptr].pointer = free_list_ptr
        free_list_ptr = this_node_ptr
    else:
        print("data does not exist in list")
    return list, start_pointer, free_list_ptr


def output_all_nodes(list, start_pointer):
    current_node_ptr = start_pointer    # start at beginning of list
    if start_pointer == null_pointer:
        print("No data in list")
    while current_node_ptr != null_pointer:     # while not end of list
        print(current_node_ptr, " ", list[current_node_ptr].data)
        # follow the pointer to the next node
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
