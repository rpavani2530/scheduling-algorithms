def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = [a.replace('\n', '') for a in line.split(',')]
            d[1] = int(d[1])  # converting burst times from string to integer
            data.append(d)
    return data


def round_robin(data, currt):
    wt = []
    q = 2
    scheduled_processes_rr = data
    remaining_bt = [d[1] for d in scheduled_processes_rr]
    chart_pl = []

    while(1):
        finished = True
        for i in range(len(remaining_bt)):
            if len(data) == 1 or 0 in remaining_bt:
                chart_pl.append(
                    [scheduled_processes_rr[i][0], remaining_bt[i], currt, currt + remaining_bt[i]])
                wt.append(currt)
                currt += remaining_bt[i]
                remaining_bt[i] = 0

            if remaining_bt[i] == 0:
                pass
            elif remaining_bt[i] > q:
                finished = False
                chart_pl.append([scheduled_processes_rr[i][0],
                                 remaining_bt[i], currt, currt + q])
                currt += q
                remaining_bt[i] -= q
            else:
                chart_pl.append(
                    [scheduled_processes_rr[i][0], remaining_bt[i], currt, currt + remaining_bt[i]])
                wt.append(currt)
                currt += remaining_bt[i]
                remaining_bt[i] = 0

        if (finished == True):
            break
    return [chart_pl, currt, wt]


def priority_with_rr(data):

    q = 2
    wt = []
    tat = []
    #
    scheduled_processes = sorted(data, key=lambda x: x[2])
    # remaining_bt = [d[1] for d in scheduled_processes]
    chart = []
    rr_list = []  # list to track processes that will go round robin
    proccess_dict = {}

    for i in range(len(scheduled_processes)):
        with_rr = False
        for j in range(len(scheduled_processes)):
            if j == i:
                pass

            else:
                if scheduled_processes[i][2] == scheduled_processes[j][2]:
                    with_rr = True
                else:
                    pass
        if with_rr:
            rr_list.append(scheduled_processes[i][0])

    for p in scheduled_processes:
        if p[2] in proccess_dict:
            proccess_dict[p[2]].append(p)
        else:
            proccess_dict[p[2]] = []
            proccess_dict[p[2]].append(p)
    # print(proccess_dict)

    currt_now = 0
    for pl in proccess_dict:
        rr_data = round_robin(proccess_dict[pl], currt_now)
        for rr_point in rr_data[0]:
            chart.append(rr_point)
        currt_now = rr_data[1]

        for wt_rr in rr_data[2]:
            wt.append(wt_rr)

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


data = read_data("5-prioritywithrr-data.txt")
priority_with_rr(data)
