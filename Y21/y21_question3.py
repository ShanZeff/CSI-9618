QueueData = ["" for i in range(0, 20)]
StartPointer = 0
EndPointer = 0

def Enqueue(DataToAdd, QueueData, EndP):
    if EndP == 20:
        return False, EndP
    else:
        QueueData[EndP] = DataToAdd
        EndP = EndP + 1
        return True, EndP

