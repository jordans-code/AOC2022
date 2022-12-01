
def day1(rawinput):
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

with open("input.txt") as f:
    lines = f.readlines()
    sums = day1(lines)
    print(max(sums)) # part 1

    # part2
    sums.sort(reverse=True)
    print(sum(sums[0:3]))