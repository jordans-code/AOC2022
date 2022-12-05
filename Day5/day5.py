def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [entry[:-1] for entry in lines]  # remove \n only
        return lines


def getcommands(input):
    cargomap = [input[entry] for entry in range(8)]
    commands = [input[entry] for entry in range(10, len(input))]
    return cargomap, commands


def getlastcrates(cargomap):
    return "".join([stack[-1] for stack in cargomap])


def parsemap(cargomap):
    cratestacks = [[] for _ in range(9)]
    for inputline in cargomap:
        for i in range(2, len(cargomap[0]), 4):
            crateletter = i-1
            col = (crateletter-1)//4
            if inputline[crateletter] != " ":
                cratestacks[col].insert(0, inputline[i-1])
    return cratestacks


def parsecommands(command):
    splitc = command.split(" ")
    moveamount = int(splitc[1])
    oldstack = int(splitc[3]) - 1
    newstack = int(splitc[5]) - 1
    return moveamount, oldstack, newstack


def part1(cargomap, commands):
    for command in commands:
        moveamount, oldstack, newstack = parsecommands(command)
        for i in range(moveamount):
            crate = cargomap[oldstack].pop()
            cargomap[newstack].append(crate)
    return getlastcrates(cargomap)


def part2(cargomap, commands):
    for command in commands:
        moveamount, oldstack, newstack = parsecommands(command)
        temp = []
        for i in range(moveamount):
            temp.insert(0, cargomap[oldstack].pop())
        for crate in temp:
            cargomap[newstack].append(crate)
    return getlastcrates(cargomap)


def main():
    input = getinput()
    cargomapraw, commands = getcommands(input)
    cargomap = parsemap(cargomapraw)
    cargomap2 = parsemap(cargomapraw)  # need to make a copy of the list as the list gets modified in part1
    part1solution = part1(cargomap, commands)
    print("The top crates in each row when moving 1 crate at a time (part1): " + part1solution)
    part2solution = part2(cargomap2, commands)
    print("The top crates in each row when moving all the crates at once (part2): " + part2solution)


if __name__ == "__main__":
    main()
