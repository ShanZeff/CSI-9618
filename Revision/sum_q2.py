# Summer 21 Q2
# Search/sort: Linear search, bubble sort -Finished

ArrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def LinearSearch(SearchValue):
    for x in range(0, 10):
        if ArrayData[x] == SearchValue:
            return True
    return False


def BubbleSort():
    for x in range(0, 10):
        for y in range(0, 9):
            if TheArray[y] < TheArray[y+1]:
                Temp = TheArray[y]
                TheArray[y] = TheArray[y+1]
                TheArray[y+1] = Temp


def main():
    SearchValue = int(input("Enter the number to search for: "))
    ReturnValue = LinearSearch(SearchValue)
    if ReturnValue == True:
        print("It was found")
    else:
        print("It was not found")


main()
