


class Setup:

    buff = 0
    def __init__(self):
        self.wallet = 0
        self.mon_killed = 6
        self.back = []
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
        self.item = None
        
        if choice == "Sword" or choice == "Axe" or choice == "Bow":
            print("You selected " + choice)
            self.backpack(self.weapon)
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
            self.wep_range = 4
        elif self.weapon == "Bow":
            self.wep_dmg = 3
            self.wep_range = 6

    def backpack(self, item):
        elif len(self.back) == 5:
            print("No Space for the " + weapon)
            choice = input("Do you want to remove an item? y/n")
            if choice == "n":
                 print("You decided to leave the " + weapon)
                 weapon = ""
            elif choice == "y":
                for x in enumerate(self.back, start=1):
                    print(str(x[0]) + ". " + x[1])
                en = input("Type number of item to remove: ")
                print("You have removed " + str(self.back[en -1]))
                del self.back[en - 1]
                self.backpack(weapon)
        self.back.append(item)
        print(item + " has been added to your backpack('b')")
        i = input("Continue? ")
        if i == "b":
            self.view_backpack()
        
    def view_backpack(self):
        print("Items: ")
        for x in enumerate(self.back, start=1):
            print(str(x[0]) + ". " + x[1])
        enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
        if enter == "m":
            print("You have " + str(self.wallet) + " money.")
            enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
        while enter != "e":
            if enter == "veq":
                print("Weapon: {}, Item: {}".format(self.weapon, self.item))
                enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
                if enter == "m":
                    print("You have " + str(self.wallet) + " money.")
                    enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
                if enter == "e":
                    break
            self.get_item(self.back[int(enter) - 1])
            enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
            if enter == "veq":
                print("Weapon: {}, Item: {}".format(self.weapon, self.item))
            if enter == "m":
                print("You have " + str(self.wallet) + " money.")
                enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")      
            if enter == "eq":
                self.equip_item(self.check)
                for x in enumerate(self.back, start=1):
                    print(str(x[0]) + ". " + x[1])
                enter = input("Type item number to view, 'e' for exit, 'eq' to equip, 'veq' - to view equiped and 'm' to see money. ")
            
            

    def get_item(self, item):
        self.check = item
        if item == "Sword":
            wep_dmg = 5
            wep_range = 3
            wep_type = "Weapon"
        elif item == "Axe":
            wep_dmg = 4
            wep_range = 4
            wep_type = "Weapon"
        elif item == "Bow":
            wep_dmg = 3
            wep_range = 6
            wep_type = "Weapon"
        elif item == "Mace":
            wep_dmg = 5
            wep_range = 4
            wep_type = "Weapon"
        elif item == "Ranger":
            wep_dmg = None
            wep_range = None
            wep_type = "Item, increases range by 3"
        elif item == "Magic Knuckles":
            wep_dmg = 6
            wep_range = 3
            wep_type = "Weapon"
        elif item == "Ring of Regeneration":
            wep_dmg = None
            wep_range = None
            wep_type = "Item, adds 2 life on monster kill."
        elif item == "Potion of Life":
            wep_dmg = None
            wep_range = None
            wep_type = "Item, gives 5 extra life"
        print("Stats for {}: Range: {}, Damage: {}, Type: {}".format(item, wep_range, wep_dmg, wep_type))

    def equip_item(self, item):
        
        if item == "Sword":
            self.wep_dmg = 5
            self.wep_range = 3
            self.weapon = "Sword"
        elif item == "Axe":
            self.wep_dmg = 4
            self.wep_range = 4
            self.weapon = "Axe"
        elif item == "Bow":
            self.wep_dmg = 3
            self.wep_range = 6
            self.weapon = "Bow"
        elif item == "Mace":
            self.wep_dmg = 5
            self.wep_range = 4
            self.weapon = "Mace"
        elif item == "Ranger":
            self.wep_range = self.wep_range + 3
            self.item = "Ranger"
        elif item == "Magic Knuckles":
            self.wep_dmg = 6
            self.wep_range = 3
            self.weapon = "Magic Knuckles"
        elif item == "Ring of Regeneration":
            self.buff = 2
            self.item = "Ring of Regeneration"
        elif item == "Potion of Life":
            self.char_life += 5
            self.back.remove("Potion of Life")
        
        print("You have equiped/used " + item)
        print("Stats: Damage: {}, Range: {}, Life: {}".format(s.wep_dmg, s.wep_range, s.char_life))

    def item_drop(self):
        item = random.randint(1, 8)
        if item == 1:
            weapon = "Sword"
        elif item == 2:
            weapon = "Axe"
        elif item == 3:
            weapon = "Bow"
        elif item == 4:
            weapon = "Mace"
        elif item == 5:
            weapon = "Ranger"
        elif item == 6:
            weapon = "Magic Knuckles"
        elif item == 7:
            weapon = "Ring of Regeneration"
        elif item == 8:
            weapon = "Potion of Life"
        print("You found " + weapon)
        enter = input("Do you want to keep it? y/n ")
        if enter == "Yes" or enter == "y" and len(self.back) < 5:
            self.backpack(weapon)
        elif enter == "n" or enter == "no":
            print("You decided to leave the " + weapon)
            weapon = ""
        

        
s = Setup()
s.wep()


class Cheats1:

    def __init__(self):
        a = True
        while a:
            ent = input("Select cheat: all, weapon, health, exit, vill: ")
            if ent == "weapon":
                s.wep_dmg = int(input("Weapon Damage: "))
                s.wep_range = int(input("Weapon Range: "))
                print("Stats: Damage: {}, Range: {}".format(s.wep_dmg, s.wep_range))
                
            if ent == "health":
                s.char_life = int(input("Life: "))
                print("Stats: Damage: {}, Range: {}, Life {}".format(s.wep_dmg, s.wep_range, s.char_life))

            if ent == "all":
                s.wep_dmg = int(input("Weapon Damage: "))
                s.wep_range = int(input("Weapon Range: "))
                s.char_life = int(input("Life: "))
                s.weapon = input("Weapon name: ")
                print("Stats: Damage: {}, Range: {}, Life {}".format(s.wep_dmg, s.wep_range, s.char_life))
                print("You selected " + s.weapon)
            if ent == "exit":
                a = False
            if ent == "vill":
                s.mon_killed = 6
                ch = Combat
                ch.victory()
                
                
while s.isTrue == False:
    s.wep()
s.stats()
print("Stats: Damage: {}, Range: {}, Life: {}".format(s.wep_dmg, s.wep_range, s.char_life))
if s.acheats == True:
    c = Cheats1()
ask = input("Do you want to start a adventure? (y/n)")
if ask == "n":
    print("Goodbye then!")
    exit()


import random
import time



class Mapa: 
    
    
    def chmonster(self):
        self.monster = ""
        mon = random.randint(1, 3)
        if mon == 1:
            self.monster = "Bat"
        elif mon == 2:
            self.monster = "Zombie"
        elif mon == 3:
            self.monster = "Gnom"
        print("A " + self.monster + " attacked you!")

    def ch1monster(self):
        self.monster = ""
        mon = random.randint(1, 3)
        if mon == 1:
            self.monster = "Bat1"
        elif mon == 2:
            self.monster = "Zombie1"
        elif mon == 3:
            self.monster = "Gnom1"
        print("A " + self.monster + " attacked you!")
        
        
    
    
    def __init__(self):
        print("Starting an adventure..")
        time.sleep(1.5)
    
m = Mapa()
m.chmonster()


class Village:

    def __init__(self):
        print("So you came accross a village, huh?")
        print("The villagers healed you and offerd you some stuff.")
        if s.char_life < 30:
            s.char_life = 30
        self.menu()
        
        
    def menu(self):
        print("Welcome to our store!")
        en = input("Select 'buy' or 'sell' items?('e' for exit) ")
        if en == "buy":
            self.buy()
        elif en == "sell":
            self.sell()
        elif en == "e":
            print(self.back)
            print("Bye")

    
    def buy(self):
        wep_ls = []
        price_ls = []
        c = 0
        while c < 4:
            rd = random.randint(1, 8)
            if rd == 1:
                wep_ls.append("Sword")
                price_ls.append(4)
                c += 1
            elif rd == 2:
                wep_ls.append("Axe")
                price_ls.append(4)
                c += 1
            elif rd == 3:
                wep_ls.append("Bow")
                price_ls.append(4)
                c += 1
            elif rd == 4:
                wep_ls.append("Mace")
                price_ls.append(5)
                c += 1
            elif rd == 5:
                wep_ls.append("Ranger")
                price_ls.append(7)
                c += 1
            elif rd == 6:
                wep_ls.append("Magic Knuckles")
                price_ls.append(9)
                c += 1
            elif rd == 7:
                wep_ls.append("Ring of Regeneration")
                price_ls.append(8)
                c += 1
            elif rd == 8:
                wep_ls.append("Potion of Life")
                price_ls.append(5)
                c += 1
        zx = list(zip(enumerate(wep_ls, start=1), price_ls))
        for x in zx:
            print(str(x[0][0]) + "." + x[0][1] + " - " + str(x[1]) + " money")
            print("You have " + str(s.wallet))
        enter = input("Type the number of the item you wanna buy or 'e' for exit.")
        while enter != "e":
            if enter != "e":
                s.back.append(zx[int(enter) - 1][0][1])
                s.wallet -= zx[int(enter) - 1][1]
                print("You pruchased " + zx[int(enter) - 1][0][1])
                print("You now have " + str(s.wallet))
                enter = input("Type the number of the item you wanna buy or 'e' for exit.")
                if enter == "e":
                    e = input("Do you want new items for 5 money? y/n ")
                    if e == "y":
                        s.wallet -= 5
                        self.buy()
                    else:
                        self.menu()
            elif enter == "e":
                e = input("Do you want new items for 5 money? y/n ")
                if e == "y":
                    self.buy()
                else:
                    self.menu()
        if enter == "e":
            self.menu()

                
    def sell(self):
        c = 1
        for x in s.back:
            if x == "Sword":
                print(str(c)+ "." + x + " costs 4")
                cost = 4
                c += 1
            if x == "Axe":
                print(str(c)+ "." + x + " costs 4")
                cost = 4
                c += 1
            if x == "Bow":
                print(str(c)+ "." + x + " costs 4")
                cost = 4
                c += 1
            if x == "Mace":
                print(str(c)+ "." + x + " costs 5")
                cost = 5
                c += 1
            if x == "Ranger":
                print(str(c)+ "." + x + " costs 7")
                cost = 7
                c += 1
            if x == "Magic Knuckles":
                print(str(c)+ "." + x + " costs 9")
                cost = 9
                c += 1
            if x == "Ring of Regeneration":
                print(str(c)+ "." + x + " costs 8")
                cost = 8
                c += 1
            if x == "Potion of Life":
                print(str(c)+ "." + x + " costs 5")
        enter = input("Do you want to sell anything?(type number)")
        if enter != "e":
            if s.back[int(enter) - 1] == "Sword":
                cost = 4
            if s.back[int(enter) - 1] == "Axe":
                cost = 4
            if s.back[int(enter) - 1] == "Bow":
                cost = 4
            if s.back[int(enter) - 1] == "Mace":
                cost = 5
            if s.back[int(enter) - 1] == "Ranger":
                cost = 7
            if s.back[int(enter) - 1] == "Magic Knuckles":
                cost = 9
            if s.back[int(enter) - 1] == "Ring of Regeneration":
                cost = 8
            if s.back[int(enter) - 1] == "Potion of Life":
                cost = 5
            s.wallet += cost
            print("You sold " + s.back[int(enter) - 1])
            del s.back[int(enter) - 1]
            self.sell()
        elif enter == "e":
            self.menu()        
   


class Combat:

        
        def __init__(self):
            
            print("You selcted to attack")
            if m.monster == "Bat":
                self.mon_life = 3
                self.mon_attack = 2
                self.mon_luck = 3
                self.worth = 2
            elif m.monster == "Zombie":
                 self.mon_life = 5
                 self.mon_attack = 4
                 self.mon_luck = 4
                 self.worth = 4
            elif m.monster == "Gnom":
                 self.mon_life = 4
                 self.mon_attack = 3
                 self.mon_luck = 2
                 self.worth = 3
            elif m.monster == "Bat1":
                m.monster = "Bat"
                self.mon_life = 4
                self.mon_attack = 3
                self.mon_luck = 3
                self.worth = 4
            elif m.monster == "Zombie1":
                m.monster = "Zombie"
                self.mon_life = 6
                self.mon_attack = 4
                self.mon_luck = 4
                self.worth = 8
            elif m.monster == "Gnom1":
                m.monster = "Gnom"
                self.mon_life = 5
                self.mon_attack = 6
                self.mon_luck = 3
                self.worth = 6

            
            print("The " + m.monster + " is attacking.")
            
        def monster_attack(self):
                luck = random.randint(0,  10)
                if self.mon_life <= 0:
                    self.victory()
                elif luck <= self.mon_luck:
                    s.char_life -= random.randint(0, self.mon_attack)
                    print("The " + m.monster + " hit you dealing " + str(self.mon_attack) + " health from you.")
                    print("You life now is " + str(s.char_life))
                    en1 = input("Attack or Run?('b' for backpack) ")
                    while en1 != "Attack" and en1 != "attack" and en1 != "a" and en1 != "Run": 
                        if en1 == "Run":
                            self.run()
                        elif en1 == "b":
                            s.view_backpack()
                            en1 = input("Attack or Run?('b' for backpack) ")
                    if en1 == "a" or en1 == "attack" or en1 == "Attack":
                        self.char_attack()             
                elif luck => self.mon_luck:
                    print("The monster missed")
                    en = input("Attack or Run?('b' for backpack) ")
                    while en != "Attack" and en != "attack" and en != "a" and en != "Run":
                        if en == "Run":
                            self.run()
                        elif en == "b":
                            s.view_backpack()
                            en = input("Attack or Run?('b' for backpack) ")
                    if en == "a" or en == "attack" or en == "Attack":
                        self.char_attack()
        
        def char_attack(self):
            self.char_luck = random.randint(0, 10)
            if self.mon_life <= 0:
                self.victory()
            elif self.char_luck <= s.wep_range:
                self.mon_life -= random.randint(0, random.randint(1, s.wep_dmg)
                if self.mon_life <= 0:
                    self.victory()
                print("You hit your enemy and now his health is " + str(self.mon_life))
                self.monster_attack()
            elif self.char_luck => s.wep_range:
                print("You missed.")
                self.monster_attack()

        def victory(self):
            print("You have beaten the " + m.monster + "('b' for backpack)")
            print("You won " + str(self.worth) + " for killing it")
            s.wallet += self.worth
            s.mon_killed += 1
            s.char_life += self.mon_luck + s.buff
            print("You life now is " + str(s.char_life))
            a = input("Continue? y/n ")
            s.item_drop()
            if s.mon_killed == 6:
                print("You have enough items to trade with and you decided to go to the nearest village.")
                choice = input("Do you want to go? y/n ")
                if choice == "y":
                    v = Village()
                    exit()
                elif choice == "n":
                    a = input("Continue? y/n ")
                    s.mon_killed = 0
            while a != "y" and a != "":
                if a == "b":
                    s.view_backpack()
                    a = input("Continue? y/n ")
            m.chmonster()
            enter = input("Attack or Run?('b' for backpack) ")
            while enter != "Attack" and enter != "attack" and enter != "a" and enter != "Run":
                if enter == "b":
                    s.view_backpack()
                    enter = input("Attack or Run?('b' for backpack) ")
                elif enter == "Run" or enter == "r":
                    ch.run()
                    m.chmonster()
            if enter == "a" or enter == "attack" or enter == "Attack":
                ch = Combat()
                ch.monster_attack()

        def run(self):
            luck = random.randint(2, 4)
            if luck == self.mon_luck:
                    s.char_life -= self.mon_attack
                    print("The " + m.monster + " hit you dealing " + str(self.mon_attack) + " health from you.")
                    print("You life now is " + str(s.char_life))
                    if s.char_life > 0:
                        print("You succesfully escaped from the " + m.monster)
            else:
                print("The " + m.monster + " missed.")
                print("You succesfully escaped from the " + m.monster)    

                  
    enter = input("Attack or Run?('b' for backpack) ")
    while enter != "Attack" and enter != "attack" and enter != "a" and enter != "Run":
        if enter == "b":
            s.view_backpack()
            enter = input("Attack or Run?('b' for backpack) ")
        elif enter == "Run" or enter == "r":
            ch.run()
            m.chmonster()
    if enter == "a" or enter == "attack" or enter == "Attack" and s.mon_killed < 6:
        ch = Combat()
        ch.monster_attack()
    elif enter == "a" or enter == "attack" or enter == "Attack" and s.mon_killed > 6:
        m.ch1monsters()
        ch = Combat()
        ch.monster_attack()




