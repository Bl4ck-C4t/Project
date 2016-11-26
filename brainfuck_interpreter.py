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
    if x == "-":
        ind[curr] -= 1
        if ind[curr] < 0:
            ind[curr] = 0
    if x == ">":
        curr += 1
        try:
            ind[curr]
        except IndexError:
            ind.append(0)
    if x == "<":
        curr -= 1
        if curr < 0:
            ind.insert(0,0)
            curr = 0
    if x == ".":
        asd += chr(ind[curr])
    if x == ",":
        if string == "":
            string = input()
        try:
            ind[curr] = ord(string[str_ind])
        except:
            ind[curr] = 0
        str_ind += 1
    if x == "[":
        loop_start = point
        loop_end = info[point:].index("]")
    if x == "]":
        if ind[curr] != 0:
            point = loop_start
    if x == "*":
        print(ind[curr])
    point += 1
print(asd)
print("DONE")
