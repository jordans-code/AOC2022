def get_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


class Sensor():
    def __init__(self, importanty, x, y, bx, by):
        self.importanty = importanty
        self.x = x
        self.y = y
        self.closestbeaconx = bx
        self.closestbeacony = by
        self.cannotcontain = set()
        self.distance = self.manhattan_distance((self.x, self.y), (self.closestbeaconx, self.closestbeacony))
        self.points = self.triangle_points()

    def manhattan_distance(self, point1, point2):
        #print(f"manhattan distance between {point1} and {point2} is {sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))}")
        return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))


    def triangle_points(self):
        for row in range(self.y+(self.distance*-1),
                         self.y+self.distance+1):
            if row != self.importanty:
                continue
            currenty = row-self.y
            for x in range((self.x-self.distance)+abs(currenty), ((self.x + self.distance)) + 1-abs(currenty)):
                self.cannotcontain.add((x, row))


def makesensors(input, num):
    sensors = []
    for sensor in input:
        x = int(sensor.split(" x=")[1].split(",")[0])
        y = int(sensor.split(" y=")[1].split(":")[0])
        closestx = int(sensor.split(" x=")[2].split(",")[0])
        closesty = int(sensor.split(" y=")[2].split(":")[0])
        #print(f"Adding sensor at {x},{y} with the closest beacon at {closestx}, {closesty}")
        sensors.append(Sensor(num, x, y, closestx, closesty))
    return sensors

def part1(row, sensors):
    onrow = set()
    for sensor in sensors:
        for point in sensor.cannotcontain:
            if point[1] == row:
                onrow.add(point)

    for sensor in sensors:  # Removes the actual beacons
        if (sensor.closestbeaconx, sensor.closestbeacony) in onrow:
            onrow.remove((sensor.closestbeaconx, sensor.closestbeacony))
    print(len(onrow))


def main():
    input = get_input()
    num = 2000000
    print(input)
    sensors = makesensors(input, num)
    part1(num, sensors)


if __name__ == "__main__":
    main()

