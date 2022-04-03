# Linear Search
MyList = []
for Index in range(7):
    MyList.append(int(input("Enter a number: ")))

MaxIndex = 6
SearchValue = int(input("Which value do you want to find? "))
Found = False
Index = -1

while not Found and Index < MaxIndex:
    Index += 1
    if MyList[Index] == SearchValue:
        Found = True
if Found:
    print("Value found at location: ", Index)
else:
    print("Value not found")

for Index in range(7):
    print(Index, " ", MyList[Index])