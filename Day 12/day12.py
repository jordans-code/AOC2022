def get_input():
    """Generates a graph of nodes representing points"""
    with open("input.txt") as f:
        start = (0, 0)
        lines = f.readlines()
        lines = [[x for x in z if x != "\n"] for z in lines]
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                item = lines[row][col]
                if item == "E":
                    finish = (row, col)
                    lines[row][col] = "z"
                elif item == "S":
                    start = (row, col)
                    lines[row][col] = "a"
    return lines, start, finish


def checkdirs(graph, neighbory, neighborx, queueitem, col, row, seen):
    """Checks if a neighbor exists next to the current point and if it hasnt been seen and is the correct height returns True"""
    if (neighbory, neighborx) not in seen:
        if 0 <= neighbory < row and 0 <= neighborx < col:
            neighbor = ord(graph[neighbory][neighborx])
            root = ord(graph[queueitem[0]][queueitem[1]])
            if neighbor-root > -2:
                return True
            else:
                return False


def bfs(graph, start, end, ispart2):
    row = len(graph)
    col = len(graph[0])
    seen = []
    queue = [start]
    cost = [[0 for _ in range(col)] for _ in range(row)]
    while len(queue) > 0:
        queueitem = queue.pop(0)
        if ispart2 and graph[queueitem[0]][queueitem[1]] == "a":
            return (cost[queueitem[0]][queueitem[1]])
        elif not ispart2 and queueitem == end:
            return cost[end[0]][end[1]]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dirnumber in range(4):  # checks each direction for a neighbor it can move to
            neighbory = queueitem[0] + directions[dirnumber][0]
            neighborx = queueitem[1] + directions[dirnumber][1]
            if checkdirs(graph, neighbory, neighborx, queueitem, col, row, seen):
                queue.append((neighbory, neighborx))
                seen.append((neighbory, neighborx))
                cost[neighbory][neighborx] = cost[queueitem[0]][queueitem[1]] + 1
    return None


def main():
    input, start, finish = get_input() # Creates graph of nodes and finds the start and finish points.
    part1solution = bfs(input, finish, start, False)
    print(f"The solution to part2: {part1solution}")
    part2solution = bfs(input, finish, start, True)
    print(f"The solution to part2: {part2solution}")


if __name__ == "__main__":
    main()
