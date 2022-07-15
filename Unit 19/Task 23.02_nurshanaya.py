# Search/sort: Bubble Sort

MyList = []
for Index in range(7):
    MyList.append(int(input("Enter a number: ")))

MaxIndex = 6
n = MaxIndex
NoMoreSwaps = False

while NoMoreSwaps == False:
    NoMoreSwaps = True
    for j in range(n):
        if MyList[j] > MyList[j + 1]:
            Temp = MyList[j]
            MyList[j] = MyList[j + 1]
            MyList[j + 1] = Temp
            NoMoreSwaps = False
    n = n-1

for Index in range(7):
    print(MyList[Index])
