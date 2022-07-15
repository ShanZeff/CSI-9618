# ADT: Queue

# NullPointer should be set to -1 if using array element with index 0
EmptyString = ""
NullPointer = -1
MaxQueueSize = 8


def InitialiseQueue():
    Queue = [EmptyString for i in range(MaxQueueSize)]
    FrontOfQueue = NullPointer
    EndOfQueue = NullPointer
    NumberInQueue = 0
    return Queue, FrontOfQueue, EndOfQueue, NumberInQueue


def AddToQueue(Queue, FrontOfQueue, EndOfQueue, NumberInQueue, NewItem):
    if NumberInQueue == 0:      # first item?
        FrontOfQueue = 0

    if NumberInQueue < MaxQueueSize:
        # there is space in the array
        # increment end of queue pointer
        EndOfQueue += 1

        # check for wrap-round
        if EndOfQueue > MaxQueueSize - 1:
            EndOfQueue = 0
        Queue[EndOfQueue] = NewItem
        # increment counter
        NumberInQueue += 1
    else:
        print("No space for more data")
    return Queue, FrontOfQueue, EndOfQueue, NumberInQueue


def RemoveFromQueue(Queue, FrontOfQueue, EndOfQueue, NumberInQueue):
    Item = EmptyString
    if NumberInQueue > 0:       # not an empty queue
        Item = Queue[FrontOfQueue]
        NumberInQueue -= 1
        # if queue now empty, reset front and end pointers
        if NumberInQueue == 0:
            FrontOfQueue = NullPointer
            EndOfQueue = NullPointer
        else:
            # increment front of queue pointer
            FrontOfQueue += 1
            # check for wrap-round
            if FrontOfQueue > MaxQueueSize - 1:
                FrontOfQueue = 0
    else:
        print("Queue empty")
    return Queue, FrontOfQueue, EndOfQueue, NumberInQueue, Item


def OutputQueue(Queue, FrontOfQueue, NumberInQueue):
    CurrentItem = FrontOfQueue      # start at beginning of queue
    if NumberInQueue == 0:
        print("No data in queue")
    else:
        for Count in range(NumberInQueue):
            print(CurrentItem, " ", Queue[CurrentItem])
            # move to next item in queue
            CurrentItem += 1
            # check for wrap-round
            if CurrentItem > MaxQueueSize - 1:
                CurrentItem = 0


def GetOption():
    print("1: join queue")
    print("2: leave queue")
    print("3: output queue")
    print("4: end program")
    Option = input("Enter your choice: ")
    return Option


def main():
    Queue, FrontOfQueue, EndOfQueue, NumberInQueue = InitialiseQueue()

    Option = GetOption()
    while Option != "4":
        if Option == "1":
            Data = input("Enter the value: ")
            Queue, FrontOfQueue, EndOfQueue, NumberInQueue = AddToQueue(Queue, FrontOfQueue, EndOfQueue, NumberInQueue, Data)
            OutputQueue(Queue, FrontOfQueue, NumberInQueue)
        elif Option == "2":
            Queue, FrontOfQueue, EndOfQueue, NumberInQueue, Item = RemoveFromQueue(Queue, FrontOfQueue, EndOfQueue, NumberInQueue)
            print("data leaving queue: ", Item)
            OutputQueue(Queue, FrontOfQueue, NumberInQueue)
        elif Option == "3":
            OutputQueue(Queue, FrontOfQueue, NumberInQueue)
            print(FrontOfQueue, EndOfQueue, NumberInQueue)
            for i in range(MaxQueueSize):
                print(i, " ", Queue[i])
        Option = GetOption()


main()
