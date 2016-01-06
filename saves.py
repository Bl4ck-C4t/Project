import peewee

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
if not(Saves.table_exists()): #Checks tables
    db.create_tables([Saved, Saves])

def save(self):
        c = 0
        for x in Saved.select():
            c += 1
        if c > 0: #if we have already the items
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
        else: #first run setup
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
        for y in Saves.select(): #User saves name
            c += 1
        if c > 0:
            for y in Saves.select():
                if y.name == 'user':
                    y.value = s.n
                    y.save()
        else:
            us = Saves(name = 'user', value = s.n)
            us.save()
def load(self):
    if s.lod[0] == "y" or s.lod[0] == "Y": #loads the game
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

    if s.lod[0] == "d" or s.lod[0] == "D": #deletes all data
        for x in Saved.select():
            x.delete_instance()
        print("Data deleted")
        u = Saves.get(Saves.name == 'user')
        u.delete_instance()
