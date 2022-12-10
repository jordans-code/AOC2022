def get_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def print_crt(board):
    for i in range(39, 40 * 6, 40):
        line = ""
        for z in range(i - 40, i):
            line += board[z]
        print(line)


class Controller():
    def __init__(self, input):
        self.input = input
        self.register = 1
        self.signal_str = []
        self.lookfor = [20, 60, 100, 140, 180, 220]
        self.cycle = 0
        self.wait = 0
        self.pending_value_change = 0
        self.crt = ["." for _ in range(0, 40*6)]
        self.cycler()

    def part1_handler(self):
        return sum(self.signal_str)

    def part2_handler(self):
        print_crt(self.crt)

    def draw_image(self, register, cycle):
        checking = cycle - 1
        while checking > 39:
            checking -= 40
        regrange = range(register - 1, register + 2)
        if checking in regrange:
            self.crt[cycle - 1] = "#"

    def cycler(self):
        for cmd in self.input:
            pending_current_cmd = True
            while pending_current_cmd:
                self.cycle += 1
                self.draw_image(self.register, self.cycle)
                if self.cycle in self.lookfor:
                    self.signal_str.append(self.register * self.cycle)
                if self.wait:
                    if self.pending_value_change != 0:
                        self.register += self.pending_value_change
                        self.pending_value_change = 0
                        self.wait = False
                        pending_current_cmd = False
                        continue
                else:
                    if "noop" in cmd:
                        pending_current_cmd = False
                        continue
                    elif "addx" in cmd:
                        self.pending_value_change = int(cmd.split(" ")[1])
                        self.wait = True


def main():
    input = get_input()
    controllerinstance = Controller(input)
    print("The solution to part1: " + str(controllerinstance.part1_handler()))
    print("\nThe solution to part2: ")
    controllerinstance.part2_handler()


if __name__ == "__main__":
    main()

