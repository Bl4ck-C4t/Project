import glob
from bin import *
print("1.Key \n2.Begining \n3.Ending")
select = input("Select option: ")
if select == "1":
    key  = int(input("Key: "))
    for x in glob.glob("*.txt"):
        dechypher(x,key)
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
    while check[:len(ch1)] != ch1:
        part = check[:check[1:].index("$") + 1]
        bi = b2i(part)
        c = ord(ch1[0])
        key = int(bi) - int(c)
        check = b2t(check, key)
        if check[:len(ch1)] != ch1:
            check = abc
            part = abc[::-1][1:][:abc[::-1][1:].index("$")][::-1]
            bi = b2i(part)
            key = int(bi) - ord("$")
            keys.append(key)
            abc = b2t(abc, key)
            check = abc
    keys.append(key)
    knum = 0
    kkk = ""
    keys.reverse()
    for x in keys:
        kkk += str(x) + ", "
        knum += 1
    print(str(knum) + " keys found: " + kkk)
    print("Message: " + check)
    choice = input("Write to file?(y/n): ")
    keys.reverse()
    if choice == "y":
        for x in glob.glob("*.txt"):
            f = open(x,"w")
            f.truncate()
            f.write(check)
            f.close()
        print("Decrypted.")









