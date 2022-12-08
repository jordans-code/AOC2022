visibleTrees = set()


def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def pt1_findVisibleTrees(currentheight, lastheight, col, row):
    """Check if tree at coordinate is visible"""
    if currentheight > lastheight:
        visibleTrees.add((col, row))
        return currentheight
    else:
        return lastheight


def pt1_checkRange(input, col, row):
    """Checks if the range of coordinates of trees given are visible"""
    lastheight = -1
    if type(row) is range:  # If verticle
        for r in row:
            currentheight = int(input[r][col])
            lastheight = pt1_findVisibleTrees(currentheight, lastheight, col, r)
    else:
        for c in col:  # If horizontal
            currentheight = int(input[row][c])
            lastheight = pt1_findVisibleTrees(currentheight, lastheight, c, row)


def part1(input):
    rowcount = len(input)
    colcount = len(input[0])
    for col in range(colcount):  # Verticle
        pt1_checkRange(input, col, range(rowcount))  # From up facing down
        pt1_checkRange(input, col, range(rowcount-1, -1, -1))  # From down facing up
    for row in range(rowcount):
        pt1_checkRange(input, range(colcount), row)  # From left facing right
        pt1_checkRange(input, range(colcount-1, -1, -1), row)  # From right facing left
    return str(len(visibleTrees))


def get_scenicscore(input, origheight, x, y):
    score = 0
    if type(x) is range:
        for col in x:
            currentheight = int(input[y][col])
            score += 1
            if currentheight >= origheight:
                return score
    else:
        for row in y:
            currentheight = int(input[row][x])
            score += 1
            if currentheight >= origheight:
                return score
    return score


def part2(input):
    scores = []
    rowcount = len(input)
    colcount = len(input[0])
    for row in range(rowcount):
        for col in range(colcount):
            origheight = int(input[row][col])
            leftscore = get_scenicscore(input, origheight, range(col-1, -1, -1), row)
            upscore = get_scenicscore(input, origheight, col, range(row-1, -1, -1))
            downscore = get_scenicscore(input, origheight, col, range(row+1, len(input)))
            rightscore = get_scenicscore(input, origheight, range(col+1, len(input[0])), row)
            scenicscore = upscore * downscore * leftscore * rightscore
            scores.append(scenicscore)
    return max(scores)


def main():
    input = getinput()
    part1solution = part1(input)
    print("The solution to part 1/amount of trees visible from the outside grid: " + part1solution)
    part2solution = part2(input)
    print("The solution to part 2 / the tree with the highest scenic score is " + str(part2solution))


if __name__ == "__main__":
    main()

