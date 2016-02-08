import glob
from bin import *
key  = int(input("Key: "))
for x in glob.glob("*.txt"):
    dechypher(x, key)

