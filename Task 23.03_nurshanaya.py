NumberOfItems = 6
List = [0]
List.append(53)
List.append(21)
List.append(60)
List.append(18)
List.append(42)
List.append(19)

for Pointer in range(1, NumberOfItems + 1):
    print(List[Pointer], end=' ')
print();

for Pointer in range(2, NumberOfItems + 1):
    ItemToBeInserted = List[Pointer]
    CurrentItem = Pointer -1
    while (List[CurrentItem] > ItemToBeInserted) and (CurrentItem > 0):
        List[CurrentItem + 1] = List[CurrentItem]
        CurrentItem = CurrentItem - 1
        List[CurrentItem + 1] = ItemToBeInserted

for Pointer in range(1, NumberOfItems + 1):
    print(List[Pointer], end=' ')