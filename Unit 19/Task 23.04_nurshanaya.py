# Search/sort: Binary Search

MyList = [7, 12, 19, 23, 27, 33, 37, 41, 45, 56, 59, 60, 62, 71, 75, 80, 84, 88, 92, 99]
MaxItems = 20
First = 0
Last = MaxItems - 1     # set boundaries of search area
Found = False
SearchFailed = False
SearchItem = int(input("Please input item to be found: "))


while not Found and not SearchFailed:
    Index = int((First + Last) / 2)     # find middle of current search area
    if MyList[Index] == SearchItem:
        Found = True
    else:
        if First >= Last:   # no search area left
            SearchFailed = True
        else:
            if MyList[Index] > SearchItem:
                Last = Index - 1    # move upper boundary
            else:
                First = Index + 1   # move lower boundary


if Found == True:
    print("Item found at position:", Index)
else:
    print("Item not present in array.")
