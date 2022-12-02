pickpoints = {  # The bonus points for our pick
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcomes = {  # [Win, Draw, Lose]
    "rock": ["paper", "rock", "scissors"],
    "paper": ["scissors", "paper", "rock"],
    "scissors": ["rock", "scissors", "paper"]
}

translations = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}


def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [entry.strip().replace(" ", "") for entry in lines]
        return lines


def part1(matches):
    totalsum = 0
    for match in matches:
        theirpick = translations[match[0]]
        ourpick = translations[match[1]]
        points = pickpoints[ourpick]
        indexoutcome = outcomes[theirpick].index(ourpick)
        if indexoutcome == 0:  # win
            points += 6
        elif indexoutcome == 1:  # tie
            points += 3
        totalsum += points
    return totalsum


def part2(matches):
    totalsum = 0
    for match in matches:
        theirpick = translations[match[0]]
        neededoutcome = match[1]
        if neededoutcome == "Z":  # needwin
            totalsum += 6
            ourchoice = outcomes[theirpick][0]
            totalsum += pickpoints[ourchoice]
        elif neededoutcome == "Y":  # needdraw
            totalsum += 3
            ourchoice = outcomes[theirpick][1]
            totalsum += pickpoints[ourchoice]
        elif neededoutcome == "X":  # needloss
            ourchoice = outcomes[theirpick][2]
            totalsum += pickpoints[ourchoice]
    return totalsum


def main():
    input = getinput()
    part1answer = part1(input)
    print(f"The answer to part 1: {part1answer}")
    part2final = part2(input)
    print(f"The answer to part 2: {part2final}")


if __name__ == "__main__":
    main()
