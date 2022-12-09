# tail must always be under head, adjacent or diagonal

# array of tuples. list of DISTINCT positions the tail has been [(1,1), (1,2)]
tail_pos_tracker = [(0, 0)]
tail_pos_dict = {}
tail_length = 10  # actually this is the length of the whole thing

# generate initial snake
for i in range(tail_length):
    tail_pos_dict[i] = (0, 0)
    i += 1
print(tail_pos_dict)


def moveHeadTail(dir, times):  # str, int
    i = 0
    while i < times:
        j = 0
        global tail_length
        while j < (tail_length - 1):  # less than number of knots in tail
            global tail_pos_dict
            # print(head_pos, tail_pos)
            x_head = tail_pos_dict[j][0]
            y_head = tail_pos_dict[j][1]
            match dir:
                case 'U':
                    tail_pos_dict[j] = (x_head, y_head + 1)
                case 'D':
                    tail_pos_dict[j] = (x_head, y_head - 1)
                case 'L':
                    tail_pos_dict[j] = (x_head - 1, y_head)
                case 'R':
                    tail_pos_dict[j] = (x_head + 1, y_head)
                # calculate distance and move tail if needed
            # tail_pos_dict[j] = head_pos  # update head pos
            dist(j)
            j += 1
        print(tail_pos_dict)
        # add position of last knot to positions tracker
        if tail_pos_dict[tail_length - 1] not in tail_pos_tracker:
            tail_pos_tracker.append(tail_pos_dict[tail_length - 1])
        i += 1


def dist(j):
    global tail_pos_dict
    # head_pos = tail_pos_dict[j]
    # tail = tail_pos_dict[j+1]
    x_head = tail_pos_dict[j][0]
    y_head = tail_pos_dict[j][1]
    x_tail = tail_pos_dict[j+1][0]
    y_tail = tail_pos_dict[j+1][1]
    x_diff = x_head - x_tail
    y_diff = y_head - y_tail
    if not (abs(x_diff) <= 1 and abs(y_diff) <= 1):
        shiftTail(j)


def shiftTail(j):
    global tail_pos_dict
    tail_num = j+1
    # head_pos = tail_pos_dict[j]
    tail_pos = tail_pos_dict[tail_num]
    x_head = tail_pos_dict[j+1][0]
    y_head = tail_pos_dict[j+1][1]
    x_tail = tail_pos_dict[tail_num][0]
    y_tail = tail_pos_dict[tail_num][1]
    x_diff = x_head - x_tail
    y_diff = y_head - y_tail
    # when to shift up or down
    if (x_head == x_tail):
        if y_diff > 0:
            tail_pos = (x_tail, y_tail + 1)
        elif y_diff < 0:
            tail_pos = (x_tail, y_tail - 1)
    # when to shift left or right
    elif (y_head == y_tail):
        if x_diff > 0:
            tail_pos = (x_tail + 1, y_tail)
        elif x_diff < 0:
            tail_pos = (x_tail - 1, y_tail)
    # when to shift digaonal
    else:
        # shif diagonal right up or down
        if x_diff > 0:
            if y_diff > 0:
                tail_pos = (x_tail + 1, y_tail + 1)
            elif y_diff < 0:
                tail_pos = (x_tail + 1, y_tail - 1)
        # shif diagonal left up or down
        elif x_diff < 0:
            if y_diff > 0:
                tail_pos = (x_tail - 1, y_tail + 1)
            elif y_diff < 0:
                tail_pos = (x_tail - 1, y_tail - 1)
    # update the global var
    tail_pos_dict[tail_num] = tail_pos


with open('./inputs/day9_ex2.txt', 'r') as input:
    for line in input:
        line = line.strip('\n').split()
        # print(line)
        moveHeadTail(line[0], int(line[1]))

print(tail_pos_tracker)
print(len(tail_pos_tracker))  # how many distinct positions
