def FCFS(burstTime, arrivalTime):

    n = len(burstTime)

    process = []
    finishTime = []
    turnaroundTime = []
    waitingTime = []
    table = []
 
    AveTAT = 0
    AveWT = 0
    currentTime = 0
    checker = 0
    pCounter = 0

    for i in range(n):
        pCounter += 1
        process.append(pCounter)

    for i in arrivalTime:
        checker += i

    print(checker)

    if checker > 0:
        processes = sorted(zip(arrivalTime, burstTime, process))

        arrivalTime = [p[0] for p in processes]
        burstTime = [p[1] for p in processes]
        process = [p[2] for p in processes] 


    # Finish Time calculation
    for i in range(n):

        if currentTime < arrivalTime[i]:
           currentTime = arrivalTime[i]

        currentTime += burstTime[i]
        finishTime.append(currentTime)
    #print(finishTime)

    # Turnaround Time Calculation
    for i in range(n):

        turnaroundTime.append(finishTime[i] - arrivalTime[i])
    #print(turnaroundTime)

    # Waiting Time Calculation
    for i in range(n):

        waitingTime.append(turnaroundTime[i] - burstTime[i])
    #print(waitingTime)

    #Average Calculations
    sumTAT = 0
    sumWT = 0
    for i in range(n):

        sumTAT += turnaroundTime[i]
        sumWT += waitingTime[i]

    AveTAT = float(sumTAT)/n
    AveWT = float(sumWT)/n


    # Combining everything into a table
    for i in range(n):
        temp = []

        temp.append(process[i])
        temp.append(arrivalTime[i])
        temp.append(burstTime[i])
        temp.append(finishTime[i])
        temp.append(turnaroundTime[i])
        temp.append(waitingTime[i])

        table.append(temp)

    sorted_table = sorted(table)

    for i in sorted_table:
        print(i)

    print(f"Average TAT = {AveTAT}" )
    print(f"Average WT = {AveWT}")
        

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

