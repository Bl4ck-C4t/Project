from bin import *
def te(string, key):
    enter = string
    fn = ""
    for x in enter:
        y = ord(x) + key
        y = i2b(y)
        fn += y
        fn += "$"
    return fn

def td(binary, key):
    enter = binary
    mes = ""
    part = ""
    c = 0
    while c < len(enter) - 1:
        while enter[c] != "$":
            part += enter[c]
            c += 1
        mes += chr(int(b2i(part)) - key)
        c += 1
        part = ""
    return mes
