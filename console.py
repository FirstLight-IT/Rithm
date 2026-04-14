def calculation(burstTime, arrivalTime, isFCFS):

    n = len(burstTime)

    process = []
    finishTime = [0] * n
    turnaroundTime = [0] * n
    waitingTime = [0] * n
    table = []
 
    currentTime = 0
    pCounter = 0

    for i in range(n):
        pCounter += 1
        process.append(pCounter)

    # FCFS sorting
    if isFCFS:
        processes = sorted(zip(arrivalTime, process, burstTime))
        # Unpack sorted values
        arr_sorted = [p[0] for p in processes]
        proc_sorted = [p[1] for p in processes]
        burst_sorted = [p[2] for p in processes]

        for i in range(n):
            if currentTime < arr_sorted[i]:
                currentTime = arr_sorted[i]

            currentTime += burst_sorted[i]
            ft = currentTime
            tat = ft - arr_sorted[i]
            wt = tat - burst_sorted[i]
            
            # Append to table in execution order
            table.append([proc_sorted[i], arr_sorted[i], burst_sorted[i], ft, tat, wt])

    else:
        # SJF (non-preemptive)
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

            if idx == -1:
                currentTime += 1
                continue

            currentTime += burstTime[idx]
            ft = currentTime
            tat = ft - arrivalTime[idx]
            wt = tat - burstTime[idx]
            
            # Append to table in execution order (Fixes the Gantt Chart)
            table.append([process[idx], arrivalTime[idx], burstTime[idx], ft, tat, wt])
            
            visited[idx] = True
            completed += 1

    return table