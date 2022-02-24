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
