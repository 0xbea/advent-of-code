# Example
# keep track of which directory you're in
# "dir_marker" = []

example_size_tracker = {
    "/": 223,
    "a": 100,
    "d": 123
}


def changeDir(dir_marker, target):  # updates directory structure and marker
    if (target == ".."):
        dir_marker.pop()
    else:
        dir_marker.append(target)


def trackSize(dir_marker, file_size):  # updates size tracker
    path = ""
    for marker in dir_marker:
        path += (marker + "/")
        if path not in size_tracker:
            size_tracker[path] = int(file_size)
        else:
            size_tracker[path] += int(file_size)


with open('./inputs/day7.txt', 'r') as input:
    dir_marker = []  # keep track of which directory you're in
    size_tracker = {}
    for line in input:
        line = line.strip('\n').split(' ')
        print(line)
        if line[0] == '$':  # handle command
            if line[1] == 'cd':
                changeDir(dir_marker, line[2])
        # handle ls
        else:
            if line[0][0] in '0123456789':
                trackSize(dir_marker, line[0])
    # print(current_dir)
    print(dir_marker)
    print(size_tracker)
    free_space = 70000000 - size_tracker["//"]
    space_needed = 30000000 - free_space
    candidate = "//"
    for key in size_tracker:
        if size_tracker[key] >= space_needed:
            print(key)
            if size_tracker[key] < size_tracker[candidate]:
                candidate = key
    print(candidate)
    print(size_tracker[candidate])
