def get_input():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def parsemonkeys(input):
    monkeys = {}
    tempmonkey = {}
    currentmonkey = 0
    input.append("")
    for i in range(len(input)):
        currentitem = input[i]
        if "Monkey" in currentitem:
            monkeynum = int(currentitem.split(" ")[1][0])
            currentmonkey = monkeynum
        elif "Starting items" in currentitem:
            startingitems = currentitem.split(":")[1]
            startingitems = startingitems.replace(" ", "")
            startingitems = [int(x) for x in startingitems.split(",")]
            tempmonkey["startitems"] = startingitems
        elif "Operation" in currentitem:
            operation = currentitem.split("=")[1]
            operation = operation.split(" ")[2:]
            tempmonkey["operation"] = operation
        elif "Test" in currentitem:
            test = currentitem.split("by ")[1]
            tempmonkey["test"] = int(test)
        elif "true" in currentitem:
            true = currentitem.split("monkey ")[1]
            tempmonkey["true"] = int(true)
        elif "false" in currentitem:
            false = currentitem.split("monkey ")[1]
            tempmonkey["false"] = int(false)
        elif currentitem == "":
            monkeys[currentmonkey] = tempmonkey.copy()
            tempmonkey = {}
    return monkeys


class Monkey():
    monkeyinstances = []
    mod = 0

    def __init__(self, number, start_items, operation, test, true, false):
        self.number = number
        self.items = start_items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspectcount = 0

    def throw(self, itemindex, othermonkey):
        othermonkey.items.append(self.items[itemindex])

    def performoperation(self, worrylevel):
        postop = worrylevel
        secondnum = self.operation[1]
        secondnum = worrylevel if secondnum == "old" else int(secondnum)
        if self.operation[0] == "*":
            postop *= secondnum
        elif self.operation[0] == "+":
            postop += secondnum
        return postop

    def bored(self, worrylevel):
        if Monkey.mod > 0:
            return worrylevel % Monkey.mod
        else:
            return worrylevel // 3

    def checkthrow(self, worrylevel):
        if worrylevel % self.test == 0: # divisible by number
            return self.true
        else:
            return self.false

    def inspect(self, itemI):
        self.inspectcount += 1
        oldworrylevel = self.items[itemI]
        opnum = self.performoperation(oldworrylevel)
        borednumber = self.bored(opnum)
        self.items[itemI] = borednumber
        monkeytothrowto = self.checkthrow(borednumber)
        self.throw(itemI, Monkey.monkeyinstances[monkeytothrowto])

    def round(self):
        for itemI in range(len(self.items)):
            self.inspect(itemI)
        self.items = []


def spawnmonkeys(monkeydict):
    monkeys = []
    for monkeynum in monkeydict.keys():
            current = monkeydict[monkeynum]
            monkey = Monkey(monkeynum, current["startitems"], current["operation"],
                            current["test"], current["true"], current["false"])
            monkeys.append(monkey)
    return monkeys


def setmod():
    """Instead of dealing with huge numbers we just find the LCM of all of the divisions of each monkey and then modulo it"""
    mod = 1
    for monkey in Monkey.monkeyinstances:
        mod *= monkey.test
    Monkey.mod = mod

def part1():
    for _ in range(20):
        for monkey in Monkey.monkeyinstances:
            monkey.round()


def part2():
    setmod()
    for _ in range(10000):
        for monkey in Monkey.monkeyinstances:
            monkey.round()


def main():
    input = get_input()
    monkeydict = parsemonkeys(input)
    Monkey.monkeyinstances = spawnmonkeys(monkeydict)
    #part1()
    part2()
    inspectcounts = sorted([monkey.inspectcount for monkey in Monkey.monkeyinstances])[::-1][:2]
    print("Solution: " + str(inspectcounts[0] * inspectcounts[1]))


if __name__ == "__main__":
    main()

