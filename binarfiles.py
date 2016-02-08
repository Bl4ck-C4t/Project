from binartxt import *
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
