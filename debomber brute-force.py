import glob
import re
from bin import *


def check_chars(word):
    word += " "
    word = word.lower()
    word = word[:word.index(" ")]
    for char in word:
        if not(ord("a") <= ord(char) <= ord("z")):
            return False
    return True


alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper() + "0123456789`!@#$%^&*()-=_+<>?:;,./[]{}"
print("1.Key\n2. Brute-force")
select = input("Select option: ")
if select == "1":
    key = int(input("Key: "))
    for x in glob.glob("*.txt"):
        f = open(x, "r+")
        txt = f.read()
        f.close()
    txt = b2t(txt, key)
    print("Text found:\n" + txt)
    ch = input("Write text to file?(y/n): ")
    if ch == "y":
        for x in glob.glob("*.txt"):
            dechypher(x, key)
            print("Decrypted.")
elif select == "2":
    for x in glob.glob("*.txt"):
        f = open(x, "r+")
        start = f.read()
        f.close()
    for ch1 in alpha:
        abc = start
        check = start
        keys = []
        state = False
        while True:
            if not state:
                first_two = re.search(r"(\d+)\$(\d+)\$", check)
                first = int(b2i(first_two.group(1)))
                second = int(b2i(first_two.group(2)))
                key = first - ord(ch1[0])
                try:
                    check = b2t(check, key)
                except ValueError:
                    break
            if check[:len(ch1)] != ch1 or key < 0 or state:
                if state:
                    state = False
                check = abc
                last = b2i(re.search(r"(\d+)\$$", check).group(1))
                last = int(last)
                key = last - 36
                keys.append(key)
                try:
                    check = b2t(check, key)
                except ValueError:
                    break
                abc = check
            else:
                print("Text found:\n{}".format(check))
                print("Try: " + ch1)
                if not check_chars(check):
                    ch = "y"
                else:
                    ch = input("Continue Decryption(y/n)?: ")
                if ch == "n":
                    keys.append(key)
                    break
                else:
                    state = True
        else:
            continue
        ks = ""
        keys.reverse()
        for x in keys:
            ks += str(x) + ", "
        ks = ks[:-2]
        print("{} Keys found: {}".format(len(keys), ks))
        print("Text found:\n{}".format(check))
        print("Try: " + ch1)
        if check != start and check[0] == ch1[0] and check_chars(check):
            chose = input("Continue with next try?(y/n): ")
        else:
            chose = "y"
        if chose == "y":
            continue
        ch = input("Would you like to write text to file?(y/n): ")
        if ch == "y":
            for x in glob.glob("*.txt"):
                f = open(x, "w")
                f.write(check)
                f.close()
            print("Text written.")
        print("Bye")
        break
