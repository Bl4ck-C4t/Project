import glob
from bin import *

print("1. Binary\n2. Hex")
ch = input("Chose Encryption method: ")
if ch == "1":
    Hex = False
if ch == "2":
    Hex = True
key = int(input("Key: "))
for x in glob.glob("*.txt"):
    chypher(x, key, Hex)

