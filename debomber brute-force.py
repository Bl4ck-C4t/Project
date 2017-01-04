import glob
import re
from bin import *
# TODO debug with Asci art.txt


def vaild(word, alpha):
    word += " "
    word = word.lower()
    word = word[:word.index(" ")]
    for char in word:
        if not(char in alpha):
            return False
    return True


def write(file, txt):
    with open(file, "w") as f:
        f.write(txt)

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
print("1. All files\n2. Specific file")
ch = input("Chose files mode to decrypt: ")
if ch == "1":
    files = glob.glob("*.txt")
else:
    for x in glob.glob("*.txt"):
        print(x)
    files = [input("Enter filename: ")]
print("1.Key\n2. Brute-force")
select = input("Select option: ")
if select == "1":
    key = int(input("Key: "))
    for x in files:
        f = open(x, "r+")
        txt = f.read()
        f.close()
    txt = s2t(txt, key)
    print("Text found:\n" + txt)
    ch = input("Write text to file?(y/n): ")
    if ch == "y":
        for x in files:
            dechypher(x, key, Hex)
            print("Decrypted.")
elif select == "2":
    for x in files:
        print("Decrypting " + x)
        with open(x, "r") as f:
            start = f.read()
        while True:
            print("1. Lower-alpha\n2. Upper alpha\n3. Mixed alpha\n4. Symbolic\n5. Numeric\n6. Mixed\n7. Custom"
                  "\n8. Text")
            ch = input("Choose alpha set: ")
            alpha = "abcdefghijklmnopqrstuvwxyz"
            symbols = " `'!@#$%^&*()-=_+<>?:;,./[]{}"
            numbers = "".join(str(x) for x in range(10))
            punct = "!.,?():;'"
            if ch == "1":
                pass
                break
            elif ch == "2":
                alpha = alpha.upper()
                break
            elif ch == "3":
                alpha += alpha.upper()
                break
            elif ch == "4":
                alpha = symbols
                break
            elif ch == "5":
                alpha = numbers
                break
            elif ch == "6":
                alpha += alpha.upper() + numbers + symbols
                break
            elif ch == "7":
                ls = []
                fn = ""
                out = False
                while True:
                    print("1. Lower alpha\n2. Upper alpha\n3. Numbers\n4. Symbols\n5. Custom character\n6. Range\n"
                          "7. Special\n8. Punctuation")
                    ch = input("Choose what to add('c' to cancel, 'f' to finish){}: ".format(ls))
                    if ch == "1":
                        fn += alpha
                        ls.append("Lower alpha")
                    elif ch == "2":
                        fn += alpha.upper()
                        ls.append("Upper alpha")
                    elif ch == "3":
                        fn += numbers
                        ls.append("Numbers")
                    elif ch == "4":
                        fn += symbols
                        ls.append("Symbols")
                    elif ch == "5":
                        sym = input("Enter symbol: ")
                        ls.append(sym)
                        fn += sym
                    elif ch == "6":
                        print("1. Lower alpha\n2. Upper alpha\n3. Numbers\n4. Symbols")
                        char = input("Enter charset: ")
                        if char == "1":
                            char = alpha
                        elif char == "2":
                            char = alpha.upper()
                        elif char == "3":
                            char = numbers
                        elif char == "4":
                            char = symbols
                        print(char)
                        rng = input("Enter range: ")
                        begin = char.index(rng[0])
                        end = char.index(rng[2])
                        fn += char[begin:end+1]
                        ls.append(rng)
                    elif ch == "7":
                        print("1. Hex\n2. Binary")
                        ch = input("Enter number of charset: ")
                        if ch == "1":
                            fn += "abcdef" + numbers
                            ls.append("hex")
                        if ch == "2":
                            fn += "01"
                            ls.append("binary")
                    elif ch == "8":
                        fn += punct
                        ls.append("Punctuation")
                    elif ch == "c":
                        break
                    elif ch == "f":
                        alpha = fn
                        out = True
                        break
                if out:
                    break
            elif ch == "8":
                alpha = alpha.upper() + alpha  + punct
                break

        for ch1 in alpha:
            abc = start
            check = start
            keys = []
            state = False
            state2 = False
            jump = False
            while True:
                if not state and not jump:
                    first_two = re.search(r"(\w+)\$(\w+)\$", check)
                    if first_two is None:
                        break
                    try:
                        first = int(s2i(first_two.group(1)))
                    except:
                        break
                    key = first - ord(ch1[0])
                    if key > 0:
                        try:
                            check = s2t(check, key)
                        except (ValueError, OverflowError) as e:
                            state2 = True
                            break
                if (check[0] != ch1 or key < 0 or state) and not jump:
                    if state:
                        state = False
                    check = abc
                    try:
                        last = s2i(re.search(r"(\w+)\$$", check).group(1))
                    except:
                        break
                    last = int(last)
                    key = last - 36
                    if key > 0:
                        keys.append(key)
                    else:
                        state2 = True
                        break
                    try:
                        check = s2t(check, key)
                        abc = check
                        if vaild(abc, alpha) and Hex:
                            jump = True
                    except ValueError:
                        state2 = True
                        break

                else:
                    if jump:
                        jump = False
                        """if check[0] != ch1[0]:
                            state2 = True
                            break"""
                    print("Text found:\n{}".format(check[:400]))
                    print("Try: " + ch1)
                    if check != start and check[0] == ch1[0] and vaild(check, alpha) and not state2:
                        ch = input("Continue Decryption(y/n)?: ")
                    elif check != start and check[0] != ch1[0] and vaild(check, alpha) and not state2:
                        state2 = True
                        break
                    else:
                        ch = "y"
                        state2 = False
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
            print("Text found:\n{}".format(check[:400]))
            print("Try: " + ch1)
            if check != start and check[0] == ch1[0] and vaild(check, alpha) and not state2:
                chose = input("Continue with next try?(y/n): ")
            else:
                chose = "y"
                state2 = False
            if chose == "y":
                continue
            ch = input("Would you like to write text to file?(y/n): ")
            if ch == "y":
                for y in files:
                    f = open(y, "w")
                    f.write(check)
                    f.close()
                print("Text written.")
            print("Bye")
            break
