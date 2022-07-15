# Search/sort: Binary Search

Found = False
SearchFailed = False
List = [7, 12, 19, 23, 27, 33, 37, 41, 45, 56, 59, 60, 62, 71, 75, 80, 84, 88, 92, 99]
MaxItems = 20
First = 0
Last = MaxItems - 1     # set boundaries of search area
SearchItem = int(input("What number are you searching for?: "))


while not Found and not SearchFailed:
    Middle = int((First + Last) / 2)     # find middle of current search area
    if List[Middle] == SearchItem:
        Found = True
    else:
        if First >= Last: # no search area left
            SearchFailed = True
        else:
            if List[Middle] > SearchItem:
                Last = Middle - 1
            else:
                First = Middle + 1

if Found == True:
    print(Middle)
else:
    print("Item not present in array")
