def b2i(binary):
    num = str(binary)
    ls = num
    ls = ls[::-1]
    a = 0
    fn = 0
    for x in ls:
        if int(x) == 1:
            fn += pow(2, a)
            a += 1
        else:
            a += 1
    return str(fn)


   
def i2b(integer):
    num = str(integer)
    nm = int(num)
    fn = ""
    while nm != 0:
        if nm % 2 == 0:
            fn = fn + "0"
            nm = nm / 2
            nm = int(nm)
        else:
            nm = nm / 2
            nm = int(nm)
            fn = fn + "1"
    while len(fn) < 8:
        fn += "0"
    fn = fn[::-1]
    return str(fn)

def chypher(name, key):
    filename = name
    f = open(filename, "r+")
    info = f.read()
    f = open(filename, "w")
    f.truncate()
    f.write(te(info, key))
    f.close()
    print("File crypted.")

def dechypher(name, key):
    filename = name
    f = open(filename, "r+")
    info = f.read()
    f = open(filename, "w")
    f.truncate()
    f.write(td(info, key))
    f.close()
    print("File decrypted.")

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

