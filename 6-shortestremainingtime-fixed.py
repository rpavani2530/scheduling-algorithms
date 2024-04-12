def read_data(filename):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        data = []
        for line in lines:
            d = [a.replace('\n', '') for a in line.split(',')]
            # d[0] = int(d[0])
            d[1] = int(d[1])  # converting arrival time from string to integer
            d[2] = int(d[2])  # converting burst times from string to integer
            data.append(d)
    return data


def shortest_remaining_time_first(data):
    wt = 0
    scheduled_processes = sorted(data, key=lambda x: x[1])
    remaining_time_processes = scheduled_processes
    chart = []
    currt = 0

    # the first second fires and takes off 1 from the bt for p1
    chart.append([scheduled_processes[0][0], scheduled_processes[0][2], 0, 1])
    currt += 1
    remaining_time_processes[0][2] -= 1

    scheduled_processes = sorted(data, key=lambda x: x[2])

    for process in sorted(remaining_time_processes, key=lambda x: x[2]):
        chart.append(
            [process[0], process[2], currt, currt + process[2]])
        currt += process[2]

    # wt = final time
    wt += currt
    # Display processes along with all details

    print("Processess | Burst Time  |  Start Time  |  End Time ")
    for p in chart:
        print(
            f"{p[0]}\t\t {p[1]}\t\t {p[2]}\t\t {p[3]}\t\t")

    print(f"\nAverage waiting time = {wt/len(data)}")


data = read_data('6-shortestremainingtime-data.txt')
shortest_remaining_time_first(data)
