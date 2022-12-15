def get_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def swap(a, b):
    return b, a


def rockpoint_set(input):
    rocks = set()
    for wholerock in input:
        newwholerock = wholerock.split(" -> ") # '498,4 -> 498,6 -> 496,6'
        for xyI in range(1, len(newwholerock)): # '498,4'
            xy1 = newwholerock[xyI-1].split(",") #
            xy2 = newwholerock[xyI].split(",")
            x1 = int(xy1[0])
            y1 = int(xy1[1])
            x2 = int(xy2[0])
            y2 = int(xy2[1])
            if y1 > y2:
                y1, y2 = swap(y1, y2)
            if x1 > x2:
                x1, x2 = swap(x1, x2)

            if x1 == x2: # verticle line
                for y in range(y1, y2+1):
                    rocks.add((x1, y))
            else:
                for x in range(x1, x2+1):
                    rocks.add((x, y1))
    return rocks


def make_arr(rocks):
    xpoints = set([x[0] for x in rocks])
    ypoints = set([y[1] for y in rocks])
    minx = min(xpoints)
    maxX = max(xpoints)
    miny = 0
    maxY = max(ypoints)
    bonusx = 140  # Bonus size for part 2 for extending X axis, was too lazy to do this dynamically
    middle = 500-minx+bonusx
    arr = []
    for row in range(0, maxY+3):
        temprow = []
        for col in range(0, maxX-minx+(bonusx*2)+1):
            point = "."
            if row == maxY+2:
                point = "#"
            elif (col+minx-bonusx, row+miny) in rocks:
                point = "#"
            temprow.append(point)
        arr.append(temprow)
    return arr, middle


def printarr(arr):
    for row in arr:
        print(" ".join(row))


class Sand():
    clog = False
    fallcount = 0
    def __init__(self):
        self.y = 0
        self.x = Sand.middle
        self.update()

    def update(self):
        if Sand.arr[0][Sand.middle] == "O":
            Sand.clog = True
            Sand.fallcount += 1
            return True
        if self.checkdown(): pass
        elif self.checkleft(): pass
        elif self.checkright(): pass
        else:
            self.place()
            return True
        return self.update()

    def checkdown(self):
        if self.y == len(Sand.arr)-1:
            return True
        elif Sand.arr[self.y+1][self.x] == ".":
            self.y = self.y+1
            return True
        else:
            return False

    def checkleft(self):
        if self.x == 0 or self.y == len(Sand.arr)-1:
            return True
        elif Sand.arr[self.y+1][self.x-1] == ".":
            self.y +=1
            self.x -=1
            return True
        else:
            return False

    def checkright(self):
        if self.x == len(Sand.arr[0])-1 or self.y == len(Sand.arr)-1:
            return True
        elif Sand.arr[self.y+1][self.x+1] == ".":
            self.y +=1
            self.x +=1
            return True
        else:
            self.currentlyfalling = False
            return False

    def place(self):
        Sand.arr[self.y][self.x] = "O"


def sand_fall():
    while Sand.clog == False:
        Sand.fallcount += 1
        Sand()


def main():
    input = get_input()
    rocks = rockpoint_set(input)
    Sand.arr, Sand.middle = make_arr(rocks)
    sand_fall()
    printarr(Sand.arr)
    print(f"The top of the sand spawner is reached in this many grains: {Sand.fallcount-1}")


if __name__ == "__main__":
    main()

