elf_cals=[0]
i=0
with open('./inputs/day1.txt','r') as input:
    # read file
    line=input.readline().rstrip('\n')
    for line in input:
        # print(line)
        # print(elf_cals)
        if line == '\n':
            elf_cals.append(0)
            i = i+1
        else:
            elf_cals[i]=elf_cals[i]+int(line)
    print(max(elf_cals))
    elf_cals.sort(reverse=True)
    print(elf_cals[0] + elf_cals[1] + elf_cals[2])
