def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        return lines[0]


def getcode(arr, length):
    for i in range(length, len(arr)):
        theset = set(arr[i-length:i])
        if len(theset) == length:
            return i


def main():
    input = getinput()
    part1solution = getcode(input, 4)
    print(f"The first start of packet marker is detected at {part1solution} characters.")
    part2solution = getcode(input, 14)
    print(f"The first start of message marker is detected at {part2solution} characters.")


if __name__ == "__main__":
    main()
