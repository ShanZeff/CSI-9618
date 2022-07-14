# Insertion Sort
List = [0, 53, 21, 60, 18, 42, 19]
NumberOfItems = 6

for Pointer in range(1, NumberOfItems + 1):
    print(List[Pointer], end='')
    print()


for Pointer in range(2, NumberOfItems + 1):
    ItemToBeInserted = List[Pointer]
    CurrentItem = Pointer - 1
    while List[CurrentItem] > ItemToBeInserted and CurrentItem > 0:
        List[CurrentItem + 1] = List[CurrentItem]
        CurrentItem = CurrentItem - 1
        List[CurrentItem + 1] = ItemToBeInserted


for Pointer in range(1, NumberOfItems + 1):
    print(List[Pointer], end=' ')
