forest = {}
# num_trees = 0
length = 0 #99
height = 0 #99

# scenic score: number of trees until tree with >= height

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
    # num_trees = (length) * (height)

# print(forest)
# print(num_trees)
# print(length)


def scoreLeft(x,y,tree):
    # keep checking leftwards until u hit greater or equal (>=) tree
    score = 1 
    checking = x - 1
    while checking > 0: 
        if forest[y][checking] >= tree:
            break
        else: 
            score += 1
            checking -= 1
    if (x == 2 and y == 3):
        print(str(x) + ',' + str(y) + ':' + str(score))
    return score

def scoreRight(x,y,tree):
    # keep checking rightwards until u hit greater or equal (>=) tree
    score = 1 
    checking = x + 1
    while checking < (length - 1): 
        if forest[y][checking] >= tree:
            break
        else: 
            score += 1
            checking += 1
    if (x == 2 and y == 3):
        print(str(x) + ',' + str(y) + ':' + str(score))
    return score

def scoreTop(x, y, tree):
    # check upwards until greater or equal tree
    score = 1
    checking = y - 1
    while checking > 0: 
        if forest[checking][x] >= tree: # not visible top if there is taller tree
            break
        else: 
            score += 1
            checking -= 1
    if (x == 2 and y == 3):
        print(str(x) + ',' + str(y) + ':' + str(score))
    return score

def scoreBottom(x,y,tree):
    score = 1
    checking = y + 1
    while checking < (height - 1): 
        if forest[checking][x] >= tree: # not visible top if there is taller tree
            break
        else: 
            score += 1
            checking += 1
    if (x == 2 and y == 3):
        print(str(x) + ',' + str(y) + ':' + str(score))
    return score

score_tracker=[]
# start calculating scores
for y in forest:  # 0 - 98
    x = 0
    for tree in forest[y]:
        score = 1 
        # print(x)  # 0 - 98
        if y == 0:  # top trees
            score *= 0
        elif x == 0:
            score *= 0
        elif y == (height - 1):
            score *= 0
        elif x == (length - 1):
            score *= 0
        else: 
            score *= scoreLeft(x,y,tree)
            score *= scoreRight(x,y,tree)
            score *= scoreTop(x,y,tree)
            score *= scoreBottom(x,y,tree)
        score_tracker.append(score)
        # print(str(x) + ',' + str(y) + ':' + str(score))
        x += 1

print(score_tracker)
print(max(score_tracker))