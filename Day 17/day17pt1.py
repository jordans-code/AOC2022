import time
start_time = time.time()


def get_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = "".join([x[:-1] for x in lines])  # strips \n
        return lines


def print_grid():
    for row in Rock.grid:
        print(" ".join(row))


class Rock():
    Tower_Height = 0
    grid = []
    blankrow = ["."]*7
    grid.insert(0, blankrow.copy())
    push_mappings = {">": 1, "<": -1}
    tower_complete = False
    last_push = -1

    def __init__(self, startingpoints):
        self.trim_tower()
        self.currentpos = startingpoints
        self.spawn_rock()
        self.placed = False
        self.falling = True
        self.update()

    def update(self):
        if Rock.tower_complete:
            self.check_height()
            return True

        if not self.falling:
            self.place()
            return True
        self.jet()
        self.fall()
        return self.update()

    def get_tower_height(self):
        return len(Rock.grid) - self.get_highest_rock()

    def trim_tower(self):  # vain attempt to optimize code for part 2, though it does make part1 10x faster
        if len(Rock.grid) > 40:
            del Rock.grid[len(Rock.grid) - 10:]
            Rock.Tower_Height += 10

    def place(self):
        for x,y in self.currentpos:
            Rock.grid[y][x] = "#"

    def jet(self):
        if Rock.last_push == len(Rock.push_order)-1:
            Rock.last_push = -1
        Rock.last_push += 1
        current_push = Rock.push_order[Rock.last_push]
        self.shift_points(Rock.push_mappings[current_push], 0)

    def fall(self):
        if not self.shift_points(0, 1):
            self.falling = False

    def shift_points(self, xchange, ychange):
        temporary_points = []
        for point in range(len(self.currentpos)):
            currentx = self.currentpos[point][0]
            currenty = self.currentpos[point][1]
            newx = currentx+xchange
            newy = currenty+ychange
            if not(6 >= newx >= 0 and newy <= len(Rock.grid)-1):
                return False
            if Rock.grid[newy][newx] != ".":
                return False
            temporary_points.append(((newx), (newy)))
        self.currentpos = temporary_points
        return True

    def spawn_rock(self):
        self.extend_grid()
        self.shift_points(2, 0)

    def extend_grid(self):
        highest_rock = self.get_highest_rock()
        bottom_edge = self.get_bottom_edge()
        if highest_rock == 0:
            self.extend_grid_by(3)
        else:
            extendby = 4 - highest_rock + bottom_edge
            self.extend_grid_by(extendby)

    def extend_grid_by(self, endrange):
        if endrange > 0:
            for row in range(0, endrange):
                Rock.grid.insert(0, Rock.blankrow.copy())
        else:
            for row in range(abs(endrange)):
                Rock.grid.pop(0)

    def get_left_edge(self):
        return min([x for x,y in self.currentpos])

    def get_bottom_edge(self):
        return max([y for x, y in self.currentpos])

    def get_highest_rock(self):
        myguy = [i for i in range(len(Rock.grid)) if Rock.grid[i] != Rock.blankrow]
        if len(myguy) == 0:
            return 0
        return min(myguy)


class Horizontal_Line(Rock):
    def __init__(self):
        self.type = "Horizontal_Line"
        self.startingpoints = [(0, 0), (1, 0), (2, 0), (3, 0)]
        super().__init__(self.startingpoints)


class Plus(Rock):
    def __init__(self):
        self.type = "Plus"
        self.startingpoints = [(1, 0),
                               (0, 1), (1, 1), (2, 1),
                               (1, 2)]
        super().__init__(self.startingpoints)


class L_Shape(Rock):
    def __init__(self):
        self.type = "L_Shape"
        self.startingpoints = [(2, 0),
                               (2, 1),
                               (0, 2), (1, 2), (2, 2)]
        super().__init__(self.startingpoints)


class Verticle_Line(Rock):
    def __init__(self):
        self.type = "Verticle_Line"
        self.startingpoints = [(0, 0),
                               (0, 1),
                               (0, 2),
                               (0, 3)]
        super().__init__(self.startingpoints)


class Square(Rock):
    def __init__(self):
        self.type = "Square"
        self.startingpoints = [(0, 0),
                               (0, 1),
                               (1, 0),
                               (1, 1)]
        super().__init__(self.startingpoints)


def part1():
    currentrock = 0
    rockmapping = {0: Horizontal_Line,
                   1: Plus,
                   2: L_Shape,
                   3: Verticle_Line,
                   4: Square}
    for rock in range(0, 2022):
        if currentrock == 5:
            currentrock = 0
        z = rockmapping[currentrock]()
        if rock == 2021:
            print(z.get_tower_height() + Rock.Tower_Height)
        currentrock +=1
    print_grid()


def main():
    Rock.push_order = get_input()
    part1()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
