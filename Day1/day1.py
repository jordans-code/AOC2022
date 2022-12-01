def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        return lines


def getsums(rawinput):
    """Returns an array of ints which are the sums of the calories of the elves"""
    stripped = [entry.strip() for entry in rawinput]
    sums = []
    tempsum = 0
    for entry in stripped:
        if entry:
            tempsum += int(entry)
        else:
            sums.append(tempsum)
            tempsum = 0
    return sums


def main():
    lines = getinput()
    sums = getsums(lines)

    part1 = max(sums)
    print(f"Part 1 solution: {part1}")

    sums.sort(reverse=True)
    part2 = sum(sums[0:3])
    print(f"Part 2 solution: {part2}")


if __name__ == "__main__":
    main()
