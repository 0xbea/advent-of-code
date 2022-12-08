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


def checkVisLeft(x,y,tree):
    # check Vis horizontally - True or False
    i = 0
    visible = True
    while i < x: 
        if forest[y][i] >= tree: # not visible left if there is taller tree
            visible = False
            break
        else: 
            i += 1
    return visible

def checkVisRight(x,y,tree):
    # check Vis horizontally - True or False
    checking = length - 1
    visible = True
    while checking > x: 
        if forest[y][checking] >= tree: # not visible right if there is taller tree
            visible = False
            break
        else: 
            checking -= 1
    return visible

def checkVisTop(x, y, tree):
    # check vis vertically - True or False
    i = 0
    visible = True
    while i < y: 
        if forest[i][x] >= tree: # not visible top if there is taller tree
            visible = False
            break
        else: 
            i += 1
    return visible

def checkVisBottom(x,y,tree):
    checking = height - 1
    visible = True
    while checking > y: 
        if forest[checking][x] >= tree: # not visible right if there is taller tree
            visible = False
            break
        else: 
            checking -= 1
    return visible

# start finding invisible trees
num_invis = num_trees
for y in forest:  # 0 - 98
    x = 0
    for tree in forest[y]:
        # print(x)  # 0 - 98
        if y == 0:  # top trees
            num_invis -= 1
        elif x == 0:
            num_invis -= 1
        elif checkVisLeft(x,y,tree):
            num_invis -= 1
        elif checkVisRight(x,y,tree):
            num_invis -= 1
        elif checkVisTop(x,y,tree):
            num_invis -= 1
        elif checkVisBottom(x,y,tree):
            num_invis -= 1
        else:
            print( str(x) + ',' + str(y) + ' is invisible')
        x += 1

print(num_trees)
print(num_invis)
num_vis = num_trees - num_invis
print(num_vis)