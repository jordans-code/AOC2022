def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def parsecommands(input):
    """Parses each command and returns a directory of each filepath as a tuple and it's size as the value.
        Also returns a set of each unique directory paths so that we can later update their sizes to match
        the files that are contained within them."""
    filesizes = {}
    dirpaths = set()
    cur_path = tuple()
    for line in input:
        if line == "$ ls": continue
        elif line == "$ cd ..":
            cur_path = cur_path[:-1]
        elif line.startswith("dir"):
            dirpaths.add((*cur_path, line[4:]))
        elif line[:4] == "$ cd":
            cur_path = (*cur_path, line[5:])
        else:  # The rest are files
            line = line.split(" ")
            size, filename = int(line[0]), line[1]
            filesizes[(*cur_path, filename)] = size
    return filesizes, dirpaths


def sum_child_dirs(filesizes, dirpaths):
    """Loops through each unique dir/filepath and sums the size of all child directory files
        Then returns a new dictionary of all directory paths with the value being the sum of everything contained within it"""
    dirsizes_withchildren = {}
    for directory in dirpaths:
        dirsum = 0
        for file, filesize in filesizes.items():
            filepath = '/'.join(file)
            dirpath = '/'.join(directory)
            if filepath.startswith(dirpath):  # if file is a child of the dir
                dirsum += filesize
        dirsizes_withchildren[directory] = dirsum
    return dirsizes_withchildren


def part1(dirsizes_withchildren):
    """returns the sum of each directory which is less than 100000 in size (includes child dirs)"""
    return sum((dir1 for dir1 in dirsizes_withchildren.values() if dir1 <= 100000))


def part2(filesizes, dirsizes_withchildren):
    """finds the space that is needed to be cleared and then returns the lowest sized directory to delete to make space"""
    availiblespace = 70000000 - sum(filesizes.values())
    requiredspace = 30000000
    minimum_space_needed = requiredspace - availiblespace
    p2_solution = min(val for val in dirsizes_withchildren.values() if val >= minimum_space_needed)
    return p2_solution


def main():
    input = getinput()
    filesizes, dirpaths = parsecommands(input)
    dirsizes_withchildren = sum_child_dirs(filesizes, dirpaths)
    p1_solution = part1(dirsizes_withchildren)
    print("The sum of the total sizes of the directories that are less than 100000 is: " + str(p1_solution))
    p2_solution = part2(filesizes, dirsizes_withchildren)
    print("The smallest directory that would free up enough space on the filesystems total size is: " + str(p2_solution))


if __name__ == "__main__":
    main()

