SIZEs = 5
def CreateStack():
    global Stack, TopPointer
    Stack = ["" for i in range(SIZEs)]
    TopPointer = -1
def Push(NewItem):
    global Stack, TopPointer
    if TopPointer == SIZEs - 1:
        print("stack is full")
    else:
        TopPointer += 1
        Stack[TopPointer] = NewItem
        print(Stack)
def Pop():
    global Stack, TopPointer
    if TopPointer == -1:
        print("stack is empty")
    else:
        Popped = Stack[TopPointer]
        Stack[TopPointer] = ""
        print(f"{Popped} was popped from the stack")
        TopPointer -= 1


SIZEq = 10
def CreateQueue():
    global Queue, StartPointer, EndPointer
    Queue = [None for i in range(SIZEq)]
    StartPointer = 0
    EndPointer = 0
def Enqueue(NewData):
    global Queue, StartPointer, EndPointer
    if StartPointer == EndPointer and Queue[StartPointer] is not None:
        print("Queue is full")
    else:
        Queue[EndPointer] = NewData
        EndPointer += 1
        if EndPointer == SIZEq:
            EndPointer = 0
        print(f"{NewData} was added to the queue")
def Dequeue():
    global Queue, StartPointer, EndPointer
    if StartPointer == EndPointer and Queue[StartPointer] is None:
        print("Queue is empty")
    else:
        Removed = Queue[StartPointer]
        Queue[StartPointer] = None
        StartPointer += 1
        if StartPointer == SIZEq:
            StartPointer = 0
        print(f"{Removed} was removed from the queue")
