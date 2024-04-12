def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = [a.replace('\n', '') for a in line.split(',')]
            d[1] = int(d[1])  # converting burst times from string to integer
            data.append(d)
    return data
# a function to read and return the data from txt files


def fcfs(data):
    wt = []  # wait time
    tat = []  # turn around time

    # calculating wait time
    for i in range(len(data)):
        if i == 0:
            # wait time for process 1 will be zero (as first proccess in need not wait )
            wt.append(0)
        else:
            lbt = data[i - 1][1]  # getting the last burst time
            # adding the last burst time to the last wait time to find current wait time
            wt.append(lbt + wt[i - 1])

    # calculating turn around time
    for i in range(len(data)):
        tat.append(data[i][1] + wt[i])

    print("Process | Burst Time |  Start Time | End Time")
    for i in range(len(data)):
        print(
            f"{data[i][0]}\t    {data[i][1]}\t\t {wt[i]}\t\t{tat[i]}\t\t")

    print(f'Average waiting time: {sum(wt)/ len(data)}')
    print(f'Average turn around time: {sum(tat) / len(data)}')


data1 = read_data('1-fcfs-data.txt')
fcfs(data1)
