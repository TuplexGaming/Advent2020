def day13_data(test_case: bool):
    if test_case:
        earliest = 939
        busses = [7, 13, 'x', 'x', 59, 'x', 31, 19]
    else:
        earliest = 1008832
        busses = ('23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,'
                  + 'x,x,x,x,x,x,x,x,x,29,x,991,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17').split(',')
        busses = [int(x) if x != 'x' else 'x' for x in busses]
    return earliest, busses


def day13_1():
    earliest, busses = day13_data(test_case=False)
    active = [x for x in busses if x != 'x']
    first_bus = active[0]
    shortest_wait = (earliest // active[0] + 1) * active[0] - earliest
    for bus in active:
        wait = (earliest // bus + 1) * bus - earliest
        if wait < shortest_wait:
            first_bus = bus
            shortest_wait = wait

    return first_bus * shortest_wait


def day13_2():
    # Bus ID: 23 41 449 13 19 29 991 37 17
    # Offset:  0 13  23 41 42 52  54 60 71
    test_case = False
    earliest, bus_ids = day13_data(test_case)
    active = [x for x in bus_ids if x != 'x']
    busses = {}
    for bus in active:
        busses[bus] = bus_ids.index(bus)

    # The problem says that time t will be > 100000000000000
    # Only need to check every x time units, where x is bus ID with 0 offset (first in list)
    delta = active[0]
    if test_case:
        t0 = 0
    else:
        t0 = 100000000000000

    # Calculate first t > t0
    t = (t0 // delta + 1) * delta

    while True:
        for bus in busses:
            offset = busses[bus]
            if bus == active[0]:
                continue
            while True:
                dt = (t // bus + 1) * bus
                if dt - offset == t:
                    delta *= bus
                    break
                t += delta
        return t


print(day13_2())
