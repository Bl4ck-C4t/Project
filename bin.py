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
