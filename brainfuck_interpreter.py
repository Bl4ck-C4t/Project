import re
import os
script_dir = os.path.dirname(__file__)
path = input("Enter filename: ")
path = "scripts/" + path
path = os.path.join(script_dir, path)
f = open(path,"r+")
info = f.read()
f.close()
info = "".join(info.split("\n"))
ind = [0]
curr = 0
point = 0
string = ""
str_ind = 0
loop_start = 0
loop_end = 0
asd = ""
while point < len(info):
    x = info[point]
    if x == "+":
        ind[curr] += 1
    elif x == "-":
        ind[curr] -= 1
        if ind[curr] < 0:
            ind[curr] = 0
    elif x == ">":
        curr += 1
        try:
            ind[curr]
        except IndexError:
            ind.append(0)
    elif x == "<":
        curr -= 1
        if curr < 0:
            ind.insert(0,0)
            curr = 0
    elif x == ".":
        asd += chr(ind[curr])
    elif x == ",":
        if string == "":
            string = input()
        try:
            ind[curr] = ord(string[str_ind])
        except:
            ind[curr] = 0
        str_ind += 1
    elif x == "[":
        loop_start = point
        loop_end = info[point:].index("]")
        if ind[curr] == 0:
            point = loop_end
    elif x == "]":
        if ind[curr] != 0:
            point = loop_start
    elif x == "/":
        asd += str(ind[curr])
    elif x == "!":
        ind[curr] = 0
    elif x == "(":
        clb = info[point:].index(")")
        part = info[point+1:clb]
        exp = re.search(r" *(-*\d+) *([><=]+) *(-*\d+): *(\d+) *\? *(\d+)",info)
        cell1 = exp.group(1)
        sign = exp.group(2)
        cell2 = exp.group(3)
        tr = exp.group(4)
        fl = exp.group(5)
        exp = str(ind[curr+int(cell1)]) + sign + str(ind[curr+int(cell2)])
        exp = eval(exp)
        if exp:
            ind[curr] = int(tr)
        else:
            ind[curr] = int(fl)
        point = clb
    elif x == "*":
        ind[curr] *= 2
    point += 1
print(asd)
print("DONE")
