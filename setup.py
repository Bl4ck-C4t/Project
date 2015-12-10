


class Setup:


    def __init__(self):
        self.acheats = False
        enter = input("What is your name? ")
        if enter == "import cheats":
            self.acheats = True
            print("Cheats activated")
            enter = input("What is your name? ")
        self.char_name = enter
        self.char_life = 30
        
        print("Hello " + enter)
        

    def wep(self):
        choice = input("What will be your weapon Sword, Axe, Bow? ")
        self.weapon = choice
        if choice == "Sword" or choice == "Axe" or choice == "Bow":
            print("You selected " + choice)
            self.isTrue = True
        else:
            print("You cannot select that!")
            self.isTrue = False
            
    def stats(self):
        self.wep_dmg = 0
        self.wep_range = 0
        if self.weapon == "Sword":
            self.wep_dmg = 5
            self.wep_range = 3
        elif self.weapon == "Axe":
            self.wep_dmg = 4
            self.wep_range = 2
        elif self.weapon == "Bow":
            self.wep_dmg = 3
            self.wep_range = 6


        
s = Setup()
s.wep()
while s.isTrue == False:
    s.wep()
s.stats()
print("Stats: Damage: {}, Range: {}, Life: {}".format(s.wep_dmg, s.wep_range, s.char_life))
if s.acheats == True:
    from cheats import Cheats1
    c = Cheats()
ask = input("Do you want to start a adventure? (y/n)")
if ask == "y":
     s.stats()
else:
    print("Goodbye then!")
    exit()
