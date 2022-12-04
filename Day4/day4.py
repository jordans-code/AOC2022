def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]
        return lines


def checkfullycontains(range1, range2):
    range1 = [int(x) for x in range1.split("-")]
    range2 = [int(x) for x in range2.split("-")]
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    else:
        return False


def checkoverlap(range1, range2):
    range1 = [int(x) for x in range1.split("-")]
    range2 = [int(x) for x in range2.split("-")]
    if range2[0] <= range1[0] <= range2[1]:
        return True
    elif range2[0] <= range1[1] <= range2[1]:
        return True
    else:
        return False


def part1(input):
    fullycontainedpairs = 0
    for pair in input:
        ranges = pair.split(",")
        result = checkfullycontains(ranges[0], ranges[1])
        resultinverse = checkfullycontains(ranges[1], ranges[0])
        if result or resultinverse:
            fullycontainedpairs += 1
    return fullycontainedpairs


def part2(input):
    overlapping = 0
    for pair in input:
        ranges = pair.split(",")
        range1 = ranges[0]
        range2 = ranges[1]
        result = checkoverlap(range1, range2)
        resultinverse = checkoverlap(range2, range1)
        if result or resultinverse:
            overlapping += 1
    return overlapping


def main():
    input = getinput()
    part1solution = part1(input)
    print("The amount of assignment pairs in which one range fully contains another: " + str(part1solution))
    part2solution = part2(input)
    print("The amount of assignment pairs that have overlapping ranges: " + str(part2solution))


if __name__ == "__main__":
    main()
