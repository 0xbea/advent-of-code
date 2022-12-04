import re


def fc(left, right):  # strings => Boolean
    [start0, end0] = left.split('-')
    [start1, end1] = right.split('-')
    start0 = int(start0)
    end0 = int(end0)
    start1 = int(start1)
    end1 = int(end1)
    if (start0 >= start1 and end0 <= end1):
        return True
    elif (start1 >= start0 and end1 <= end0):
        return True
    else:
        return False


def overlap(left, right):  # not fully contained but overlap
    [start0, end0] = left.split('-')
    [start1, end1] = right.split('-')
    start0 = int(start0)
    end0 = int(end0)
    start1 = int(start1)
    end1 = int(end1)
    # left end overlap with right start
    if (start0 < start1 and end0 >= start1):
        return True
    # right end overlap with left start
    elif (start1 < start0 and end1 >= start0):
        return True
    else:
        return False


# start0-end0,start1-end1
with open('./inputs/day4.txt', 'r') as input:
    FCs = 0
    overlaps = 0
    for line in input:
        [left, right] = line.split(',')
        if fc(left, right):
            FCs += 1
            overlaps += 1
        else:
            overlaps += overlap(left, right)
    print(FCs)
    print(overlaps)
