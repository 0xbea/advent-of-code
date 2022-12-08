forest = {}
num_trees = 0
length = 0
height = 0

# generate forest as dict of arrays
# forest coordinates [(0-98),(0-98)]
with open('./inputs/day8.txt', 'r') as input:
    # print(input.readline())
    # print(arr_length)
    y = 0
    for line in input:
        forest[y] = []
        line = line.strip('\n')
        length = len(line)
        for char in line:
            forest[y].append(int(char))
        y += 1
    height = y
    num_trees = (length) * (height)

# print(forest)
# print(num_trees)
# print(length)

# start finding invisible trees
num_invis = num_trees

# trees on top and bottom are visible
# num_invis -= (2 * length)

# trees on sides are visible - exclude already counted top & bottom
num_invis -= (2 * (height - 2))

# find invisible trees
for y in forest:  # 0 - 98
    x = 0
    for tree in forest[y]:
        print(x)  # 0 - 98
        if y == 0:  # top trees
            num_invis -= 1
        elif x == 0:
            num_invis -= 1
        x += 1
