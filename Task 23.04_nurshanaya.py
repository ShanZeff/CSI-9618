Found = False
SearchFailed = False
First = 0
Last = MaxItems - 1     # set boundaries of search area

while not Found and not SearchFailed:
    Middle = (First + Last) / 2     # find middle of current search area
    if List[Middle] = SearchItem:
        Found = True
    else:
        if First >= Last: # no search area left
            SearchFailed = True
        else:
            if List[Middle] > SearhItem:
                Last = Middle - 1
            else:
                First = Middle + 1

if Found = True:
    print(Middle)
else:
    print("Item not present in array")