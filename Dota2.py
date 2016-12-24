import random
import copy
import pickle
import os

# TODO make start a new game and delete saves
# TODO make skip the beginning if has saves


def pack(enemy, team, file="db.pl"):
    with open(file, "wb") as f:
        pickle.dump([enemy, team], f)


def unpack(file="db.pl"):
    with open(file, "rb") as f:
        return pickle.load(f)


def search(var, ls, check="name", cpy=True):
    for x in ls:
        if eval("x." + check) == var:
            if cpy:
                return copy.deepcopy(x)
            else:
                return x
    return False


def procent(source, num, integer=False):
    if not integer:
        return (source * num) / 100
    return int((source * num) / 100)


def chance(pro):
    return random.randint(1, 100) <= pro


def ratio(n1, n2, n3):
    return int((n2 * n3) / n1)


def stats(hero, add=""):
    print(add + "HP:{} AD:{} Money:{}$".format(hero.hp, hero.ad, hero.money))


def do_effects(enemy):
    for x in enemy.effects:
        owner = x.owner
        if x.duration > 0:
            if x.name == "DPS":
                enemy.hp -= x.damage
                print("{} dealt {} DPS damage to {} with '{}' active:{}".format(owner.name, x.damage, enemy.name,
                x.own_spell, x.duration))
            elif x.name == "DPS%":
                enemy.hp -= procent(enemy.hp, x.damage)
                print("{} dealt {} DPS damage to {} with '{}' active:{}".format(owner.name, x.damage, enemy.name,
                x.own_spell, x.duration))
            elif x.name == "Lifesteal":
                enemy.hp -= x.damage
                owner.hp += x.damage
                print("{} stole {} health from {} with '{}' active:{}".format(owner.name, x.damage, enemy.name,
                x.own_spell, x.duration))
            elif x.name == "Lifesteal%":
                enemy.hp -= procent(enemy.hp, x.damage)
                owner.hp += procent(enemy.hp, x.damage)
                print("{} stole {} health from {} with '{}' active:{}".format(owner.name, x.damage, enemy.name,
                x.own_spell, x.duration))
            elif x.name == "passive_damage" and not x.toggle:
                x.toggle = True
                ad = procent(enemy.ad, 50)
                enemy.ad += ad
                x.prev_ad = ad

        else:
            enemy.effects.remove(x)
            if x.toggle:
                if x.name == "passive_damage":
                    enemy.ad -= x.prev_ad
        x.duration -= 1


def coolDOWN(ls):
    for hero in ls:
        for x in hero.backpack:
            if x.cool is not None and x.curr_cool > 0:
                x.curr_cool -= 1
        if hero.spell1.cooldown is not None and hero.spell1.curr_cool > 0:
            hero.spell1.curr_cool -= 1
        if hero.spell2.cooldown is not None and hero.spell2.curr_cool > 0:
            hero.spell2.curr_cool -= 1
        if hero.spell3.cooldown is not None and hero.spell3.curr_cool > 0:
            hero.spell3.curr_cool -= 1
        if hero.ultimate.cooldown is not None and hero.ultimate.curr_cool > 0:
            hero.ultimate.curr_cool -= 1


class Hero:
    heroes = []

    def __init__(self, name, ad, hp, spell1, spell2, spell3, ultimate):
        self.name = name
        self.ad = ad
        self.max_hp = hp
        self.hp = hp
        self.spell1 = spell1
        self.spell2 = spell2
        self.spell3 = spell3
        self.ultimate = ultimate
        self.spells = [spell1, spell2, spell3, ultimate]
        self.backpack = []
        self.money = 350
        self.me = False
        self.pos = "On Spawn"
        self.lane = None
        self.recalling = False
        self.effects = []


class Magic:
    magics = []

    def __init__(self, name, damage, projectile, AOE, special_effect=None, cooldown=None, target="enemy"):
        self.name = name
        self.damage = damage
        self.projectile = projectile
        self.AOE = AOE
        self.special_effect = special_effect
        self.cooldown = cooldown
        self.curr_cool = 0
        self.target = target

    def effect(self, enemys):
        if self.curr_cool == 0:
            if self.AOE:
                for x in enemys:
                    ch = 100
                    if self.projectile:
                        ch = 60
                    if chance(ch):
                        dmg = random.randint(procent(self.damage, 40), self.damage)
                        x.hp -= dmg
                        print("You hit {} with {} and dealt {} damage".format(x.name, self.name, dmg))
                        if self.special_effect is not None:
                            eff = self.special_effect
                            x.effects.append(eff)
                            print("You activated {} effect on {} for {}t".format(eff.name, x.name, eff.duration))
                    else:
                        print("You missed")
            else:
                ch = 100
                if self.projectile:
                    ch = 60
                if chance(ch):
                    dmg = random.randint(procent(self.damage, 40), self.damage)
                    enemys.hp -= dmg
                    print("You hit {} with {} and dealt {} damage".format(enemys.name, self.name, dmg))
                    if self.special_effect is not None:
                        eff = self.special_effect
                        enemys.effects.append(eff)
                        print("You activated {} effect on {} for {}t".format(eff.name, enemys.name, eff.duration))
                else:
                    print("You missed")
            self.curr_cool = self.cooldown
        else:
            print("{} on cooldown {} more turns".format(self.name, self.curr_cool))




class Special_effect:
    def __init__(self, name, damage, duration, target="enemy", toggle=False):
        self.name = name
        self.damage = damage
        self.duration = duration
        self.toggle = toggle
        self.target = target


class Item:
    items = []

    def __init__(self, name, effect, buff, prize, oneuse=False, cool=None, amount=None, target="hero"):
        self.name = name
        self.effect = effect
        self.buff = buff
        self.cool = cool
        self.curr_cool = 0
        self.amount = amount
        self.prize = prize
        self.used = False
        self.target = target
        self.oneuse = oneuse

    def act_effect(self, hero):
        backpack = hero.backpack
        if self.effect == "active":
            if self.oneuse:
                backpack.remove(self)
            if self.buff == "attack_damage":
                if self.cool is not None and self.curr_cool == 0:
                    hero.ad += self.amount
                    self.curr_cool = self.cool
            if self.buff == "HP_boost":
                if self.cool is not None and self.curr_cool == 0:
                    hero.hp *= self.amount
                    self.curr_cool = self.cool
            if self.buff == "HP":
                if self.cool is not None and self.curr_cool == 0:
                    hero.hp += self.amount
                    if hero.hp > hero.max_hp:
                        hero.hp = hero.max_hp
                    self.curr_cool = self.cool
            if self.buff == "Damage":
                if self.cool is not None and self.curr_cool == 0:
                    hero.hp -= procent(hero.hp, self.amount, True)
                    self.curr_cool = self.cool

        elif not self.used and self.effect == "passive":
            amount = self.amount
            if self.buff == "health+":
                hero.hp += amount
            if self.buff == "armor":
                hero.max_hp += procent(hero.max_hp, amount, True)
            if self.buff == "damage+":
                hero.ad += amount
            if self.buff == "damage%":
                hero.ad += procent(hero.ad, amount, True)
            self.used = True

        else:
            print("Item {} has only a passive effect".format(self.name))
        hero.hp = hero.max_hp


Magic.magics.append(Magic("Fire_spell", 0, False, False, Special_effect("DPS", 50, 2), 6))
Magic.magics.append(Magic("Fire_strike", 100, True, False))
Magic.magics.append(Magic("Leech", 0, False, False, Special_effect("Lifesteal%", 20, 1), 4))
Magic.magics.append(Magic("Reborn", 0, False, False, Special_effect("Lifesteal", 100, 1), 13))
Magic.magics.append(Magic("Ice_spell", 0, False, False, Special_effect("Freeze", 20, 1), 3))
Magic.magics.append(Magic("Earth_spell", 0, False, False, Special_effect("Root", 10, 1), 6))
Magic.magics.append(Magic("Portal_beam", 60, True, False))
Magic.magics.append(Magic("Void", 0, False, True, Special_effect("DPS%", 40, 3), 6))
Magic.magics.append(Magic("Infect", 0, False, False, Special_effect("DPS", 60, 5), 6))
Magic.magics.append(Magic("BEAM", 0, False, False, Special_effect("Silence", 100, 3), 18))
Magic.magics.append(Magic("Spear_strike", 80, True, False, None, 6))
Magic.magics.append(Magic("Quick_recall", 20, False, True, None, 3))
Magic.magics.append(Magic("Spear_madness", 70, True, True, None, 7))
Magic.magics.append(Magic("Destroyer", 400, False, False, None, 20))
Magic.magics.append(Magic("Blood_pool", 0, False, False, Special_effect("Untarget", 0, 2, "hero"), 12, "hero"))
Magic.magics.append(Magic("Sword_turn", 100, False, True, None, 5))
Magic.magics.append(Magic("Burn_blow", 0, False, True, Special_effect("DPS%", 10, 3), 2))
Magic.magics.append(Magic("Explosion", 70, True, True, None, 17))
Magic.magics.append(Magic("Damage_spell", 40, False, False, None, 3))
Magic.magics.append(Magic("Venom_shot", 60, True, False, None, 6))
Magic.magics.append(Magic("Spider_bomb", 70, True, True, None, 9))
Magic.magics.append(Magic("Web_shot", 0, True, False, Special_effect("Stun", 20, 2), 4))
Magic.magics.append(Magic("Spider_form", 0, False, False, Special_effect("passive_damage", 80, 4, "hero"), 20, "hero"))
Item.items.append(Item("Health_potion", "active", "HP", 50, True, None, 50))
Item.items.append(Item("Dagger", "passive", "damage+", 200, False, None, 20))
Item.items.append(Item("Sword of Rah'zak", "active", "Damage", 300, False, 4, 40, "enemy"))
Item.items.append(Item("ThornMail", "passive", "armor", 500, False, None, 40))
Item.items.append(Item("Blade of the ruined king", "passive", "damage%", 600, False, None, 40, "hero"))
Hero.heroes.append(Hero("Garen", 30, 1000, search("Damage_spell", Magic.magics), search("Fire_spell", Magic.magics),
                        search("Sword_turn", Magic.magics), search("Destroyer", Magic.magics)))
Hero.heroes.append(Hero("LavaHog", 40, 430, search("Fire_spell", Magic.magics), search("Burn_blow", Magic.magics),
                        search("Fire_strike", Magic.magics), search("Explosion", Magic.magics)))
Hero.heroes.append(Hero("Vlad", 40, 300, search("Leech", Magic.magics), search("Ice_spell", Magic.magics),
                        search("Blood_pool", Magic.magics), search("Reborn", Magic.magics)))
Hero.heroes.append(Hero("Pantheon", 80, 250, search("Damage_spell", Magic.magics), search("Spear_strike", Magic.magics),
                        search("Spear_madness", Magic.magics), search("Quick_recall", Magic.magics)))
Hero.heroes.append(Hero("Malzahar", 30, 300, search("Portal_beam", Magic.magics), search("Void", Magic.magics),
                        search("Infect", Magic.magics), search("BEAM", Magic.magics)))
Hero.heroes.append(Hero("Elise", 40, 320, search("Venom_shot", Magic.magics), search("Spider_bomb", Magic.magics),
                        search("Web_shot", Magic.magics), search("Spider_form", Magic.magics)))


def item_desc(item):
    y = item
    add = ""
    txt = ""
    if y.cool is not None:
        add = "cooldown:" + str(y.cool) + "t"
    if y.name == "Health_potion":
        txt = "Heals 50hp oneuse only" + add
    elif y.name == "Dagger":
        txt = "Increases damage by 20" + add
    elif y.name == "Sword of Rah'zak":
        txt = "Damages enemy with 40% of their health, " + add
    elif y.name == "ThornMail":
        txt = "Increases armor by 40%" + add
    elif y.name == "Blade of the ruined king":
        txt = "Increases current damage by 40%" + add
    return txt


def shop(hero):
    backpack = hero.backpack
    items = Item.items
    print("Welcome to the shop!")
    while True:
        stats(hero)
        for x, y in enumerate(items, start=1):
            txt = item_desc(y)
            print("{}. {} {}$ - {}".format(x, y.name, y.prize, txt))
        ch = input("Chose item to purchase 'e' to exit: ")
        if ch == "e":
            break
        else:
            chosen = items[int(ch) - 1]
            if chosen.prize <= hero.money:
                hero.money -= chosen.prize
                backpack.append(copy.deepcopy(chosen))
                if chosen.effect == "passive":
                    backpack[-1].act_effect(hero)

                print("You purchased {} for {}$".format(chosen.name, chosen.prize))
            else:
                print("You need {}$ more to purchase {}".format(abs(hero.money - chosen.prize), chosen.name))


def item_menu(hero, enemys):
    while True:
        for x, y in enumerate(hero.backpack, start=1):
            cl = ""
            if y.cool is not None:
                ad = str(y.curr_cool)
                if ad == "0":
                    ad = "ready"
                else:
                    ad += "t"
                cl = " cooldown: " + ad
            print("{}. {}({}){} - {}".format(x, y.name, y.effect, cl, item_desc(y)))
        enter = input("Which item to activate('e' to exit): ")
        if enter != "e":
            item = hero.backpack[int(enter) - 1]
            if item.effect == "passive":
                print("This item has only passive effect")
            else:
                if item.target == "hero":
                    add = ""
                    if item.effect == "active" and item.cool is not None:
                        add = " cooldown:" + str(item.cool) + "t"
                    print("You used {}{}".format(item.name, add))
                    item.act_effect(hero)
                elif item.target == "enemy":
                    for x, y in enumerate(enemys, start=1):
                        print("{}. {}".format(x, y.name))
                    enter = input("Select enemy to use item on: ")
                    en = enemys[int(enter) - 1]
                    item.act_effect(en)
                    add = ""
                    if item.cool is not None:
                        add = " cooldown:" + str(item.cool) + "t"
                    print("You used {}{}".format(item.name, add))
        else:
            break


def AI(enemys, team):
    for hero in team:
        effects = [x.name for x in hero.effects]
        stun = "Stun" in effects
        root = "Root" in effects
        freeze = "Freeze" in effects
        silence = "Silence" in effects
        if stun or freeze:
            print("Turn missed because of a stun")
            return True
        ls = [x for x in hero.spells if x.curr_cool == 0]
        ls.append("basic_attack")
        spell = random.choice(ls)
        if spell != "basic_attack" and spell.AOE:
            target = enemys[:]
        else:
            target = [random.choice(enemys)]
        if spell == "basic_attack":
            if "Untarget" in map(lambda x: x.name, target[0].effects):
                print("Target untargetable.")
                return True
            if not root:
                print("{} hit {} with basic attack dealing {} dmg".format(hero.name, target[0].name, hero.ad))
                target[0].hp -= hero.ad
            else:
                print("Couldn't basic attack because of a root.")
            return True
        if not silence:
            ch = 100
            if spell.projectile:
                ch = 65
            if chance(ch):
                for x in target:
                    if x.pos != hero.pos:
                        return False
                    if "Untarget" in map(lambda y: y.name, x.effects):
                        print("Target {} untargetable.".format(x.name))
                        continue
                    dmg = random.randint(procent(spell.damage, 40), spell.damage)
                    x.hp -= dmg
                    if dmg == 0 and spell.special_effect is not None:
                        dmg = spell.special_effect.damage
                    if spell.damage != 0:
                        print("{} hit {} with '{}' and dealt {}".format(hero.name, x.name, spell.name, dmg))
                    if spell.special_effect is not None:
                        if spell.special_effect.target == "hero":
                            print("{} activated '{}'".format(hero.name, spell.name))
                            if spell.name == "Quick_recall":
                                hero.pos = "On Spawn"
                                print("{} fled the battle.".format(hero.name))
                                return False
                        effect = spell.special_effect
                        effect.owner = hero
                        effect.own_spell = spell.name
                        x.effects.append(effect)
                        print("{} activated '{}'".format(hero.name, spell.name))
                    if x.hp <= 0:
                        get = procent(x.money, 60)
                        x.money -= get
                        hero.money += get
                        print("{} killed {} and received {}$".format(hero.name, x.name, get))
                        return False
                    return True
            else:
                print("{} missed you".format(hero.name))
        else:
            print("Couldn't use '{}' because of silence.".format(spell.name))
            return True


def fight(hero, enemys, team=None):
    if team is None:
        team = []
    targets = enemys[:]
    if hero not in team:
        team.append(hero)
    turn = True
    while True:
        for x in enemys:
            if x.hp <= 0:
                rec = procent(x.money, 70)
                print("You killed {}".format(x.name))
                enemys.remove(x)
                hero.money += rec
                print("You received {}$ for killing {}".format(rec, x.name))
        if len(enemys) == 0:
            break
        if turn:
            for x in team:
                stats(x, "Team " + x.name + " ")
            AI(enemys, team)
            stats(hero)
            effects = list(map(lambda x: x.name, hero.effects))
            for x in enemys:
                stats(x, "Enemy " + x.name + " ")
            for x, y in enumerate(hero.spells, start=1):
                sp_effect = ""
                dmg = y.damage
                if dmg == 0 and y.special_effect is not None:
                    dmg = y.special_effect.damage
                if y.curr_cool == 0:
                    cld = "ready"
                else:
                    cld = str(y.curr_cool) + "t"
                if y.special_effect is not None:
                    sp_effect = "Type: " + y.special_effect.name
                print("{}. {} {} DMG:{} {}".format(x, y.name, cld, dmg, sp_effect))
            print("5. Basic attack\n6. Open backpack\n7. Flee")
            spl = int(input("Enter number: "))
            if spl in range(1, 5):
                spell = hero.spells[spl-1]
                if spell.name == "Quick_recall":
                    hero.pos = "On Spawn"
                    print("You fled the battle using 'Quick_recall'.")
                if spell.curr_cool == 0:
                    ch = 100
                    if spell.projectile:
                        ch = 65
                    if chance(ch):
                        if spell.target == "enemy":
                            if not spell.AOE:
                                for x, y in enumerate(targets, start=1):
                                    print("{}. {}".format(x, y.name))
                                en = int(input("Select enemy to use spell on: "))
                                enemy = [targets[en - 1]]
                            else:
                                enemy = targets[:]
                            for x in enemy:
                                dmg = random.randint(procent(spell.damage, 40), spell.damage)
                                if dmg == 0 and spell.special_effect is not None:
                                    dmg = spell.special_effect.damage
                                x.hp -= dmg
                                if x.hp > 0:
                                    print("You damaged {} with {} and dealt {} dmg".format(x.name, spell.name, dmg))
                                elif x.hp <= 0:
                                    rec = procent(x.money, 70)
                                    print("You killed {}".format(x.name))
                                    enemys.remove(x)
                                    hero.money += int(rec)
                                    print("You received {}$ for killing {}".format(rec, x.name))
                                if spell.special_effect is not None:
                                    if spell.special_effect.target == "hero":
                                        print("You activated '{}'".format(spell.name))
                                    effect = spell.special_effect
                                    effect.owner = hero
                                    effect.own_spell = spell.name
                                    x.effects.append(effect)
                        else:
                            if spell.special_effect is not None:
                                effect = spell.special_effect
                                effect.owner = hero
                                effect.own_spell = spell.name
                                hero.effects.append(effect)
                                print("You activated '{}'".format(spell.name))

                    else:
                        print("You missed")
                    if spell.cooldown is not None:
                        if spell.curr_cool == 0:
                            spell.curr_cool = spell.cooldown
                else:
                    print("Spell on cooldown you can't use it yet")
                    turn = not turn

            else:
                if spl == 5:
                    for x, y in enumerate(targets,start=1):
                        print("{}. {}".format(x, y.name))
                    en = int(input("Select enemy to attack: "))
                    enemy = targets[en - 1]
                    enemy.hp -= hero.ad
                elif spl == 6:
                    item_menu(hero, enemys)
                    turn = not turn
                elif spl == 7:
                    ch = ratio(600, 30, random.choice(enemys).hp-hero.hp)
                    if chance(ch):
                        print("You didn't manage to flee.")
                    else:
                        print("You fled the battle.")
                        break
        else:
            coolDOWN(enemys+team)
            for x in enemys+team:
                do_effects(x)
            for x in enemys:
                print("{} is doing a turn".format(x.name))
            end = AI(team, enemys)
            if not end:
                break

        turn = not turn
    return enemys


def start():
    if os.path.exists("db.pl") and os.stat("db.pl").st_size > 0:
        save = True
    else:
        save = False
    if save:
        en = input("Load game(y/n): ")
        if en == "n":
            save = False
        else:
            unpacked = unpack()
            team = unpacked[0]
            enemy = unpacked[1]
            hero = search(True, team, "me", False)
    if not save:
        for x in range(len(Hero.heroes)):
            print("{}. {}".format(x + 1, Hero.heroes[x].name))
        ch = int(input("Chose a hero: "))
        curr_hero = copy.deepcopy(Hero.heroes[ch - 1])
        curr_hero.me = True
        lanes = ["top", "mid", "bot"]
        for x in range(1, 4):
            print("{}. {}".format(x, lanes[x - 1]))
        lane = input("Choose lane: ")
        lane = lanes[int(lane) - 1]
        curr_hero.lane = lane
        enemy = []
        team = []
        for x in range(5):
            team.append(copy.deepcopy(random.choice(Hero.heroes)))
            enemy.append(copy.deepcopy(random.choice(Hero.heroes)))
        del team[-1]
        team.insert(0, curr_hero)
        enemy[0].lane = "mid"
        enemy[1].lane = "top"
        enemy[2].lane = "top"
        enemy[3].lane = "bot"
        enemy[4].lane = "bot"
        for x in enemy:
            x.pos = "On " + x.lane
        top = 0
        mid = 0
        bot = 0
        if lane == "top":
            top = 1
        elif lane == "mid":
            mid += 1
        else:
            bot += 1
        for x in team:
            if x.lane is None:
                if top < 2:
                    x.lane = "top"
                    top += 1
                elif bot < 2:
                    x.lane = "bot"
                    top += 1
                elif mid < 1:
                    x.lane = "mid"
                    mid += 1
        print("5v5 Game started.")
        team_show = ""
        enemy_show = ""
        for x in team:
            x.faction = "team"
            team_show += x.name + " "
        for x in enemy:
            x.faction = "enemy"
            enemy_show += x.name + " "
        print("{}\n            vs\n{}".format(team_show, enemy_show))
        hero = curr_hero
    turn = True
    while True:
        if turn:
            if hero.hp <= 0:
                hero.pos = "On Spawn"
                print("You got respawned")
            print("You are {}".format(hero.pos))
            if hero.pos == "On Spawn":

                ch = 1
                while ch != 2:
                    hero.hp = hero.max_hp
                    print("1. Shop\n2. Go to lane\n3. Save and exit")
                    ch = int(input("Enter choice: "))
                    if ch == 1:
                        shop(hero)
                        hero.hp = hero.max_hp
                    elif ch == 2:
                        hero.pos = "On " + hero.lane
                    elif ch == 3:
                        pack(enemy, team)
                        print("Game saved.\nGoodbye.")
                        exit()
            elif hero.pos == "On " + hero.lane:
                stats(hero, "Stats: ")
                print("1. Check enemy {}\n2. Farm\n3. Gang lane\n4. Recall\n5. Open backpack\n6. Attack enemy\n"
                      "7. Save and exit".format(hero.pos))
                ch = int(input("Choose what to do:  "))
                enemys = [x for x in enemy if x.lane == hero.lane and x.hp > 0]
                if ch == 1:
                    if len(enemys) > 0:
                        for x in enemys:
                            print("Enemy {}: HP:{} AD:{}".format(x.name, x.hp, x.ad))
                    else:
                        print("You are alone " + hero.pos)
                    turn = not turn
                elif ch == 2:
                    attackers = []
                    for en in enemys:
                        if chance(ratio(560, 60, (en.hp - hero.hp) + (en.ad - hero.ad))):
                            attackers.append(en)
                    if len(attackers) == 0:
                        max_get = ratio(400, 50, hero.hp) + ratio(60, 80, hero.ad)
                        gain = random.randint(int(procent(max_get, 40)), max_get)
                        hero.money += gain
                        print("You farmed and gained {}$".format(gain))
                    if len(attackers) > 0:
                        print("Enemy {} attacked you while farming".format(" ".join(map(lambda x: x.name, attackers))))
                        enemys = fight(hero, attackers)
                elif ch == 3:
                    for x, y in enumerate([x for x in lanes if x != hero.lane],start=1):
                        print("{}. {}".format(x, y))
                    choice = int(input("Select lane to gang: "))
                    gang_lane = [x for x in lanes if x != hero.lane][choice-1]
                    hero.pos = "On " + gang_lane
                    fight(hero, [x for x in enemy if x.lane == gang_lane], [x for x in team if x.lane == gang_lane])
                elif ch == 4:
                    if chance(ratio(4, 30, len(enemys))):
                        print("Enemy attacked you while recalling.")
                        enemys = fight(hero, enemys)
                    else:
                        print("You recalled to the spawn")
                        hero.pos = "On Spawn"
                elif ch == 5:
                    item_menu(hero, enemys)
                    turn = not turn
                elif ch == 6:
                    targets = []
                    while True:
                        for x, y in enumerate(enemys, start=1):
                            print("{}. {}".format(x, y.name))
                        en = input("Enter enemy number 'e' to enter fight 'c' to cancel{}: ".format(
                         list(map(lambda x: x.name, targets))))
                        if en == "c":
                            break
                        elif en == 'e':
                            fight(hero, targets)
                            break
                        else:
                            targets.append(enemys[int(en)-1])
                elif ch == 7:
                    pack(enemy, team)
                    print("Game saved.\nGoodbye.")
                    exit()
                turn = not turn
        else:
            coolDOWN(team + enemy)
            for x in team + enemy:
                do_effects(x)
            for en in enemy:
                if en.recalling:
                    en.recalling = False
                    en.hp = en.max_hp
                    if en.lane == hero.lane:
                        print(en.name + " recalled back.")
                if en.hp <= procent(en.max_hp, 40):
                    en.recalling = True
                    if en.lane == hero.lane:
                        print(en.name + " is recalling.")
                if en.money < 700:
                    if en.lane == hero.lane:
                        print(en.name + " is farming.")
                        max_get = ratio(400, 50, en.hp) + ratio(60, 100, en.ad)
                        en.money += random.randint(int(procent(max_get, 40)), max_get)
            turn = not turn

start()
