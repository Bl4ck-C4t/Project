import random
num = random.randint(1000,4000)
while len(str(num)) != len(set(str(num))):
    num = random.randint(100,999)
print("The number is " + str(len(str(num))) + " digits long.")
guess = ""
nm = str(num)
while guess != num:
    cows = 0
    bulls = 0
    guess = int(input("Enter number: "))
    if guess == -1:
        print(num)
    gs = str(guess)
    c = list(zip(nm,gs))
    for x,y in c:
        if x == y:
            bulls += 1
    for z in gs:
        times = nm.count(z)
        cows += times
    cows -= bulls
    print("Bulls: " + str(bulls))
    print("Cows: " + str(cows))
else:
    print("The number was {}. You won!!".format(num))
