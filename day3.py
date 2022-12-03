from itertools import islice
# find the priority of the common item types
# lowercase: priority 1-26
# uppercase: priority 27-52


def priority(common):  # char to int
    pri = ord(common.lower()) - 96
    if common.isupper():
        pri += 26
    return pri


def check(rucksack):  # string to char
    size = len(rucksack)
    # print(size)
    l1 = int(size/2)
    r0 = int(size/2)
    r1 = size
    left = rucksack[0:l1]
    right = rucksack[r0:r1]
    # print(set(left))
    # print(set(right))
    c = set(left) & set(right)
    # print(c)
    for common in c:
        return common


def checkbadge(rucksacks):
    b = (set(rucksacks[0].strip('\n'))
         & set(rucksacks[1].strip('\n'))
         & set(rucksacks[2].strip('\n')))
    print(b)
    for badge in b:
        return badge


with open('./inputs/day3.txt', 'r') as input:
    priorities = 0
    for line in input:
        rucksack = line.strip('\n')
        # print(list(rucksack))
        # find letters (items) common to each part of the rucksack
        common = check(rucksack)
        priorities += priority(common)
    print(priorities)

with open('./inputs/day3.txt', 'r') as input:
    group_priorities = 0
    while True:
        lines = list(islice(input, 3))
        if not lines:
            print(group_priorities)
            break
        badge = checkbadge(lines)
        group_priorities += priority(badge)
