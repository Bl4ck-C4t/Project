import glob
def asci(txt):
    enter = txt
    aa = ""
    c = 0
    for x in enter:
        try:
            aa += chr(ord(str(x)) - c)
        except ValueError:
            aa += x
        c += 1
    return aa

for x in glob.glob("*.txt"):
    f = open(x, "r+")
    file = f.read()
    f = open(x, "w")
    f.truncate()
    f.write(asci(file))
    f.close()

for x in glob.glob("asd.py"):
    f = open(x)
    file = f.read()
    f = open(x, "w")
    f.truncate()
    f.write(asci(file))
    f.close()


print("File encrypted.")
