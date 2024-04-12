def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = [a.replace('\n', '') for a in line.split(',')]
            d[1] = int(d[1])  # converting burst times from string to integer
            data.append(d)
    return data


def round_robin(data):
    q = 4
    wt = []
    tat = []
    scheduled_processes = data
    remaining_bt = [d[1] for d in data]
    chart = []

    currt = 0
    while(1):
        finished = True
        for i in range(len(remaining_bt)):

            if remaining_bt[i] == 0:
                pass
            elif remaining_bt[i] > q:
                finished = False
                chart.append([scheduled_processes[i][0],
                              remaining_bt[i], currt, currt + q])
                currt += q
                remaining_bt[i] -= q
            else:
                chart.append(
                    [scheduled_processes[i][0], remaining_bt[i], currt, currt + remaining_bt[i]])
                wt.append(currt)
                currt += remaining_bt[i]
                remaining_bt[i] = 0

        if (finished == True):
            break

    # calculating turn around time
    for i in range(len(data)):
        tat.append(scheduled_processes[i][1] + wt[i])

    print("Processess | Burst Time  |  Start Time  |  End Time ")
    for p in chart:
        print(
            f"{p[0]}\t\t {p[1]}\t\t {p[2]}\t\t {p[3]}\t\t")

    print(f'Average waiting time: {sum(wt[:-1])/ len(scheduled_processes)}')
    print(
        f'Average turn around time: {sum(tat[:-1]) / len(scheduled_processes)}')


data = read_data("4-roundrobin-data.txt")
round_robin(data)
