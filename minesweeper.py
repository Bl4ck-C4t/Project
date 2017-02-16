import random
import re


def ratio(n1, n2, n3):
    return int((n2*n3)/n1)


def print_map(fl):  # ┏ ┑┖ ┚─
    head = "  "
    for x in range(1, len(fl[0]) + 1):
        head += str(x) + " "
    print(head)
    head = "  " + "_ "*(len(fl[0]))
    print(head)
    for x in range(1, len(fl) + 1):
        print(str(x) + "|" + " ".join(fl[x-1]) + "|")


def num_set(x, y, fl):
    bombs = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == 0 and b == 0:
                continue
            if x+a >= 0 and y+b >= 0:
                try:
                    if fl[x+a][y+b] == "X":
                        bombs += 1
                except IndexError:
                    pass
    return str(bombs)


def destroy(x, y, fl, curr):
    curr[x][y] = "0"
    done = True
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == 0 and b == 0:
                continue
            if x + a >= 0 and y + b >= 0:
                try:
                    if curr[x+a][y+b] != fl[x+a][y+b]:
                        curr[x+a][y+b] = fl[x+a][y+b]
                        done = False
                except IndexError:
                    pass
    if done:
        return
    for a in range(-1, 2):
        for b in range(-1, 2):
            if x + a >= 0 and y + b >= 0:
                try:
                    if curr[x + a][y + b] == "0":
                        destroy(x + a, y + b, fl, curr)
                except IndexError:
                    pass


def won(curr, fl):
    st1 = True
    st2 = True
    for x in range(len(fl)):
        for y in range(len(fl[x])):
            if fl[x][y] == "X" and curr[x][y] != "?":
                st1 = False
                break
        if not st1:
            break

    for x in range(len(fl)):
        for y in range(len(fl[x])):
            if fl[x][y] != "X" and curr[x][y] != fl[x][y]:
                st2 = False
                break
        if not st2:
            break

    return st1 or st2


rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
fl = [["O" for x in range(cols)] for x in range(rows)]
curr = [["P" for x in range(cols)] for x in range(rows)]
S = rows*cols
bombs = ratio(9, 2, S)
for z in range(bombs):
    x = random.randint(0, rows-1)
    y = random.randint(0, cols-1)
    while fl[x][y] == "X":
        x = random.randint(0, rows-1)
        y = random.randint(0, cols-1)
    fl[x][y] = "X"

for x in range(len(fl)):
    for y in range(len(fl[x])):
        if fl[x][y] == "O":
            fl[x][y] = num_set(x, y, fl)

dn = False
for x in range(len(fl)):
    for y in range(len(fl[x])):
        if fl[x][y] == "0":
            destroy(x, y, fl, curr)
            dn = True
            break
    if dn:
        break


while True:
    print_map(curr)
    cords = input("Enter Row,Column(M:Row,Column - to mark/unmark a bomb): ")
    cords = re.search(r"(?P<mark>M:)?(?P<x>\d+),(?P<y>\d+)", cords)
    x = int(cords.group("x")) - 1
    y = int(cords.group("y")) - 1
    mark = cords.group("mark") == "M:"
    square = fl[x][y]
    curr_sq = curr[x][y]
    if not mark:
        if square == "X":
            print_map(fl)
            print("Game Over.")
            exit()
        elif square != "X" and square != "0":
            curr[x][y] = square
        elif square == "0":
            destroy(x, y, fl, curr)
    else:
        if curr_sq == "?":
            curr[x][y] = "P"
        else:
            curr[x][y] = "?"
    if won(curr, fl):
        print_map(fl)
        print("YOU WON!!")
        break
