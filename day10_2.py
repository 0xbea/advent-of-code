cycle = 1
X = 1
screen = ''


def draw():
    global cycle, X, screen
    CRT_pos = (cycle - 1) % 40  # 0 - 39
    sprite_pos = [X-1, X, X+1]
    # print(sprite_pos)
    if CRT_pos in sprite_pos:
        screen += '#'
    else:
        screen += '.'
    if cycle % 40 == 0:
        print(screen)
        screen = ''


def execute(command, value):
    global cycle, X
    match command:
        case 'noop':
            # begin execution and do nothing
            draw()
            cycle += 1  # finish and move onto next cycle
        case 'addx':
            value = int(value)
            # begin execution at start of current cycle
            draw()
            cycle += 1  # move onto next cycle
            # finish during this cycle
            draw()
            cycle += 1
            X += int(value)


with open('./inputs/day10.txt', 'r') as input:
    for line in input:
        line = line.strip('\n').split()
        if line[0] == 'noop':
            line.append('0')
        execute(line[0], line[1])
