


class Cheats1:

    def __init__(self):
        a = True
        while a:
            ent = input("Select cheat: all, weapon, health, exit: ")
            if ent == "weapon":
                self.wep_dmg = int(input("Weapon Damage: "))
                self.wep_range = int(input("Weapon Range: "))
                print("Stats: Damage: {}, Range: {}".format(self.wep_dmg, self.wep_range))
                
            if ent == "health":
                self.char_life = int(input("Life: "))
                print("Stats: Damage: {}, Range: {}, Life {}".format(self.wep_dmg, self.wep_range, self.char_life))

            if ent == "all":
                self.wep_dmg = int(input("Weapon Damage: "))
                self.wep_range = int(input("Weapon Range: "))
                self.char_life = int(input("Life: "))
                self.weapon = input("Weapon name: ")
                print("Stats: Damage: {}, Range: {}, Life {}".format(self.wep_dmg, self.wep_range, self.char_life))
                print("You selected " + self.weapon)
            if ent == "exit":
                a = False
