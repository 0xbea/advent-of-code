# Rock: A, X +1
# Paper: B, Y +2 
# Scissors: C, Z +3
# Win: AY, BZ, CX +6
# Draw: AX, BY, CZ +3
# Lose: AZ, BX, CY +0

# A - Rock, B - Paper, C - Scissors
# X - lose, Y - draw, Z - win

outcome = {
    'lose': 0,
    'draw': 3,
    'win': 6
}

uchooz = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

scoring = {
    'A': {  # rock
        'X': uchooz['scissors'] + outcome['lose'], # ulose
        'Y': uchooz['rock'] + outcome['draw'], #udraw
        'Z': uchooz['paper'] + outcome['win']
    },
    'B': { # paper
        'X': uchooz['rock'] + outcome['lose'],
        'Y': uchooz['paper'] + outcome['draw'],
        'Z': uchooz['scissors'] + outcome['win']
    },
    'C': { #scissors
        'X': uchooz['paper'] + outcome['lose'],
        'Y': uchooz['scissors'] + outcome['draw'],
        'Z': uchooz['rock'] + outcome['win']
    } 
}

score = 0

with open('./inputs/day2.txt','r') as input:
    # read file
    # line=input.readline().rstrip('\n')
    for line in input:
        # print(line)
        theirchoice = line[0]
        urchoice = line[2]
        # print(uchooz)
        score+=scoring[theirchoice][urchoice]
    print(score)
