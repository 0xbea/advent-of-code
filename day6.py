with open('./inputs/day6.txt') as input:
    stream = input.readline()
    i = 0
    found = False
    while i < len(stream) and not (found):
        phrase = stream[i:i+14]     # read 4 or 14 chars at a time
        print(phrase)
        for char in phrase:
            if phrase.count(char) > 1:
                i += 1
                break
        print(i+14)
# not sure how to terminate loop
