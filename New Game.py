import random
from peewee import *
db = SqliteDatabase('save.db')


class Saved(Model):
    name = CharField()
    value = IntegerField()

    class Meta:
        database = db

class Saves(Model):
    name = CharField()
    value = CharField()

    class Meta:
        database = db

db.connect()

class Setup:

    def __init__(self):
        self.lod = "no"
        self.life = 100
        self.dmg = 3
        self.score = 0
        self.armor = 0
        self.ct =False
        self.at = False
        self.bt = False
        self.wt = False
        self.st = False
        self.qt = False
        self.n = input("what is your name? ")
        print("Hello, " + self.n)
        self.dif = input("Select difficulty: Easy, Normal, Hard, Insane? ")
        if self.dif == "Easy":
            self.dif = 1
        if self.dif == "Normal":
            self.dif = 2
        if self.dif == "Hard":
            self.dif = 3
        if self.dif == "Insane":
            self.dif = 4
        c = 0
        if not(Saves.table_exists()):
            db.create_tables([Saved, Saves])
        
        for x in Saves.select():
            c += 1
        if c > 0:
            self.lod = input("Do you want to reload last game " + Saves.get(Saves.name == 'user').value + " y/n/delete? ")
        for x in Saved.select():
            if x.name == 'high':
                print("The highest score for now is " + str(x.value))


class Tr:

    def Bear_trap(self):
        self.name = "Bear Trap"
        self.dmg = 20
      

    def Cage_trap(self):
        self.name = "Cage Trap"
        self.dmg = 10
        

    def Spike_trap(self):
        self.name = "Spike Trap"
        self.dmg = 40
        

    def Arrows_trap(self):
        self.name = "Arrows Trap"
        self.dmg = 60
        

    def Wall_trap(self):
        self.name = "Wall closing trap"
        self.dmg = 100
        

    def quicksand_trap(self):
        self.name = "Quicksand trap"
        self.dmg = 90
        

tr = Tr()
s = Setup()


class Items:

    def __init__(self):
        self.materials = ["Wood", "Stone", "Bronze", "Iron", "Silver", "Golden", "Platinium", "Obsidian", "Soul"]
        self.quality = ["Common", "Training", "Uncommon", "Rare", "Very Rare", "Legendary"]
        self.weapons = ["Club", "Bat", "Knife", "Dagger", "Kunai", "Shuriken", "Bow", "Sword", "Katana", "Magic"]
        self.armor = ["Hat", "Helmet", "Boots", "Chestplate", "Leggings", "Gloves", "Anti-Trap Armor set"]
        self.items = ["Potion of Life", "Book of Cages", "Book of Spikes", "Book of Bear Traps", "Book of Arrows", "Book of Quicksand", "Book of Walls"]

    def item_drop(self):
        luck = random.randint(-2, 3)
        if luck == 1:
            rw = random.randint(0, len(self.weapons) - 1)
            rq = random.randint(0, len(self.quality) - 1)
            rm = random.randint(0, len(self.materials) - 1)
            w = self.weapons[rw]
            q = self.quality[rq]
            m = self.materials[rm]
            new_wep = q + " " +  m + " " + w
            print("You found a " + new_wep)
            enter = input("Do you want to pick it up? ")
            if enter == "y":
                s.dmg = rq*2 + rm + rw
                print("You have equiped the " + new_wep)
            else:
                print("You left the weapon")
        elif luck == 2:
            ra = random.randint(0, len(self.armor) - 1)
            rq = random.randint(0, len(self.quality) - 1)
            rm = random.randint(0, len(self.materials) - 1)
            a = self.armor[ra]
            q = self.quality[rq]
            m = self.materials[rm]
            new_wep = q + " " +  m + " " + a
            print("You found a " + new_wep)
            enter = input("Do you want to pick it up? ")
            if enter == "y":
                s.armor = rq + rm*2 + ra
                print("You have equiped the " + new_wep)
        elif luck == 3:
            ri = random.randint(0, len(self.items) - 1)
            rq = random.randint(0, len(self.quality) - 1)
            i = self.items[ri]
            q = self.quality[rq]
            new_item = q + " " + i
            print("You found " + new_item)
            enter = input("Do you want to pick it up? ")
            if enter == "y":
                if i == "Potion of Life":
                    s.life += 10 + rq*10
                    print("You have drinked the Potion of Life.")
                    print("Now your life is " + str(s.life))
                else:
                    print("You now have " + new_item)
                    if ri == 1:
                        s.ct = True
                    if ri == 2:
                        s.st = True
                    if ri == 3:
                        s.bt = True
                    if ri == 4:
                        s.at = True
                    if ri == 5:
                        s.qt = True
                    if ri == 6:
                        s.wt = True
                    s.life += rq
            else:
                print("You left the item")
        else:
            print("No luck")

i = Items()
class Map:

    def __init__(self):
        self.s = False
        self.victory = False
        mp = str(2+s.dif) + "," + str(2+s.dif)
        c = 0
        w = ""
        h = ""
        for x in mp:
            if x == ",":
                h = int(h)
                w += mp[c+1:]
                w = int(w)
                break
            elif x != "," :
                h += x
                c += 1
        self.w = w
        self.h = h
        rny = random.randint(1, self.h - 1)
        rnx = random.randint(1, self.w - 1)
        self.pos_x = rnx
        self.pos_y = rny

    def traps(self):
        self.trps = []
       
        self.c = 0
        while self.c < ((self.h + self.w)/ 2) - 2:
            self.trap_x = random.randint(1, self.w - 1)
            self.trap_y = random.randint(0, self.h - 1)
            while (self.door_x == self.trap_x and self.door_y == self.trap_y) or (self.pos_x == self.trap_x and self.pos_y == self.trap_y):
                self.trap_x = random.randint(1, self.w - 1)
                self.trap_y = random.randint(0, self.h - 1)
            self.trps.append(self.trap_x)
            self.trps.append(self.trap_y)
            self.c += 1
        
    def door(self):
        self.door_x = random.randint(1, self.w - 1)
        self.door_y = random.randint(0, self.h - 1)
        while self.door_x == self.pos_x and self.door_y == self.pos_y:
            self.door_x = random.randint(1, self.w - 1)
            self.door_y = random.randint(0, self.h - 1)

    def update(self):
        rnx = self.pos_x
        rny = self.pos_y
        w = self.w
        h = self.h
        c = 0
        print("Level " + str(s.score + 1))
        while c < h:
             if c == rny:
                 print(" _  "*w); print("| | "*((w - (w - rnx)) - 1) + "|X| " + "| | "*(w-rnx)); print(" ¯  "*w)
                 c += 1
             else:
                 print(" _  "*w); print("| | "*w); print(" ¯  "*w)
                 c += 1
        c = 0
        if self.pos_x == self.door_x and self.pos_y == self.door_y:
            s.score += 1
            print("Victory")
            self.victory = True
        if len(self.trps) > 2:
            for x in self.trps[::2]:
                for y in self.trps[1::2]:
                    if rnx == x and rny == y:
                        self.trapped()
        elif len(self.trps) == 2:
            if self.trps[0] == rnx and self.trps[1] == rny:
                self.trapped()
                    


    
    def new_map(self):
        w = self.w
        h = self.h
        for x in list(range(3, 100, 2)):
            if s.score == x: 
                r1 = random.randint(0, 1)
                if r1 == 1:
                    w += 1
                else:
                    h += 1

                sumed = w + h
                w = 0
                h = 0
                while w + h < sumed:
                    r1 = random.randint(0, 1)
                    if r1 == 1:
                        w += 1
                    else:
                        h += 1
                self.w = w
                self.h = h
                self.pos_x = random.randint(1, self.w - 1)
                self.pos_y = random.randint(1, self.h - 1)
                self.save()
        

    def move(self):
        choice = input("Go Up, down, left, right? ")
        if (choice[0] == "w" or choice[0] == "W") and self.pos_y - 1 > -1:
            self.pos_y -= 1
            
        elif (choice[0] == "s" or choice[0] == "S") and self.pos_y + 1 != self.h:
            self.pos_y += 1
            
        elif (choice[0] == "a" or choice[0] == "A") and self.pos_x - 1 > 0:
            self.pos_x -= 1
            
        elif (choice[0] == "d" or choice[0] == "D") and self.pos_x + 1 < self.w + 1:
            self.pos_x += 1
        elif choice[0] == "z" or choice[0] == "Z":
            self.s = True
        elif choice == "cheat":
            self.cheat()
        else:
            print("Can't do this bro!")
            self.update()
            self.move()

    def trapped(self):
        luck = random.randint(0, s.dmg)
        
        trap = random.randint(1, 6)
        if trap == 1:
            tr.Bear_trap()
            if s.bt:
                print("You used your book to doge this.")
                luck = 4
                s.bt = False
        elif trap == 2:
            tr.Cage_trap()
            if s.ct:
                print("You used your book to doge this.")
                luck = 4
                s.ct = False
        elif trap == 3:
            tr.Spike_trap()
            if s.st:
                print("You used your book to doge this.")
                luck = 4
                s.st =False
        elif trap == 4:
            tr.Arrows_trap()
            if s.at:
                print("You used your book to doge this.")
                luck = 4
                s.at = False
        elif trap == 5:
            tr.Wall_trap()
            if s.wt:
                print("You used your book to doge this.")
                luck = 4
                s.wt = False
        elif trap == 6:
            tr.quicksand_trap()
            if s.qt:
                print("You used your book to doge this.")
                luck = 4
                s.qt = False
        if luck == 0:
            dmg = random.randint(tr.dmg / 2, tr.dmg)
            print("You encountered a " + tr.name)
            print("The " + tr.name +  " hit you dealing " + str(dmg))
            s.life -= dmg - (((s.armor*10)/100)*dmg)
            print("You life now is " + str(s.life))
            
        else:
            print("You doged a " + tr.name)
            i.item_drop()
            self.traps()
            
       
    def save(self):
        c = 0
        for x in Saved.select():
            c += 1
        if c > 0:
            for x in Saved.select():
                if x.name == 'points':
                    x.value = s.score
                    x.save()
                elif x.name == 'life':
                    x.value = s.life
                    x.save()
                elif x.name == 'dmg':
                    x.value = s.dmg
                    x.save()
                elif x.name == 'x':
                    x.value = self.w
                    x.save()
                elif x.name == 'y':
                    x.value = self.h
                    x.save()
                elif x.name == 'px':
                    x.value = self.pos_x
                    x.save()
                elif x.name == 'py':
                    x.value = self.pos_y
                    x.save()
                elif x.name == 'arm':
                    x.value = s.armor
                    x.save()
                elif x.name == 'high':
                    if s.score > x.value:
                        x.value = s.score
                        x.save()
                        print("You high-score is " + str(x.value))
                    else:
                        print("You high-score is " + str(x.value))
            print("Saved")
        else:
            p = Saved(name = 'points', value = s.score)
            l = Saved(name = 'life', value = s.life)
            dmg = Saved(name = 'dmg', value = s.dmg)
            x = Saved(name = 'x', value = self.w)
            y = Saved(name = 'y', value = self.h)
            px = Saved(name = 'px', value = self.pos_x)
            py = Saved(name = 'py', value = self.pos_y)
            hi = Saved(name = 'high', value = s.score)
            arm = Saved(name = 'arm', value = s.armor)
            name = Saves(name = 'user', value = s.n)
            p.save()
            l.save()
            dmg.save()
            x.save()
            y.save()
            px.save()
            py.save()
            hi.save()
            name.save()
            arm.save()
            print("Saved")
        c = 0
        for y in Saves.select():
            c += 1
        if c > 0:
            for y in Saves.select():
                if y.name == 'user':
                    y.value = s.n
                    y.save()
        else:
            us = Saves(name = 'user', value = s.n)
            us.save()

    def cheat(self):
        z = len(self.trps)
        if z == 2:
            rnx = self.trps[0]
            rny = self.trps[1]
            w = self.w
            h = self.h
            c = 0
            print("Level " + str(s.score + 1))
            while c < h:
                if c == rny:
                    print(" _  "*w); print("| | "*((w - (w - rnx)) - 1) + "|O| " + "| | "*(w-rnx)); print(" ¯  "*w)
                    c += 1
                else:
                    print(" _  "*w); print("| | "*w); print(" ¯  "*w)
                    c += 1
                c = 0

        
        else:
            for x in self.trps[::2]:
                for y in self.trps[1::2]:
                    rnx = x
                    rny = y
                    w = self.w
                    h = self.h
                    c = 0
                    print("Level " + str(s.score + 1))
                    while c < h:
                        if c == rny:
                            print(" _  "*w); print("| | "*((w - (w - rnx)) - 1) + "|O| " + "| | "*(w-rnx)); print(" ¯  "*w)
                            c += 1
                        else:
                            print(" _  "*w); print("| | "*w); print(" ¯  "*w)
                            c += 1
                        c = 0
                
            
            
           
        


i = Items()
m = Map() 
if s.lod[0] == "y" or s.lod[0] == "Y":
    for x in Saved.select():
        if x.name == 'points':
            s.score = x.value
                    
        elif x.name == 'life':
            s.life = x.value
                    
        elif x.name == 'dmg':
            s.dmg = x.value
                    
        elif x.name == 'x':
            m.w = x.value
        elif x.name == 'y':
            m.h = x.value
                   
        elif x.name == 'px':
            m.pos_x = x.value
                    
        elif x.name == 'py':
            m.pos_y = x.value

        elif x.name == 'arm':
            s.armor = x.value
                    
        elif x.name == 'high':
            print("Highest score is " + str(x.value))
    print("Data Loaded.")

if s.lod[0] == "d" or s.lod[0] == "D":
    for x in Saved.select():
        x.delete_instance()
    print("Data deleted")
    u = Saves.get(Saves.name == 'user')
    u.delete_instance()
m.door()
m.traps()
m.update()
while s.life > 0:
    if m.victory:
        i.item_drop()
        m.door()
        m.traps()
        m.new_map()
        m.update()
        m.victory = False
    if m.s:
        m.save()
        m.s = False
    m.move()
    m.update()
m.save()
print("You died")
