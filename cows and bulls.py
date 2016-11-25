import random
def cow_find(it1,it2):
    c = 0
    for x in it1:
        for y in range(len(it2)):
            if x == it2[y] and it2[y] != it1[y]:
                c += 1
    return c
def bull_find(it1,it2):
    bulls = 0
    c = list(zip(it1,it2))
    for x,y in c:
        if x == y:
            bulls += 1
    return bulls
ln = int(input("Enter secret number's length: "))
attempts = int(input("Enter attempts: "))
rep = input("Do you want to have same digits in the secret number?(y/n): ")
att = attempts
n1 = 10**(ln-1)
n2 = int("9"*ln)
num = random.randint(n1,n2)
if rep == "n":
    while len(str(num)) != len(set(str(num))):
        num = random.randint(n1,n2)
print("The number is " + str(len(str(num))) + " digits long.")
num = 1231
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
        attempts += 1
        continue
    gs = str(guess)
    bulls += bull_find(gs,nm)
    cows += cow_find(gs,nm)
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
    if att - attempts <= att/2:
        print("Wow that luck/cheat brah!!!")
input("Press any key to exit...")
