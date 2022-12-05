import re
# Last in array => first added to end of new array
# now which is last of array?

#stacks from bottom to top
stack={}
stack[1]='JHGMZNTF'
stack[2]='VWJ'
stack[3]='GVLJBTH'
stack[4]='BPJNCDVL'
stack[5]='FWSMPRG'
stack[6]='GHCFBNVM'
stack[7]='DHGMR'
stack[8]='HNMVZD'
stack[9]='GNFH'

def shift(quant,origin,dest):
    for i in range(quant):
        topCrate = stack[origin][-1]
        stack[origin] = stack[origin][:-1]
        stack[dest] += topCrate
        i += 1

with open('./inputs/day5.txt') as input:
    for line in input:
        match = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if match:
            # print(match.group())
            quant = int(match.group(1))
            origin = int(match.group(2))
            dest = int(match.group(3))
            shift(quant,origin,dest)
        else:
            print(stack)
    for i in stack:
        print(stack[i][-1])