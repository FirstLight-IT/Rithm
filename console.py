import numpy as np

def FCFS(burstTime, arrivalTime):

    #n = len(burstTime)
    finishTime = [0]
    currentTime = 0

    processes = sorted(zip(arrivalTime, burstTime))

    arrivalTime = [p[0] for p in processes]
    burstTime = [p[1] for p in processes]

    print(burstTime)

    for i in range(len(burstTime)):

        if currentTime < arrivalTime[i]:
            currentTime = arrivalTime[i]

        currentTime += burstTime[i]
        finishTime.append(currentTime)
    
    print(finishTime)



def SJF(burstTime, arrivalTime):

    burstTime.sort()

    finishTime = [0]
    currentTime = 0

    for i in burstTime:

        currentTime = currentTime + i
        finishTime.append(currentTime)
    
    print(finishTime)

#---------------------------------------------------------------------------------------------------------------

burstTime = input("Enter the Burst Time | ").strip()
arrivalTime = input("Enter the Arrival Time | ").strip()

burstTime = burstTime.split(" ")
arrivalTime = arrivalTime.split(" ")

BTime = []
ATime = []

for b in burstTime:
    b = int(b)
    BTime.append(b)

for a in arrivalTime:
    a = int(a)
    ATime.append(a)


FCFS(BTime, ATime)
#SJF(BTime, ATime)






