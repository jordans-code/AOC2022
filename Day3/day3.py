priority = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]
        return lines


def part1(input):
    totalsum = 0
    for rucksack in input:
        firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        seen = ""  # to not count duplicates
        for item in firstpart:
            if item in secondpart and item not in seen:
                totalsum += priority.index(item)+1
                seen += item
    return totalsum


def part2(input):
    badges = 0
    for i in range(2, len(input), 3):
        bag1 = input[i-2]
        bag2 = input[i-1]
        bag3 = input[i]
        for item in bag1:
            if item in bag2 and item in bag3:
                badges += priority.index(item)+1
                break
    return badges


def main():
    input = getinput()
    part1solution = part1(input)
    print("The solution to part 1: " + str(part1solution))
    part2solution = part2(input)
    print("The solution to part 2: " + str(part2solution))


if __name__ == "__main__":
    main()
