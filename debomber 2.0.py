import glob
import re

from bin import *
print("1.Key \n2.Beginning \n3.Ending")
select = input("Select option: ")
if select == "1":
    key = int(input("Key: "))
    for x in glob.glob("*.txt"):
        f = open(x, "r+")
        txt = f.read()
        f.close()
    print("Text found:\n" + txt)
    ch = input("Write text to file?(y/n): ")
    if ch == "y":
        for x in glob.glob("*.txt"):
            dechypher(x, key)
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
            first_two = re.search(r"(\d+)\$(\d+)\$", check)
            first = int(b2i(first_two.group(1)))
            second = int(b2i(first_two.group(2)))
            key = first - ord(ch1[0])
            check = b2t(check, key)
        if check[:len(ch1)] != ch1 or key < 0 or state:
            if state:
                state = False
            check = abc
            last = b2i(re.search(r"(\d+)\$$", check).group(1))
            last = int(last)
            key = last - 36
            keys.append(key)
            check = b2t(check, key)
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
