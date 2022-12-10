"""I'm not even going to bother cleaning up this monstrosity, I spent enough time making a clean pt2 and now my head hurts"""

def getinput():
    with open("input.txt") as f:
        lines = f.readlines()
        lines = [x[:-1] for x in lines]  # strips \n
        return lines


def main():
    input = getinput()
    tailpositions = set()
    tailpositionsL = []
    cheadpos = (0, 0)
    ctailpos = (0, 0)
    headposL = []
    for move in input:
        movez = move.split(" ")
        direction = movez[0]
        amount = int(movez[1])
        x, y = cheadpos
        tailx, taily = ctailpos
        if direction == "L":
            x = x-amount
            cheadpos = (x, y)
            headposL.append(cheadpos)
            if tailx > x:
                diffx = tailx - x
            else:
                diffx = x - tailx
            if taily > y:
                diffy = taily - y
            else:
                diffy = y - taily
            if diffx < 2 and diffy < 2:
                pass
            elif diffx > 1:
                for i in range(tailx-1, x, -1):
                    ctailpos = (i, y)
                    tailpositions.add(ctailpos)
                    tailpositionsL.append(ctailpos)

        elif direction == "R":
            x = x+amount
            cheadpos = (x, y)
            headposL.append(cheadpos)
            if tailx > x:
                diffx = tailx - x
            else:
                diffx = x - tailx
            if taily > y:
                diffy = taily - y
            else:
                diffy = y - taily
            if diffx < 2 and diffy < 2:
                pass
            elif diffx > 1:
                for i in range(tailx+1, x):
                    ctailpos = (i, y)
                    tailpositions.add(ctailpos)
                    tailpositionsL.append(ctailpos)

        elif direction == "U":
            y = y + amount
            cheadpos = (x, y)
            headposL.append(cheadpos)
            if tailx > x:
                diffx = tailx - x
            else:
                diffx = x - tailx
            if taily > y:
                diffy = taily - y
            else:
                diffy = y - taily
            if diffx < 2 and diffy < 2:
                pass
            elif diffy > 1:
                for i in range(taily+1, y):
                    ctailpos = (x, i)
                    tailpositions.add(ctailpos)
                    tailpositionsL.append(ctailpos)

        elif direction == "D":
            y = y - amount
            cheadpos = (x, y)
            headposL.append(cheadpos)
            if tailx > x:
                diffx = tailx - x
            else:
                diffx = x - tailx
            if taily > y:
                diffy = taily - y
            else:
                diffy = y - taily
            if diffx < 2 and diffy < 2:
                pass
            elif diffy > 1:
                for i in range(taily-1, y, -1):
                    ctailpos = (x, i)
                    tailpositions.add(ctailpos)
                    tailpositionsL.append(ctailpos)

        tailpositions.add(ctailpos)
        tailpositionsL.append(ctailpos)
    print("Tail of the rope visits this many points at least once: " + str(len(tailpositions)))


if __name__ == "__main__":
    main()

