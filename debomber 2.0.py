import glob
import re
from bin import *

print("1. Binary\n2. Hex")
ch = input("Chose Encryption method: ")
if ch == "1":
    Hex = False
    s2t = b2t
    t2s = t2b
    s2i = b2i
    i2s = i2b
if ch == "2":
    Hex = True
    s2t = h2t
    t2s = t2h
    s2i = h2i
    i2s = i2h
print("1.Key \n2.Beginning \n3.Ending")
select = input("Select option: ")
if select == "1":
    key = int(input("Key: "))
    for x in glob.glob("*.txt"):
        f = open(x, "r+")
        txt = f.read()
        f.close()
    txt = s2t(txt, key)
    print("Text found:\n" + txt)
    ch = input("Write text to file?(y/n): ")
    if ch == "y":
        for x in glob.glob("*.txt"):
            dechypher(x, key, Hex)
            print("Decrypted.")
elif select == "2":
    ch1 = input("Type first characters of file: ")
    print("Decrypting...")
    check = ""
    for x in glob.glob("*.txt"):
        f = open(x, "r+")
        start = f.read()
        abc = start
        check = start
        f.close()
    keys = []
    state = False
    while True:
        if not state:
            first_two = re.search(r"(\w+)\$(\w+)\$", check)
            first = int(s2i(first_two.group(1)))
            second = int(s2i(first_two.group(2)))
            key = first - ord(ch1[0])
            check = s2t(check, key)
        if check[:len(ch1)] != ch1 or key < 0 or state:
            if state:
                state = False
            check = abc
            last = s2i(re.search(r"(\w+)\$$", check).group(1))
            last = int(last)
            key = last - 36
            keys.append(key)
            check = s2t(check, key)
            abc = check
        else:
            print("Text found:\n{}".format(check))
            ch = input("Continue Decryption(y/n)?: ")
            if ch == "n":
                keys.append(key)
                break
            else:
                state = True
    ks = ""
    keys.reverse()
    for x in keys:
        ks += str(x) + ", "
    ks = ks[:-2]
    print("{} Keys found: {}".format(len(keys), ks))
    print("Text found:\n{}".format(check))
    ch = input("Would you like to write text to file?(y/n): ")
    if ch == "y":
        for x in glob.glob("*.txt"):
            f = open(x, "w")
            f.write(check)
            f.close()
        print("Text written.")
    print("Bye")
