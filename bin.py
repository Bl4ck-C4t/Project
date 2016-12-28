import re

def b2i(binary):
    ls = str(binary)
    ls = ls[::-1]
    a = 0
    fn = 0
    for x in ls:
        if int(x) == 1:
            fn += pow(2, a)
        a += 1
    return str(fn)

def i2h(integer):
    return hex(integer)[2:]

def h2i(Hex):
    Hex = Hex.upper()
    Hex = Hex[::-1]
    table = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    a = 0
    fn = 0
    for x in Hex:
        if x in table.keys():
            x = table[x]
        else:
            x = int(x)
        fn += (16**a)*x
        a += 1
    return fn

def i2b(integer):
    return bin(integer)[2:]

def chypher(name, key, Hex=False):
    filename = name
    f = open(filename, "r+")
    info = f.read()
    f = open(filename, "w")
    if not Hex:
        fn = t2b
    else:
        fn = t2h
    f.write(fn(info, key))
    f.close()

def dechypher(name, key, Hex=False):
    filename = name
    f = open(filename, "r+")
    info = f.read()
    f = open(filename, "w")
    f.truncate()
    if not Hex:
        fn = b2t
    else:
        fn = h2t
    f.write(b2t(info, key))
    f.close()

def t2b(string, key):
    enter = string
    fn = ""
    for x in enter:
        y = i2b(ord(x) + key)
        fn += y + "$"
    return fn

def b2t(binary, key):
    return re.sub(r"(\d+)\$",lambda x: chr(int(b2i(x.group(1))) - key),binary)

def t2h(string, key):
    encrypted = ""
    for x in string:
        encrypted += i2h(ord(x) + key) + "$"
    return encrypted

def h2t(Hex, key):
    return re.sub(r"(\w+)\$", lambda x: chr(h2i(x.group(1))- key), Hex)
