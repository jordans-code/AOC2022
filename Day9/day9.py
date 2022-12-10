def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        lines = "".join([(cmd.split(" ")[0] * int(cmd.split(" ")[1])) for cmd in lines])
        return lines


class TailPoint:
    def __init__(self, tail_length):
        self.x = 0
        self.y = 0
        self.tail_length = tail_length
        self.VisitedPoints = set()
    move_order_map = {"D": (0, -1),
                    "U": (0, 1),
                    "L": (-1, 0),
                    "R": (1, 0)}

    def move(self, direction):
        newx, newy = TailPoint.move_order_map[direction]
        self.x += newx
        self.y += newy

    def logvisited(self):
        self.VisitedPoints.add((self.x, self.y))

    def getpoints(self):
        return (self.x, self.y)

    def determinediff(self, followx, followy):
        diffx = abs(self.x-followx)
        diffy = abs(self.y-followy)
        return (diffx, diffy)

    def diagonalmove(self, followx, followy):
        dir = "U" if followy > self.y else "D"
        self.move(dir)
        dir = "R" if followx > self.x else "L"
        self.move(dir)

    def verticalmove(self, followy):
        dir = "U" if followy > self.y else "D"
        self.move(dir)

    def horizontalmove(self, followx):
        dir = "R" if followx > self.x else "L"
        self.move(dir)

    def unevendiagonalmove(self, followx, followy, diffx, diffy):
        """The difference that equals 1 will always be the same row or column that we follow on
        Then we just need to move over one value for the other
        ex: (3, 1) following (4, 3). x diff == 1 so we set that x equal to ours"""
        if diffx == 1:  # If we need to move left or right
            self.x = followx
            dir = "U" if followy > self.y else "D"
        else:  # If we need to move up or down
            self.y = followy
            dir = "R" if followx > self.x else "L"
        self.move(dir)

    def handlemove(self, followx, followy):
        diffx, diffy = self.determinediff(followx, followy)
        if diffx < 2 and diffy < 2: pass  # If the part we are following is 1 x and 1 y away or less.
        elif diffx == 2 and diffy == 2:  # If diagonal
            self.diagonalmove(followx, followy)
        elif diffx == 0:  # if up or down move
            self.verticalmove(followy)
        elif diffy == 0:  # if right or left move
            self.horizontalmove(followx)
        else:  # if partial diagonal (2 up 1 right etc)
            self.unevendiagonalmove(followx, followy, diffx, diffy)


def movehead(currentpos, moveorder):
    xchange, ychange = TailPoint.move_order_map[moveorder]
    return (currentpos[0]+xchange, currentpos[1]+ychange)


def printboard(VisitedPoints):
    """Visualizes the tail moving around in a grid. Useful for when you write buggy code and can't find an issue,
    speaking from personal experience"""
    board = []
    allxpoints = [x[0] for x in VisitedPoints]
    allypoints = [x[1] for x in VisitedPoints]
    minY = min(allypoints)
    maxY = max(allypoints)
    diffY = maxY - minY
    minX = min(allxpoints)
    maxX = max(allxpoints)
    diffX = maxX - minX
    for rowI in range((diffY * 2 + 1)):
        row = ["."] * (diffX * 2 + 1)
        board.append(row)
    for x, y in VisitedPoints:
        newx = (x + diffX)
        newy = (y + diffY)
        board[newy][newx] = "X"
    for row in board[::-1]:
        print(row)


def snakemover(moveorders, tails):
    currentheadpos = (0, 0)
    for moveorder in moveorders:
        currentheadpos = movehead(currentheadpos, moveorder)
        tails[0].x = currentheadpos[0]
        tails[0].y = currentheadpos[1]
        for taili in range(1, len(tails)):
            lasttailx, lasttaily = tails[taili-1].getpoints()
            tails[taili].handlemove(lasttailx, lasttaily)
            if taili+1 == tails[taili].tail_length:
                tails[taili].logvisited()
    return tails


def part1(moveorders):
    taillength = 2
    tails = [TailPoint(taillength) for _ in range(taillength)]  # 0 is the head, 9 is the true "tail" for the problem.
    tails = snakemover(moveorders, tails)
    #printboard(tails[taillength-1].VisitedPoints)
    return "The back tail of the snake visits these many unique positions for part1: " + str(len(tails[taillength-1].VisitedPoints))


def part2(moveorders):
    taillength = 10
    tails = [TailPoint(taillength) for _ in range(taillength)]  # 0 is the head, 9 is the true "tail" for the problem.
    tails = snakemover(moveorders, tails)
    #printboard(tails[taillength-1].VisitedPoints)
    return "The back tail of the snake visits these many unique positions for part2: " + str(len(tails[taillength-1].VisitedPoints))


def main():
    moveorders = getinput()
    part1solution = part1(moveorders)
    print(part1solution)
    part2solution = part2(moveorders)
    print(part2solution)

if __name__ == "__main__":
    main()
