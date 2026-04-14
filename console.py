def calculation(burstTime, arrivalTime, isFCFS):

    n = len(burstTime)

    process = []
    finishTime = [0] * n
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

    # FCFS sorting (keep this)
    if checker > 0 and isFCFS:
        processes = sorted(zip(arrivalTime, process, burstTime))
        arrivalTime = [p[0] for p in processes]
        process = [p[1] for p in processes]
        burstTime = [p[2] for p in processes]

    # -------------------------------
    # FINISH TIME CALCULATION
    # -------------------------------
    if isFCFS:
        for i in range(n):
            if currentTime < arrivalTime[i]:
                currentTime = arrivalTime[i]

            currentTime += burstTime[i]
            finishTime[i] = currentTime

    else:
        # ✅ Correct SJF (non-preemptive)
        visited = [False] * n
        completed = 0

        while completed < n:
            idx = -1
            min_bt = float('inf')

            for i in range(n):
                if (arrivalTime[i] <= currentTime and 
                    not visited[i] and 
                    burstTime[i] < min_bt):
                    min_bt = burstTime[i]
                    idx = i

            # If no process has arrived yet
            if idx == -1:
                currentTime += 1
                continue

            currentTime += burstTime[idx]
            finishTime[idx] = currentTime
            visited[idx] = True
            completed += 1

    # -------------------------------
    # TURNAROUND TIME
    # -------------------------------
    for i in range(n):
        turnaroundTime.append(finishTime[i] - arrivalTime[i])

    # -------------------------------
    # WAITING TIME
    # -------------------------------
    for i in range(n):
        waitingTime.append(turnaroundTime[i] - burstTime[i])

    # -------------------------------
    # AVERAGES
    # -------------------------------
    sumTAT = sum(turnaroundTime)
    sumWT = sum(waitingTime)

    AveTAT = sumTAT / n
    AveWT = sumWT / n

    # -------------------------------
    # TABLE
    # -------------------------------
    for i in range(n):
        temp = []
        temp.append(process[i])
        temp.append(arrivalTime[i])
        temp.append(burstTime[i])
        temp.append(finishTime[i])
        temp.append(turnaroundTime[i])
        temp.append(waitingTime[i])
        table.append(temp)

    return table