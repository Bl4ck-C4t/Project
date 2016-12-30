import glob
from bin import *
import os

print("1. Binary\n2. Hex")
ch = input("Chose Encryption method: ")
if ch == "1":
    Hex = False
if ch == "2":
    Hex = True
print("1. All files\n2. Specific file")
ch = input("Choose file mode to decrypt: ")
if ch == "1":
    files = glob.glob("*.txt")
else:
    for x in glob.glob("*.txt"):
        print(x)
    files = [input("Enter filename: ")]
key = int(input("Key: "))
for x in files:
    chypher(x, key, Hex)
print("Encrypted.")
