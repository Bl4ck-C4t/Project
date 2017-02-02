import time
import random
import re
import threading
import sys
import copy

# TODO part - 6
# TODO continue part 5
# TODO make hashdump



def getTerminalSize():
    import os
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
                                                 '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

def head():
    time.sleep(2)
    print("""
    ______          _           _     _____   ___  ___  ___  ___
    | ___ \        (_)         | |   |  __ \ / _ \ |  \/  | / _ \
    | |_/ / __ ___  _  ___  ___| |_  | |  \// /_\ \| .  . |/ /_\ \
    |  __/ '__/ _ \| |/ _ \/ __| __| | | __ |  _  || |\/| ||  _  |
    | |  | | | (_) | |  __/ (__| |_  | |_\ \| | | || |  | || | | |
    \_|  |_|  \___/| |\___|\___|\__|  \____/\_| |_/\_|  |_/\_| |_/
                  _/ |
                 |__/
       """)

def box(text, space=False):
    width, b = getTerminalSize()
    hw = int(width / 2)
    f = ""
    part = ""
    c = 0
    top = "_" * hw
    if space:
        top = " " * hw + "_" * hw
    f += top + "\n"
    if space:
        f += " " * (hw - 1) + "|"
    while c < len(text):
        ch = text[c]
        part += ch
        if len(part) == hw:

            if not space:
                part += "|"
            if c != len(text):
                part += "\n"
            if space:
                part += " " * (hw - 1) + "|"
            f += part
            part = ""
        c += 1
    f += part
    if part != "" and not space:
        f += " " * (hw - len(part)) + "|"
    if not space:
        f += "\n" + "_" * hw + "|"
    if space:
        f += "\n" + " " * (hw - 1) + "|" + "_" * hw
    return f


def ipgen():
    f = ""
    for x in range(4):
        f += str(random.randint(1, 255)) + "."
    return f[:-1]


def t2a(text):
    chypher = ""
    a = 0
    for x in text:
        chypher += chr(ord(x) + a)
        a += 1
    return chypher


def a2t(asci):
    try:
        dec = ""
        a = 0
        for x in asci:
            dec += chr(ord(x) - a)
            a += 1
        return dec
    except:
        pass


def credits(p_len, u_len):
    alpha = "qwertyuiopasdfghjklzxcvbnm0123456789"
    user = ""
    password = ""
    while p_len > 0:
        password += random.choice(alpha)
        p_len -= 1
    while u_len > 0:
        user += random.choice(alpha)
        u_len -= 1
    return [user, password]


def check(ls):
    if (ls[0][0] == ls[1][1] and ls[1][1] == ls[2][2]) or (ls[0][2] == ls[1][1] and ls[1][1] == ls[2][0]):
        return True
    return False


def magic_square(gone, hard=2):
    square = [[0 for c in range(3)] for b in range(3)]
    while check(square):
        square = [[0 for c in range(3)] for b in range(3)]
        sm = random.randint(1,hard)
        form = ["12","33","21","31","22","13","23","11","32"]
        for seq in form:
            y = int(seq[0])-1
            x = int(seq[1])-1
            square[y][x] = sm
            sm += 1
        adf = copy.deepcopy(square)
        for cac in range(gone):
            x = random.randint(0,2)
            y = random.randint(0,2)
            while square[y][x] == "?":
                x = random.randint(0,2)
                y = random.randint(0,2)
            square[y][x] = "?"

    print("Example '2,3,4' - replaces the number at second row third colomun with the number 4")
    while True:
        for x in square:
            row = ""
            for y in x:
                row += str(y) + " "
            print(row)
        if square == adf:
            print("Victory")
            print("You solved the firewall.")
            return True
        pos = input("Enter coordinates(row,colomun,number to replace with) 'c' to cancel: ")
        if pos == "c":
            print("Bypass canceled.")
            return False
        ps = pos.split(",")
        row = int(ps[0])-1
        col = int(ps[1])-1
        num = int(ps[2])
        del square[row][col]
        square[row].insert(col,num)

def HardCount(ls, name):
    found = 0
    for file in ls:
        nm = file.name
        patt = re.compile(name + "(\(\d+\))?")
        sr = re.search(patt, nm)
        if sr != None:
            found += 1
    if found > 0:
        new_name = "{}({})".format(name, found)
    else:
        new_name = name
    return new_name





def ratio(n1, n2, n3, whole=False):
    if not whole:
        return (n2*n3)/n1
    return int((n2*n3)/n1)


def search(ls, pro, value, cp=False):
    for x in ls:
        if eval("x." + pro) == value:
            if not cp:
                return x
            else:
                return copy.deepcopy(x)
    return False


def check_unread(contact):
    for x in contact.emails:
        if x.unread:
            return "*"
    return ""


def add_email(contact, title, content=[]):
    mail = Contacts.Mail(title, content)
    contact.emails.append(mail)

def open_file(path, obj):
    found = re.search(r"(?P<folder>.+)/(?P<filename>\w+\.\w+)", path)
    if found == None:
        folder = obj.dir
        name = path
    else:
        folder = found.group("folder")
        name = found.group("filename")
        folder = search(obj.harddrive, "path", folder)
    file = search(folder.folder, "name", name)
    return file


def Portscanner(self):
    while True:
        print("""
        Welcome to Port scanner
        'p' - to scan ports
        'a' - for about
        'e' - to exit
        """)
        ent = input("Choose: ")
        if ent == 'a':
            print("The portscanner can detect vulnerable ports on systems.")
        elif ent == "e":
            return
        elif ent == "p":
            ip = input("Enter target's ip: ")
            target = search(PC.all_pc, "ip", ip)
            if target == False:
                print("No such ip :/")
                continue
            else:
                print("Scanning...")
                time.sleep(1)
                for port in target.ports:
                    print("Port {} - {}".format(port.number, port.state))

def Ncrack(self):
    print("""
        ███╗   ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
        ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
        ██╔██╗ ██║██║     ██████╔╝███████║██║     █████╔╝
        ██║╚██╗██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗
        ██║ ╚████║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
        ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """)
    while True:
        print("""
        'a' - for about
        'c' - to start attack
        'e' - to exit
        """)
        ent = input("Choose: ")
        if ent == "a":
            print("Ncrack is used for cracking usernames and passwords.")
        elif ent == "e":
            return
        elif ent == "c":
            ip = input("Enter target's ip: ")
            target = search(PC.all_pc, "ip", ip)
            if target == False:
                print("No such ip :/")
                continue
            port = int(input("Enter port to attack: "))
            port = search(target.ports, "number", port)
            if port == False:
                print("No such port :/")
                continue
            if port.state == "closed":
                print("This port is closed.")
                continue
            tp = input("Choose attack('b' - bruteforce, 'd' - dictionary): ")
            if tp == "b":
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                user = port.user
                password = port.password
                pass_guess = ""
                print("Connecting...")
                time.sleep(1)
                print("Collecting username...")
                time.sleep(1.5)
                print("Username got. Starting password cracking...")
                time.sleep(0.5)
                x = 0
                while True:
                    ch = alpha[x]
                    succ = "FAIL"
                    if ch == password[len(pass_guess)]:
                        succ = "SUCCESS"
                    print("Trying {}{} - {}".format(pass_guess, ch, succ))
                    time.sleep(0.2)
                    if succ == "SUCCESS":
                        pass_guess += ch
                        x = -1
                    if pass_guess == password:
                        print("Password cracked.")
                        break
                    x += 1
            elif tp == "d":
                file = input("Enter wordlist full path: ")
                file = open_file(file, self)
                txt = file.content
                txt = txt.split(",")

            print("Found:\nUsername: {}\nPassword: {}".format(user, password))



def Webcrawler(self):
    print("""
        Welcome to
         _    _  ____  ____     ___  ____    __    _    _  __    ____  ____
        ( \/\/ )( ___)(  _ \   / __)(  _ \  /__\  ( \/\/ )(  )  ( ___)(  _ \
         )    (  )__)  ) _ <  ( (__  )   / /(__)\  )    (  )(__  )__)  )   /
        (__/\__)(____)(____/   \___)(_)\_)(__)(__)(__/\__)(____)(____)(_)\_)
    """)
    while True:
        print("""
        'a' - for about
        'c' - to toggle crawler
        'e' - to eit

        """)
        ent = input("Choose option: ")
        if ent == "e":
            return
        elif ent == "a":
            print("The Web crawler can detect network traffic and server request and responses\nand find server ip addresses, "
                  "locations, etc.")
        elif ent == "c":
            self.crawling = not self.crawling
            if self.crawling:
                print("Crawler activated in the background")
                print("Use the 'web' command to access websites and the crawler will follow the net traffic.")
            else:
                print("Crawler deactivated.")



def Decryptor(self):
    name = input("Enter file path to decrypt: ")
    file = open_file(name, self)
    if not file.encrypted:
        print("The file is not encrypted")
    else:
        txt = file.content
        txt = a2t(txt)
        print("Text decrypted:\n" + txt)
        if self.story == 5:
            self.reply(self.mails[0], "p5")
        ent = input("Write to file?(y/n): ")
        if ent == "y":
            file.content = txt
            file.encrypted = False
            name = re.search(r"\w+", name).group()
            file.name = name + "." + file.type
            print("Text written to " + name)
        print("Goodbye")


def LAN(ls):
    host = ls[0]
    rhost = ls[1]
    ln = rhost.LAN
    print("Welcome to LAN tool")
    while True:
        print("'e' - to exit\n's' - to scan\n'c' - to connect")
        ent = input("Enter: ")
        if ent == "e":
            return
        elif ent == "s":
            print("Computers connected to LAN:")
            for x in ln:
                print("{} - Lan state: {}".format(x.name, x.type))
        elif ent == "c":
            name = input("Enter name of computer on lan: ")
            lan_adp = search(ln, "name", name)
            comp = lan_adp.host
            if lan_adp.type == "unlocked":
                Instance.i = comp
                print("Connected.")
            elif lan_adp.type == "locked":
                user = input("Enter username: ")
                password = input("Enter password: ")
                if user == lan_adp.user and password == lan_adp.password:
                    Instance.i = comp
                    print("Connected.")
            return


def hashdump(lhost, rhost):
    pass

class Dirs:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.folder = []

    def __str__(self):
        return self.path


class File:
    files = []
    fls = {x.name: x for x in files}

    def __init__(self, name, size, tp, content, encr=False):
        self.fls = {x.name: x for x in self.files}
        self.name = name
        self.size = size
        self.type = tp
        self.content = content
        self.encrypted = encr
        if self.encrypted:
            self.name = "{}[e].{}".format(name, tp)
        else:
            self.name = "{}.{}".format(name, tp)

    def run(self, arg):
        if not self.encrypted:
            if self.type == "exe":
                self.content(arg)
            elif self.type == "txt":
                print("Content:\n" + self.content)
        else:
            print("Can't open this file because it is encrypted.")


class Contacts:

    class Mail:
        def __init__(self, title, content=[]):
            self.title = title
            self.content = content
            self.unread = True

    def __init__(self, name, emails=[]):
        self.name = name
        self.emails = emails
        self.attachments = []


class Port:
    ports = []

    def __init__(self, number, diff, state="open"):
        p_len = ratio(1, 3, diff, True)
        u_len = ratio(1, 5, diff, True)
        cred = credits(p_len, u_len)
        self.number = number
        self.user = cred[0]
        self.password = cred[1]
        self.state = state


class LAN_con:
    def __init__(self, host, tp="unlocked", user=None, password=None):
        self.type = tp
        self.user = user
        self.password = password
        self.host = host
        self.name = host.name

class Instance:
    i = 0


class PC:
    all_pc = []


    def __init__(self, name, ip, me, space=1000, hard=[], mails=[]):
        self.ip = ip
        self.used = 0
        hard.append(Dirs(name, name))
        hr = []
        for x in hard:
            if x.__class__.__name__ != "Dirs":
                hr.append(x)
                self.used += x.size
        hard = [x for x in hard if x.__class__.__name__ == "Dirs"]
        root = search(hard, "name", name)
        root.folder += hr
        self.harddrive = hard
        self.dir = search(hard, "name", name)  # current directory
        self.name = name
        self.path = name
        self.bash = "{}#> ".format(name)
        self.cl = ["help", "ls", "connect", "email"]
        self.crawling = False
        self.net = []
        self.mails = mails
        self.me = me
        self.space = space
        self.story = 1  # shows to which part of the story we are
        self.ports = []
        self.all_pc.append(self)

    def reply(self, contact, mess):
        part = self.story
        if part == 1 and mess == "Ok":
            self.story += 1
            add_email(contact, "Gear up", [box("Ok then go to 'www.h4u.com' and download the apps from there("
                                                 "use the 'web' command to do it).")])
            print("New message.")
        elif part == 2 and mess == "p2":
            self.story += 1
            add_email(contact, "Attack", [box("Ok i need you to attack {} use the portscanner to find a port for "
                                              "attack and then crack password with Ncrack and use connect."
                                              " Then download data.txt".format(obj1.ip))])
            print("New message.")
        elif part == 3 and mess == "p3":
            self.story += 1
            add_email(contact, "Good", [box("Ok. Good job in retrieving the file. But it seems it is encrypted"
                                            " we need to find a way to decrypt it. I am hearing that a website has"
                                            " a very good decryptor on their server but i don't know the ip :/."
                                            " Anyways here is a little tool to help you and the name of their webpage"
                                            " is www.r2b.net")])
            contact.attachments = [File.fls["Webc"]]
            print("New message.")
        elif part == 4 and mess == "p4":
            self.story += 1
            add_email(contact, "Hack the server", [box("Cool, you found the ip. Now hack their server "
                                                       "and get the decryptor ;)")])
            print("New message.")

        elif part == 5 and mess == "p5":
            self.story += 1
            add_email(contact, "More software", [box("The file you stole points to a server. There is a great "
                                                     "hacking tool on it, but you will need the 'LAN' to "
                                                     "find the mainframe.")])
            contact.attachments = [File.fls["LAN"]]
            print("New message.")
        elif part == 6 and mess == "p6":
            self.story += 1
            add_email(contact, "Well done", [box("All right. Now just decrypt the file and follow the trail : )")])
            print("New message.")

    def execute(self, command):
        command = command.split(" ")
        cmd = command[0]
        if cmd == "help":
            print("'help' - to show this screen\n'ls' - to list files in current directory"
                  "\n'mkdir [folder_name]' - to make a new folder\n'cd [path]' - to change current directory\n"
                  "'mv [filename] [folder_path]' - to move a file to another folder\n'connect' - to connect to"
                  " another computer.\n'email' - to access emails\n'dis' - to disconnect from a computer\n"
                  "'download' - to download files\n'space' - to see current memory\n'run' - to open a file\n"
                  "'hrun' - to run files from your computer when connected to another"
                  "\n'web [url]' - to go to a website")

        elif cmd == "admin":
            print("Welcome Shadow")
            self.bash = "Developer#> "
            self.dir.folder.append(File.fls["Portscanner"])
            self.dir.folder.append(File.fls["Ncrack"])
            self.dir.folder.append(File.fls["Webc"])
            self.dir.folder.append(File.fls["Decryptor"])
            self.dir.folder.append(File.fls["ObjtxtFile1"])
            self.dir.folder.append(File.fls["Dictionary"])

        elif cmd == "story":
            part = int(input("Enter part: "))
            self.story = part

        elif cmd == "creds":
            ls = [obj1, obj3]
            for x in ls:
                print("{} {} - ports: {}".format(x.name, x.ip, list(map(lambda y: y.number, x.ports))))

        elif cmd == "ls":
            for x in self.dir.folder:
                print(x.name)
            for folder in self.harddrive:
                if folder.path == self.path + "/" + folder.name:
                    print("FOLDER[{}]".format(folder.name))

        elif cmd == "email":
            while True:
                print("Contacts: ")
                for x, y in enumerate(self.mails, start=1):
                    add = check_unread(y)
                    print("{}. {}{}{}".format(x, add, y.name, list(map(lambda z: z.name, y.attachments))))
                ent = input("Enter contact number to access('b' - to get back, 'd' - to download attachments): ")
                if ent == "b":
                    break
                elif ent == "d":
                    nm = int(input("Enter number of contact to get attachments from: "))
                    cont = self.mails[nm-1]
                    fls = cont.attachments
                    self.download(fls, self)
                else:
                    cont = self.mails[int(ent)-1]
                    while True:
                        print("Emails from '{}'".format(cont.name))
                        for x, y in enumerate(cont.emails, start=1):
                            add = ""
                            if y.unread:
                                add = "*"
                            print("{}. {}{}".format(x, add, y.title))
                        ent = input("Enter message number to view('b' - to get back, 'r' - to reply): ")
                        if ent == "b":
                            break
                        if ent == "r":
                            ent = input("Enter message: ")
                            self.reply(cont, ent)
                            continue
                        email = cont.emails[int(ent)-1]
                        email.unread = False
                        print("Content of message " + email.title + ":")
                        for x in email.content:
                            print(x)

        elif cmd == "web":
            page = command[1]
            if page == "www.h4u.com":
                self.download([File.fls["Portscanner"], File.fls["Ncrack"]], self)
                if self.story == 2:  # progress story line
                    self.reply(self.mails[0], "p2")  # if first time here

            elif page == "www.r2b.net":
                print("Welcome to r2b.")
                while True:
                    print("""
                    'e' - to disconnect
                    'd' - to download files
                    """)
                    ent = input("Choose: ")
                    if ent == "e":
                        break
                    elif ent == "d":
                        print("Connecting...")
                        time.sleep(1)
                        if self.crawling:
                            print("Crawler intercepting signal...")
                            time.sleep(1)
                            print("Sending request...")
                            time.sleep(2)
                        print("Access Denied.")
                        print("You don't have permission to download files")
                        if self.crawling:
                            print("Response caught.")
                            print("Analyzing...")
                            time.sleep(2)
                            print("Server ip found: {}".format(obj2.ip))
                            if self.story == 4:
                                self.reply(self.mails[0], "p4")
            elif page == "www.metasploit.com":
                pass  # download msf.exe
            else:
                print("Unresolved web address. :/")

        elif cmd == "run":
            file = command[1]
            file = search(self.dir.folder, "name", file)
            if file == False:
                print("No such file found.")
            else:
                file.run(self)

        elif cmd == "hrun":
            host = Instance.host
            print("Files on host:")
            for x in host.dir.folder:
                print(x.name)
            file = input("Enter filename: ")
            file = search(host.dir.folder, "name", file)
            if file == False:
                print("No such file found.")
            else:
                file.run([host, self])

        elif cmd == "space":
            print("Memory: {}/{}".format(self.used, self.space))

        elif cmd == "mkdir":
            name = command[1]
            path = self.path + "/" + name
            folder = Dirs(name, path)
            self.harddrive.append(folder)
            print("Folder " + name + " created.")

        elif cmd == "cd":
            if command[1] == "..":
                path = re.search(r"\w+/(?P<gr>/\w+)+(/\w+)$", self.path).group("gr")
                self.bash = path + "#> "
                self.dir = search(self.harddrive, "path", path)

            elif command[1] == "../":
                path = re.search(r"\w+", self.path).group()
                self.path = path
                self.dir = search(self.harddrive, "path", path)
                self.bash = path + "#> "

            else:
                if command[1][0] != "/":
                    command[1] = "/" + command[1]
                path = self.path + command[1]
                self.bash = path + "#> "
                self.path = path
                self.dir = search(self.harddrive, "path", path)
        elif cmd == "mv":
            file = command[1]
            folder = command[2]
            file = search(self.dir.folder, "name", file)
            folder = search(self.harddrive, "path", folder)
            folder.folder.append(copy.deepcopy(file))
            self.dir.folder.remove(file)
            print("File moved to " + folder.path)

        elif cmd == "connect":
            ip = input("Enter ip to connect: ")
            comp = search(PC.all_pc, "ip", ip)
            if comp == False:
                print("No computer with that ip")
            else:
                port = int(input("Enter port: "))
                port = search(comp.ports, "number", port)
                if port == False:
                    print("Wrong port.")
                elif port.state == "closed":
                    print("Port is closed.")
                else:
                    user = input("Enter username: ")
                    password = input("Enter password: ")
                    if user == port.user and password == port.password:
                        Instance.i = comp
                        print("Connected to " + ip)
                    else:
                        print("Wrong credentials.")

        elif cmd == "download":
            fls = []
            while True:
                self.execute("ls")
                names = [x.name for x in fls]
                file = input("Type filename(current files: {}) 'd' - to download 'c' - to cancel: ".format(names))
                if file == "c":
                    break
                elif file == "d":
                    my_pc = Instance.host
                    self.download(fls, my_pc)
                    if my_pc.story == 3:
                        contact = my_pc.mails[0]
                        my_pc.reply(contact, "p3")
                    if my_pc.story == 6:
                        contact = my_pc.mails[0]
                        my_pc.reply(contact, "p6")
                    break
                else:
                    file = search(self.dir.folder, "name", file, True)
                    fls.append(file)

        elif cmd == "dis":
            Instance.i = Instance.host
            print("Disconnected.")



    def download(self, fls, obj):
        print("{} files are trying to download.".format(len(fls)))
        while True:
            ent = input("Enter('y' - to download then, 'c' - to cancel, 'a' - for more info about the files.): ")
            if ent == "a":
                for x in fls:
                    print("{} {}MB".format(x.name, x.size))
            elif ent == "c":
                print("You canceled the download.")
                break
            elif ent == "y":
                size = sum([x.size for x in fls])
                if size > obj.space - obj.used:
                    print("Not enough space to download {}MB".format(size))
                    continue
                print("Downloading...")
                speed = ratio(30, 0.3, size)
                pro = 0
                while pro < 110:
                    print("[" + "#"*int(pro/10) + "] " + str(pro) + "%")
                    time.sleep(speed)
                    pro += 10
                for x in fls:
                    obj.dir.folder.append(copy.deepcopy(x))
                    obj.used += x.size
                print("Files downloaded.")
                break

File.fls["Portscanner"] = File("Portscanner", 30, "exe", Portscanner)
File.fls["Ncrack"] = File("Ncrack", 50, "exe", Ncrack)
File.fls["Webc"] = File("Webcrawler", 60, "exe", Webcrawler)
File.fls["Decryptor"] = File("Decryptor", 60, "exe", Decryptor)
File.fls["LAN"] = File("LAN_connect", 30, "exe", LAN)
File.fls["ObjtxtFile1"] = File("data", 20, "txt", t2a("Some data"), True)
File.fls["Dictionary"] = File("dict", 30, "txt", "pass1, pass2, pass3")
File.fls["Link_to_msf"] = File("link", 30, "txt", t2a("The file is at: www.metasploit.com"), True)
Port.ports.append(Port(25, 1))
Port.ports.append(Port(80, 2))
# Initializing other computers
obj1 = PC("H4n_s0l0", ipgen(), False, 1000, [File.fls["ObjtxtFile1"], File.fls["Dictionary"]])  # the dude with data.txt
obj1.ports.append(Port(25, 1))
obj2 = PC("Admin", ipgen(), False, 1400, [File.fls["Decryptor"]])  # decryptor server
obj2.ports.append(search(Port.ports, "number", 80, True))
obj3 = PC("User", ipgen(), False, 600)  # first LAN
obj3.ports.append(Port(25, 1))
obj3.lan_conn = LAN_con(obj3)
obj4 = PC("Retr0", ipgen(), False, 2000)  # middle
obj4.lan_conn = LAN_con(obj4)
obj5 = PC("Mainframe", ipgen(), False, 2000, [File.fls["Link_to_msf"]])  # has msfconsole 'end'
obj5.ports.append(Port(40, 3, "closed"))
obj5.lan_conn = LAN_con(obj5)
obj3.LAN = [obj4.lan_conn]
obj4.LAN = [obj3.lan_conn, obj5.lan_conn]
obj5.LAN = [obj4.lan_conn]
File.fls["ObjtxtFile1"].content = t2a("So the files are on: {}".format(obj3.ip))
# head()
name = input("Enter name: ")
player = PC(name, ipgen(), True)
player.mails.append(Contacts("Friend", [Contacts.Mail("Offer", [box("I am some one offering you job if you "
                                                              "accept reply with 'Ok'")])]))
Instance.i = player
Instance.host = search(PC.all_pc, "me", True)
print("New emails check mailbox with 'email'")
print("Use 'help' to see available commands")
while True:
    inst = Instance.i
    inst.execute(input(inst.bash))
