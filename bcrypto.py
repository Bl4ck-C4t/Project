import glob
from bin import *
import os
import pickle


def unpack(file="db.pl"):
    with open(file, "rb") as f:
        return pickle.load(f)


def pack(data, file="db.pl"):
    with open(file, "wb") as f:
        pickle.dump(data, f)

if not os.path.exists("db.pl"):
    f = open("db.pl", "w")
    f.close()
while True:
    print("1. Binary\n2. Hex\n3. Show logs\n4. Delete logs")
    ch = input("Chose Encryption method: ")
    if ch == "1":
        Hex = False
    if ch == "2":
        Hex = True
    elif ch == "3":
        if os.stat("db.pl").st_size == 0:
            print("No logs found.")
        else:
            dc = unpack()
            for x in dc.keys():
                print("{} - {}".format(x, dc[x]))
    elif ch == "4":
        with open("db.pl", "wb") as f:
            f.truncate()
        print("Logs deleted")
    if ch != "3" and ch != "4":
        break
print("1. All files\n2. Specific file")
ch = input("Choose file mode to decrypt: ")
if ch == "1":
    files = glob.glob("*.txt")
else:
    for x in glob.glob("*.txt"):
        print(x)
    files = [input("Enter filename: ")]
key = abs(int(input("Key: ")))
for x in files:
    chypher(x, key, Hex)
    if Hex:
        hx = "hex"
    else:
        hx = "bin"
    if os.stat("db.pl").st_size > 0:
        dc = unpack()
    else:
        dc = {}
    name = x + "(" + hx + ")"
    if name not in dc.keys():
        dc[name] = []
    dc[name].append(key)
pack(dc)
print("Encrypted.")
