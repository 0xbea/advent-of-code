# Example
# keep track of which directory you're in
# current_dir = example
# "subdirectory":{}
# "file": int
# "dir_marker" = []

example_dir = {
    "/": {
        "a": {},
        "b.txt": 14848514,
        "c.dat": 8504156,
        "d": {}
    }
}

example_size_tracker = {
    "/": 223,
    "a": 100,
    "d": 123
}


# def setCurrentDir(current_dir, dir_marker):  # set this variable
#    for marker in dir_marker:
#        current_dir = current_dir[marker]


def changeDir(current_dir, dir_marker, target):  # updates directory structure and marker
    if (target == ".."):
        dir_marker.pop()
    else:
        dir_marker.append(target)
        # current_dir[target] = {}  # creates empty dict at target
        # print(current_dir)
        # current_dir = current_dir[target]
    # setCurrentDir(current_dir, dir_marker)  # update current directory


def trackSize(dir_marker, file_size):  # updates size tracker
    for marker in dir_marker:
        if marker not in size_tracker:
            size_tracker[marker] = int(file_size)
        else:
            size_tracker[marker] += int(file_size)


def trackFile(current_dir, dir_marker, filename, file_size):
    current_dir[filename] = int(file_size)
    trackSize(dir_marker, file_size)


with open('./inputs/day7.txt', 'r') as input:
    current_dir = {}  # map out dir structure here
    dir_marker = []  # keep track of which directory you're in
    size_tracker = {}
    for line in input:
        line = line.strip('\n').split(' ')
        print(line)
        if line[0] == '$':  # handle command
            if line[1] == 'cd':
                changeDir(current_dir, dir_marker, line[2])
            # handle ls
        else:
            if line[0][0] in '0123456789':
                # trackFile(current_dir, dir_marker, line[1], line[0])
                trackSize(dir_marker, line[0])
    # print(current_dir)
    print(dir_marker)
    print(size_tracker)
    total = 0
    for key in size_tracker:
        if size_tracker[key] <= 100000:
            total += size_tracker[key]
    print(total)
