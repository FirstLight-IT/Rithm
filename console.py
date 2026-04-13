import numpy as np

def FCFS(burstTime, arrivalTime):

    n = len(burstTime)
    finishTime = []
    turnaroundTime = []
    waitingTime = []

    AveTAT = 0
    AveWT = 0
    currentTime = 0
    checker = 0

    for i in arrivalTime:
        checker += i

    if checker > 0:
        processes = sorted(zip(arrivalTime, burstTime))

        arrivalTime = [p[0] for p in processes]
        burstTime = [p[1] for p in processes]


    # Finish Time calculation
    for i in range(n):

        if currentTime < arrivalTime[i]:
            currentTime = arrivalTime[i]

        currentTime += burstTime[i]
        finishTime.append(currentTime)
    print(finishTime)

    # Turnaround Time Calculation
    for i in range(n):

        turnaroundTime.append(finishTime[i] - arrivalTime[i])
    print(turnaroundTime)

    # Waiting Time Calculation
    for i in range(n):

        waitingTime.append(turnaroundTime[i] - burstTime[i])
    print(waitingTime)

    #Average Calculations
    sumTAT = 0
    sumWT = 0
    for i in range(n):

        sumTAT += turnaroundTime[i]
        sumWT += waitingTime[i]

    AveTAT = float(sumTAT)/n
    AveWT = float(sumWT)/n

    print(f"Average TAT = {AveTAT}" )
    print(f"Average WT = {AveWT}")
        

    # Combining everything into a table





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






