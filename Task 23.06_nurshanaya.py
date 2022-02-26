# Binary Search Tree

# NullPointer should be set to -1 if using array element with index 0
null_pointer = -1


# Declare record type to store data and pointer
class TreeNode:
    def __init__(self):
        self.data = ""
        self.left_pointer = null_pointer
        self.right_pointer = null_pointer


def initialise_tree():
    tree = [TreeNode() for i in range(8)]
    root_pointer = null_pointer
    free_ptr = 0
    for index in range(7):
        tree[index].left_pointer = index + 1
    return tree, root_pointer, free_ptr


def insert_node(tree, root_pointer, free_ptr, new_item):
    if free_ptr != null_pointer:
        new_node_ptr = free_ptr
        tree[new_node_ptr].data = new_item
        free_ptr = tree[free_ptr].left_pointer
        tree[new_node_ptr].data = new_item
        free_ptr = tree[free_ptr].left_pointer
        tree[new_node_ptr].left_pointer = null_pointer
        if root_pointer == null_pointer:
            root_pointer = new_node_ptr
        else:
            this_node_ptr = root_pointer
            while this_node_ptr != null_pointer:
                previous_node_ptr = this_node_ptr
                if tree[this_node_ptr].data > new_item:
                    turned_left = True
                    this_node_ptr = tree[this_node_ptr].left_pointer
                else:
                    turned_left = False
                    this_node_ptr = tree[this_node_ptr].right_pointer
                if turned_left:
                    tree[previous_node_ptr].left_pointer = new_node_ptr
                else:
                    tree[previous_node_ptr].right_pointer = new_node_ptr
    else:
        print("no space for more data")
    return tree, root_pointer, free_ptr


def find_node(tree, root_pointer, search_item):
    this_node_ptr = root_pointer
    while this_node_ptr != null_pointer and tree[this_node_ptr].data != search_item:
        if tree[this_node_ptr].data > search_item:
            this_node_ptr = tree[this_node_ptr].left_pointer
        else:
            this_node_ptr = tree[this_node_ptr].right_pointer
    return this_node_ptr


def traverse_tree(tree, root_pointer):
    if root_pointer != null_pointer:
        traverse_tree(tree, tree[root_pointer].left_pointer)
        print(tree[root_pointer].data)
        traverse_tree(tree, tree[root_pointer].right_pointer)
