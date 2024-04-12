def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = [a.replace('\n', '') for a in line.split(',')]
            d[1] = int(d[1])  # converting burst times from string to integer
            data.append(d)
    return data


def sjf(data):
    wt = []  # wait time
    ft = []  # turn around time

    scheduled_processes = []

    # sorting the processes (data) based on the second element in list (burst time)
    for p in sorted(data, key=lambda x: x[1]):
        scheduled_processes.append(p)

    # calculating wait time and finish time for each process
    for i in range(len(scheduled_processes)):
        if i == 0:
            wt.append(0)
            ft.append(scheduled_processes[i][1] + 0)
        else:
            wt.append(ft[i - 1])
            ft.append(scheduled_processes[i][1] + wt[i])

    print("Process  |  Burst Time  |  Start Time  |  End Time ")
    for i in range(len(data)):
        print(
            f"{scheduled_processes[i][0]}\t\t {scheduled_processes[i][1]}\t\t {wt[i]}\t {ft[i]}\t")

    print(f'Average waiting time: {sum(wt)/ len(data)}')
    print(f'Average turn around time: {sum(ft) / len(data)}')


data = read_data('2-sjf-data.txt')
sjf(data)
