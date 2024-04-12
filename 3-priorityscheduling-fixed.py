def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            if line != "":
                d = [a.replace('\n', '') for a in line.split(',')]
                # converting burst times from string to integer
                d[1] = int(d[1])
                # converting priority from string to integer
                d[2] = int(d[2])
                data.append(d)
            else:
                pass
    return data


def priority_scheduling(data):
    wt = []
    ft = []
    scheduled_processes = []

    for p in sorted(data, key=lambda x: x[2]):
        scheduled_processes.append(p)

    # calculating wait time and finish time for each process
    for i in range(len(scheduled_processes)):
        if i == 0:
            wt.append(0)
            ft.append(scheduled_processes[i][1] + 0)
        else:
            wt.append(ft[i - 1])
            ft.append(scheduled_processes[i][1] + wt[i])

    print("Processess | Burst Time  |  Start Time  |  End Time ")
    for i in range(len(data)):
        process = scheduled_processes[i]
        print(
            f"{process[0]}\t\t {process[1]}\t\t {wt[i]}\t\t {ft[i]}\t\t")

    print(f'Average waiting time: {sum(wt[:-1])/ len(data)}')
    print(f'Average turn around time: {sum(ft[:-1]) / len(data)}')


data = read_data('3-priorityscheduling-data.txt')

priority_scheduling(data)
