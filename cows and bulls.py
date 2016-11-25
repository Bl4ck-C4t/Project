import random
ln = int(input("Enter secret number's length: "))
attempts = int(input("Enter attempts: "))
rep = input("Do you want to have same digits in the secret number?(y/n): ")
att = attempts
n1 = 10*(ln-1)
n2 = int("9"*ln)
num = random.randint(n1,n2)
if rep == "n":
    while len(str(num)) != len(set(str(num))):
        num = random.randint(n1,n2)
print("The number is " + str(len(str(num))) + " digits long.")
guess = ""
nm = str(num)
pl = True
while guess != num:
    if attempts == 0:
        print("You lost :( The number was " + nm)
        break
    cows = 0
    bulls = 0
    if pl:
        print("Player 1 turn")
    else:
        print("Player 2 turn")
    pl = not(pl)
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
    attempts -= 1
    print("Attempts: {}".format(attempts))
else:
    pl = not(pl)
    if pl:
        player = "Player 1"
    else:
        player = "Player 2"
    print("The number was {}. {} won!!".format(num,player))
    print("You won in {} attempts".format(att-attempts))
    if att - attempts <= 4:
        print("Wow that luck/cheat brah!!!")

