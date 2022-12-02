# Rock: A, X +1
# Paper: B, Y +2 
# Scissors: C, Z +3
# Win: AY, BZ, CX +6
# Draw: AX, BY, CZ +3
# Lose: +0

score = 0

with open('./inputs/day2.txt','r') as input:
    # read file
    # line=input.readline().rstrip('\n')
    for line in input:
        # print(line)
        theychooz = line[0]
        uchooz = line[2]
        # print(uchooz)
        if uchooz == 'X':
            # calculate u choose rock
            score += 1
            if theychooz == 'A':
                score += 3
            if theychooz == 'B':
                score += 0
            if theychooz == 'C':
                score += 6
        elif uchooz == 'Y':
            # calculate u choose paper
            score += 2
            if theychooz == 'A':
                score += 6
            if theychooz == 'B':
                score += 3
            if theychooz == 'C':
                score += 0
        elif uchooz == 'Z':
            # calculate u choose scissors
            score += 3
            if theychooz == 'A':
                score += 0
            if theychooz == 'B':
                score += 6
            if theychooz == 'C':
                score += 3
    print(score)
