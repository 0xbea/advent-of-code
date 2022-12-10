cycle = 1
X = 1
signalSum = 0


def cycleCheck():
    global cycle, X, signalSum
    if cycle in [20, 60, 100, 140, 180, 220]:
        signalStrength = cycle * X
        signalSum += signalStrength
    if cycle == 221:
        print(signalSum)


def execute(command, value):
    global cycle, X
    match command:
        case 'noop':
            # begin execution and do nothing
            cycleCheck()
            cycle += 1  # finish and move onto next cycle
        case 'addx':
            # begin execution at start of current cycle
            cycleCheck()
            cycle += 1  # move onto next cycle
            # finish during this cycle
            cycleCheck()
            cycle += 1
            X += int(value)  # set value after th cycle finish


with open('./inputs/day10.txt', 'r') as input:
    for line in input:
        line = line.strip('\n').split()
        if line[0] == 'noop':
            line.append('0')
        execute(line[0], line[1])
