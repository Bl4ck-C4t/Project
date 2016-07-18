import time
import random
import re
import threading
import sys
Login = None
IP = None
an_mes = "Hello"
lock = True
class SecondCounter(threading.Thread):
    
    def __init__(self, interval=0.1):
        threading.Thread.__init__(self)
        self.interval = interval 
        self.value = 0
        self.alive = False
    def run(self,stop):
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            self.value += self.interval
            if self.value >= stop:
                return "Time out"
    def peek(self):
        return self.value
    def finish(self):
        self.alive = False
        return self.value
    
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

def box(text, space=False):
    width,b = getTerminalSize()
    hw = int(width/2)
    f = ""
    part = ""
    c = 0
    top = "_"*hw
    if space:
        top = " "*hw + "_"*hw
    f += top + "\n"
    if space:
        f += " "*(hw-1) + "|"
    while c < len(text):
        ch = text[c]
        part += ch      
        if len(part) == hw:
           
            if not(space):
                part += "|"
            if c != len(text):
                part += "\n"
            if space:
                part += " "*(hw-1) + "|"
            f += part
            part = ""
        c += 1
    f += part
    if part != "" and not(space):
        f += " "*(hw-len(part)) + "|"
    if not(space):
        f += "\n" + "_"*hw + "|"
    if space:
        f += "\n"+ " "*(hw-1) + "|" + "_"*hw
    return f


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

def HardCount(hard, file):
    try:
        file1 = file[:file.index(".")]
        ext = file[file.index("."):]
    except ValueError:
        file1 = file
        ext = ""
    file = file1
    c = 0
    for x in hard:
        if x == file + ext:
            c += 1
            file = "{}({})".format(file1, c)
    return file + ext
def search(ls,string):
    for x in ls:
        if str(x) == string:
            return True
    return False

class Dirs:
    Dir = []
    def __init__(self,name,path):
        self.name = name
        self.path = path
        self.folder = []
        self.txt = {}

    def __str__(self):
        return self.path

class Setup:
    hashls = {}
    def __init__(self):
        self.bash = "root#> "
        print("Enter username: ")
        ent = input(self.bash)
        self.home = ent
        self.bash = ent + "#> "
        print("Use 'help' to see commands")
        self.cl = ["cd","mkdir","ls",  "run", "mail", "web", "new","getuid", "help", "space","mv", "connect","rm","cat"]
        self.harddrive = ["explorer.exe", "File.txt"]
        self.txt = {"File.txt":"Something..."}
        self.messages = {"Anonymous":[[box("I am some one offering you job if you accept reply")],""]}
        self.pspace = {"tracer.exe":50,"hashcat.exe":70,"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.space = 2048
        self.used = 30
        self.location = self.home
        self.generated = False
        self.crawling = False
        self.mis1 = True
        self.mis2 = True
        self.mis3 = True
        self.hash = False
        self.LAN = False
        self.LAN_net = None
        self.uid = "NT/Authority System"
        self.getsys = []
        Dirs.Dir.append(Dirs(self.home, self.home))
        Dirs.Dir[0].folder = self.harddrive
        Dirs.Dir[0].txt = self.txt

    def repshow(self,name,tm=1):
        print(self.messages[name][0][-1])
        time.sleep(tm)
        
    def searchF(self,name):
        for x in Dirs.Dir:
            if str(x) == name:
                return x
        return None
    
    def run(self, pr):
        fl = re.search(r"\[e\]",pr)
        if fl != None:
            print("File encrypted and cannot be opened")
        else:
            if len(pr) < 3:
                print("Wrong syntax: run [program.extension]")
            elif pr[::-1][:3] == "txt" or pr[::-1][:4] == "html":
                print("Can't use run on non '.exe' files use 'cat' instead")
                
            elif pr in self.harddrive and pr[::-1][:3] == "exe":
                if pr == "Ncrack.exe":
                    Ncrack()
                else: 
                    a = pr[::-1][4:][::-1]
                    getattr(Setup, a)(self)
                
            else:
                print("Program not found or unable to run")

    def admin(self):
        self.harddrive.append("hashdump_install.exe")
        self.used += self.pspace["hashdump_install.exe"]
        self.harddrive.append("data[e].txt")
        self.txt["data[e].txt"] = t2a("An0Nym0us:If you are done with the job just connect to the station(ip:95.126.234.24)")
        self.used += 15
        self.harddrive.append("Ncrack.exe")
        self.harddrive.append("Port_scanner.exe")
        self.harddrive.append("Web_crawler.exe")
        self.harddrive.append("Web_open.exe")
        self.harddrive.append("Decryptor.exe")
        self.harddrive.append("LAN_installer.exe")
        self.harddrive.append("msf.exe")
        self.harddrive.append("hashcat.exe")
        self.harddrive.append("tracer.exe")
        self.run("LAN_installer.exe")
        self.run("hashdump_install.exe")
        print("Hi shadow!")
        self.bash = "MasterShadow#> "

        
    def ls(self):
        for x in enumerate(self.harddrive, start=1):
            print(str(x[0]) + ". " + x[1])

    def error(self):
        print("Unrecognized/Unknown command. Type 'help' for syntax")
        
    def commands(self, ent):
        comms = re.search(r"( .+)",ent)
        if comms != None:
            comms = comms.group()[1:]
            comms = comms.split(" ")
        ent = re.search(r"(\w+)", ent)
        ent = ent.group()
        
        if "ls" == ent and "ls" in self.cl:
            self.ls()

        elif "admin" == ent:
            self.admin()

        elif "passes" == ent:
            print("PC1: {}, RE4: {}, Station1: {}, MAinframe1: {}".format(PC1.password,RE4.password,Station1.password,Mainframe1.password))

        elif "mkdir" == ent and "mkdir" in self.cl:
            folder_name = comms[0]
            Dirs.Dir.append(Dirs(folder_name, self.location + "/" + folder_name))
            for x in Dirs.Dir:
                if str(x) == self.location:
                    x.folder.append("FOLDER[{}]".format(HardCount(x.folder,folder_name)))
            
        elif "cd" == ent and "cd" in self.cl:
            self.cd(comms[0])

        elif "new" == ent and "new" in self.cl:
            self.new()

        elif "run" == ent and "run" in self.cl:
            self.run(comms[0])

        elif "getuid" == ent and "getuid" in self.cl:
            print(self.uid)

        elif "getsystem" == ent:
            self.getsystem()

        elif "user" == ent and "user" in self.cl:
            print(self.name)

        elif "mv" == ent and "mv" in self.cl:
            self.move(comms[0],comms[1])

        elif "cat" == ent and "cat" in self.cl:
            self.cat(comms[0])

        elif "LAN" == ent and "LAN" in self.cl:
            self.LAN_connect(comms[0],comms[1])

        elif "help" == ent and "help" in self.cl:
            self.help()

        elif "scan" == ent and "scan" in self.cl:
            try:
                print("Results:")
                for x in self.LAN_net:
                    print("({}){}".format(x.__name__,x.lan_address))

            except:
                print("No LAN found")

        elif "mail" == ent and "mail" in self.cl:
            self.mail()

        elif "web" == ent and "web" in self.cl:
            self.web(comms[0])

        elif "hashdump" == ent and "hashdump" in self.cl:
            self.hashdump()

        elif "hashlist" == ent:
            for x in Setup.hashls.keys():
                print("{}: {}".format(x,str(Setup.hashls[x])))

        elif "space" == ent and "space" in self.cl:
            print("You have {}/{}".format(self.used, self.space))

        elif "connect" == ent and "connect" in self.cl:
            if comms == None:
                self.connect()
            else:
                self.connect(comms[0], comms[1])

        elif "rm" == ent and "rm" in self.cl:
            self.ls()
            en = input("Enter file number to delete: ")
            if self.harddrive[int(en)-1] in self.harddrive:
                self.used -= self.pspace[self.harddrive[int(en)-1]]
                print(self.harddrive[int(en)-1] + " deleted.")
                del self.harddrive[int(en)-1]
            else:
                print("{} not found.".format(self.harddrive[int(en)-1]))
            

        elif not(ent in self.cl):
            self.error()
        try:
            if "dis" == ent and "dis" in self.cl:
                global an_mes
                i.me = "mine"
                print("Disconnected.")
                if "data.txt" in s.harddrive and s.mis1:
                    print("New message check mail!")
                    s.messages['Anonymous'][0].append(box("Well done, you recovered the file next i will need you to decrypt it. Use this website to download the decryptor: 'www.RE4.com' for any problems reply this"))
                    an_mes = "Good Job"
                    s.mis1 = False
                if "download.html" in s.harddrive and s.mis2:
                    print("New message check mail!")
                    s.messages['Anonymous'][0].append(box("You got the downloads page just use this tool to connect to the real page :D."))
                    s.messages['Anonymous'].append("Web_open.exe")
                    s.mis2 = False
                if "attack_list.txt" in s.harddrive and s.mis3:
                     print("New message check mail!")
                     s.mis3 = False
                     s.messages['Anonymous'][0].append(box("Nice job the attack_list shows their new target so try to hack in first install the tracer.exe virus and run it on Votepad servers to find this guys before they find you."))
                     s.messages['Anonymous'].append("tracer.exe")
                     

        except IndexError:
            pass
        try:
            if "download" == ent and "download" in self.cl:
                fls = []
                while True:
                    for x in enumerate(self.harddrive, start=1):
                        print(str(x[0]) + "." + " " + x[1])
                    en = input("Select Files to download('d' - confirm, 'c' - cancel)(Current files:{}): ".format(str(fls)))
                    if en == "d":
                        for file in fls:
                            if file in s.harddrive:
                                print("The file {} exist it will be changed to {}".format(file, HardCount(s.harddrive,file)))
                                if file[::-1][:3] == "exe":
                                    s.pspace[HardCount(s.harddrive,file)] = s.pspace[file]
                            if file[::-1][:3] == "exe":
                                self.download(fls, 30, s.harddrive)
                            else:
                                file_txt = self.txt[file]
                                size = len(file_txt)/5
                                if s.used + size <= s.space:
                                    file = HardCount(s.harddrive, file)
                                    s.txt[file] = file_txt
                                    s.pspace[file] = size
                                    s.used += s.pspace[file]
                                    s.harddrive.append(HardCount(s.harddrive, file))
                        print("File/s downloaded!")
                        break
                    elif en == "c":
                        print("Download cancelled")
                        break
                    else:
                        fls.append(self.harddrive[int(en) - 1])
                        

        except IndexError:
            pass
    
    def FolderCheck(self,patch):
        try:
            s.Folder(patch)
        except KeyError:
            return False
        return True
    def cd(self, path):
        if path == "..":
            self.searchF(self.location).folder = self.harddrive
            self.searchF(self.location).txt = self.txt
            new_path = re.findall(r"/\w+",s.location)
            new_path.insert(0, self.home)
            last_folder = new_path.pop()
            new_path = "".join(new_path)
            self.harddrive = self.searchF(new_path).folder
            self.txt = self.searchF(new_path).txt
            self.bash = new_path + "#> "
            self.location = new_path
            
        elif path == "../":
            self.searchF(self.location).folder = self.harddrive
            self.searchF(self.location).txt = self.txt
            self.harddrive = Dirs.Dir[0].folder
            self.txt = Dirs.Dir[0].txt
            self.location = self.home
            self.bash = self.home + "#> "
        else:
            name = path
            path = "/" + path
            self.searchF(self.location).folder = self.harddrive
            self.searchF(self.location).txt = self.txt
            self.location += path
            self.harddrive = self.searchF(self.location).folder
            self.txt = self.searchF(self.location).txt
            self.bash = self.location + "#> "

    def move(self,file,dest):
        ext = re.search(r"\.(?P<ext>\w+)",file).group("ext")
        folder = self.searchF(self.location + "/" + dest)
        if ext == "txt":
            txt = self.txt[file]
            folder.txt[file] = txt
            del self.txt[file]
            self.harddrive.remove(file)
            folder.folder.append(file)
        elif ext == "exe":
            self.harddrive.remove(file)
            folder.folder.append(file)
        
    def new(self):
        print("Enter file name: ")
        name = input(s.bash)
        if name + ".txt" in self.harddrive:
            check = input("File {} already exists. Create {} y/n".format(name + ".txt", HardCount(self.harddrive, name + ".txt")))
            if check == "n":
                print("File not created.")
        print("Enter text: ")
        ent = input(s.bash)
        name = HardCount(self.harddrive, name + ".txt")
        space = int(len(ent) / 10)
        if self.used + space <= self.space:
            self.pspace[name] = space
            self.used += space
            self.txt[name] = ent
            self.harddrive.append(name)
            print("Text written.")
            print("File size " + str(space))

    
    def cat(self,file):
        sr = re.search(r"\[e\]",file)
        if sr == None:
            print("Data of file " + file)
            print(self.txt[file])
        else:
            print("File is encrypted and cannot be opened.")

    def hashdump_install(self):
        print("Installing hashdump...")
        time.sleep(2)
        print("hashdump command installed.")
        print("command cant be used on your own PC")
        print("Remove the installer")
        self.hash = True

    def hashdump(self):
        print("Obtaining os boot key...")
        time.sleep(0.6)
        print("Success")
        time.sleep(0.4)
        print("Collecting hashes...")
        time.sleep(1)
        if not("FOLDER[HASHES]" in s.harddrive):
            Dirs.Dir.append(Dirs("HASHES", s.home + "/HASHES"))
            s.harddrive.append("FOLDER[HASHES]")
        for x in Dirs.Dir:
            if x.path == s.home + "/HASHES":
                mem = int(len(self.hashes) / 10)
                if mem + s.used <= s.space:
                    name = HardCount(x.folder, "({})hash.txt".format(str(IP)))
                    x.folder.append(name) 
                    s.pspace[name] = mem
                    s.txt[name] = self.hashes
                    if not(IP in Setup.hashls.keys()):
                        Setup.hashls[IP] = []
                    Setup.hashls[IP].append(self.hashes)
                    print("Hashes collected and saved at /FOLDER[HASHES]\nUse hashlist to view hashes")
                else:
                    print("No space")
        print("Hashes: " + self.hashes)

    def hashcat(self):
        self.commands("hashlist")
        ip = input("Enter ip: ")
        txt = input("Enter hashes to decrypt: ")
        password = searchC(ip).password
        method = input("[b]rutefore,[d]ictionary: ")
        if method[0] == "b":
            print("Cracking...")
            time.sleep(len(password))
            print("Hash decrypted:\n{}{}".format(txt[:txt.index(":") + 1],password))
        else:
            print("Not such a file")

    def help(self):
        print("ls - list programs\nnew - make a txt file\nrun - runs a program\nmail - check mail\nweb - to access web\nspace - space on harddrive\nconnect - to connect to other computers\ndis - to disconnect from connected computer.\n'getuid' - see current priviliges\n'getsystem' - try to evaluate.")

    def getsystem(self):
        if self.uid != "NT/Authority System":
            if self.uid == "User":
                if 1 in self.getsys:
                    print("System got via technique 1 Named Pipe Impersonation (In Memory/Admin)")
                elif 2 in self.getsys:
                    print("System got via technique 2 Named Pipe Impersonation (Dropper/Admin)")
                elif 3 in self.getsys:
                    print("System got via technique 3 Token Duplication (In Memory/Admin)")
                elif 0 in self.getsys:
                    print("System got via all techniques")
        else:
            print("You already are System admin.")
    def mail(self):
        global an_mes
        for x in enumerate(self.messages, start=1):
            new = ""
            for file in self.messages[x[1]][1:]:
                if not(file in self.harddrive) and file != "":
                    new += "*"
            print(str(x[0]) + ". " + x[1] + "[" + new + str(self.messages[x[1]][-1]) + "]")
        enter = input("Type a contact name to view('e' to exit, 'r [contact name]' to reply', 'd' - to download attachment) ")
        while enter != "e":
            if enter[0] == "r" and len(enter) > 1:
                    if enter[2:] == "Anonymous":
                        self.reply(an_mes)
            elif enter[0] == "r" and len(enter) == 1:
                conti = input("Enter message name: ")
                self.reply(conti)
            elif enter[0] == "d":
                tp = input("Type name of contact to download attachment from: ")
                if tp in self.messages.keys():
                    if self.messages[tp][-1] != "":
                        for x in enumerate(self.messages[tp][1:], start=1):
                            new=""
                            if not(x[1] in self.harddrive):
                                new = "*"
                            print("{}. {}{}".format(str(x[0]),new,x[1]))
                        fl = input("Type file number to download: ")
                        fl = self.messages[tp][int(fl)]
                        memory = self.pspace[fl]
                        self.download([fl], memory, self.harddrive)
                    else:
                        print("No attachment.")
                else:
                    print("Unknown message.")
            else:
                ls = list(self.messages.keys())
                contact = ls[int(enter)-1]
                for boxes in self.messages[contact][0]:
                    print(boxes)
            enter = input("Type a contact name to view('e' to exit, 'r [contact name]' to reply', 'd' - to download attachment) ")
       
    def reply(self, mess):
        global an_mes
        if an_mes == "Hello":
            print("Reply sent")
            self.repshow("Anonymous")
            self.messages['Anonymous'][0].append(box("Ok, what's the job?",True))
            self.repshow("Anonymous")
            self.messages['Anonymous'][0].append(box("So you decieded to take the job ok. So first download these two files from the link 'www.h4u.com' use the 'web' command to do it"))     
            self.repshow("Anonymous")
            an_mes = ""
        if an_mes == "Good Job":
            print("Reply sent")
            self.repshow("Anonymous")
            self.messages['Anonymous'][0].append(box("It gives me erorr 404 and i cant get the file",True))
            self.repshow("Anonymous")
            self.messages['Anonymous'][0].append(box("Hmmm...Ii think the page for the downloads has been moved. Download the attachment and use it on the website. Once you find the ip of the server hack it and download the original download file."))
            self.repshow("Anonymous")
            self.messages['Anonymous'].append("Web_crawler.exe")
            an_mes = ""
            print("New message received check mail!")
        elif an_mes == "":
            print("You don't know what to say.")
            

    def web(self, url):
        if url == "www.h4u.com":
            if "Ncrack.exe" in self.harddrive:
                self.pspace[HardCount(self.harddrive, "Ncrack.exe")] = self.pspace['Ncrack.exe']
            if "Port_scanner.exe" in self.harddrive:
                self.pspace[HardCount(self.harddrive, "Port_scanner.exe")] = self.pspace['Port_scanner.exe']
            self.download(["Ncrack.exe", "Port_scanner.exe"], self.pspace['Ncrack.exe'] + self.pspace['Port_scanner.exe'], self.harddrive)
            self.messages['Anonymous'][0].append(box("So you managed to download the files. Ok so this is what you need to do: with the Port scanner scan for open ports '172.435.211.10' when you find use Ncrack to ahck the password and at the end connect to the computer and download the file data.txt, and also try downloading the file dict.txt - it will be useful later. "))
            time.sleep(0.7)
            print("New message!")

        elif url == "www.RE4.com":
            print("""
         Welcome to RE4.com
         Type 'about' - for the about page
         and '[d]ownloads' - for the downloads
         'e' - to exit
         """)
            ent = input("Select option: ")
            while ent != 'e':
                if ent == "about":
                    print("This website will give you the best possble encrypting and decrypting tools")
                    ent = input("Select option: ")
                elif ent[0] == "d":
                    input("1 file is trying to download proceed?(y/n) ")
                    if self.crawling:
                        print("Attaching to page.")
                        time.sleep(0.5)
                        print("Attaching to page..")
                        time.sleep(0.5)
                        print("Attaching to page...")
                        time.sleep(0.5)
                        print("Connected.")
                        print("Catching response..")
                        time.sleep(0.5)
                        print("Caught response 'Error 404'")
                        print("Checking source..")
                        time.sleep(0.5)
                        print("Error due page move.")
                        time.sleep(0.6)
                        print("Details: Original page: downloads.html, server ip: 173.545.23.4, Sent data: " + ent + " , Caught data: 'Error 404'")
                        print("Stop Crawling from web crawler")
                    print("Error 404")
                    ent = input("Select option: ")

        elif url == "www.R4.com":
            self.download(["Decryptor.exe"],self.pspace['Decryptor.exe'], self.harddrive)
            print("New message check mail.")
            self.messages['Anonymous'][0].append(box("Beutiful now just decrypt the file and send me the text from it."))
            
        else:
            print("Wrong url.")
        

    def download(self, files, size, putin):
        ent = input(str(len(files)) + " files are trying to download.('c - to cancel, 'y' - to download, 'i' - for inforamtion about the files) ")
        while ent != "c":
            if ent == "i":
                print("")
                for x in files:
                    print(x)
                print("")               
            elif ent == "y":
                try:
                    if s.used + size > s.space:
                        print("No space to download files, try deleting some things")
                        c = "c"
                        break
                except NameError:
                    if self.used + size > self.space:
                        print("No space to download files, try deleting some things")
                        c = "c"
                        break
                c = 10
                while c < 110:
                    print(" "+"_"*10);print("|" + "#"*int((c/10)) + "_"*int((10 - (c/10))) + "|"); print(str(c) + "%")
                    c += 10
                    time.sleep(size/60)
                print("Files downloaded")
                for x in files:
                    if type(x) == list or type(x) == tuple:
                        putin.append(HardCount(putin, x[0]))
                        self.used += size
                        
                    else:
                        putin.append(HardCount(putin, x))
                        self.used += size
                break
            else:
                print("Download canceled!")
                break
            ent = input(str(len(files)) + " files are trying to download.('c - to cancel, 'y' - to download, 'i' - for inforamtion about the files) ")
        if ent == "c":
            print("Download canceled!")

            
            
    
            
                
    def connect(self, ip='', port=''):
        global IP
        if ip == '' or port == '':
            ip = input("Enter ip: ")

        port = input("Enter port: ")
        user = input("Enter username: ")
        pas = input("Enter password: ")
        if ip == PC1.address:
            a = PC1
        elif ip == RE4.address:
            a = RE4
        elif ip == Station1.address:
            a = Station1
        elif ip == Mainframe1.address:
            a = Mainframe1
        if int(port) in a.ports:
            if a.name == user and a.password == pas:
                if a == PC1:
                    i.me = "1"
                elif a == RE4:
                    i.me = "2"
                elif a == Station1:
                    i.me = "3"
                elif a == Mainframe1:
                    i.me = "4"
                print("Connected.")
                time.sleep(0.5)
            else:
                print("Wrong details.")
        else:
            print("The port is closed")
        IP = ip
                
    def Port_scanner(self):
        global IPls
        print("""
        Welcome to the Port Scanner
        'p' - to start scaning
        'e' - for exit
    """)

        ent = input("Select option: ")
        if ent == 'p':
            ip = input("Enter ip: ")
            try:
                print("Scanning...")
                time.sleep(1)
                for x in IPls:
                    if ip == x.address:
                        cmp = x
                print(str(len(x.ports)-1) + " ports found")
                for y in cmp.ports:
                    if y == 25:
                          print("25 - Telnet port OPEN")
                    elif y == 80:
                        print("80 - Http port OPEN")
                    elif y == 445:
                        print("445 - SMB port OPEN")
                    elif y == 2556:
                        print("2556 - TCP/UDP port OPEN")
            except:
                print("No such ip.")
        elif ent == 'e':
            print("Goodbye")

    def Web_crawler(self):
        
        while True:
            print("""
        Welcome to the
         _    _  ____  ____       ___  ____    __    _    _  __    ____  ____   
        ( \/\/ )( ___)(  _ \     / __)(  _ \  /__\  ( \/\/ )(  )  ( ___)(  _ \  
         )    (  )__)  ) _ < ___( (__  )   / /(__)\  )    (  )(__  )__)  )   /  
        (__/\__)(____)(____/(___)\___)(_)\_)(__)(__)(__/\__)(____)(____)(_)\_)
        'c' - to start crawling
        'a' - for about
        'e' - for exit
        's' - to stop crawling
      """)
            ent = input("Select option: ")
            if ent == "a":
                print("The crawler is used to catch sends and responses between servers and pages")
            elif ent == "c":
                url = input("Enter page url: ")
                print("Now enter the page from the 'web' ")
                self.crawling = True
            elif ent == "s":
                self.crawling = False
                print("Stoped crawling")
            elif ent == "e":
                break
            

    def Web_open(self):
        self.ls()
        ent = input("Type filename to open website: ")
        if ent in self.harddrive:
            if ent == "download.html":
                print("connecting to www.R4.com...")
                time.sleep(1)
                self.web("www.R4.com")

            else:
                print("Unknown format.")
        else:
            print("File not in harddrive.")

    def Decryptor(self,file=""):
        fl = re.search(r"(.+)\[e\](.+)", file)
        if file == "":
            self.ls()
            file = input("Enter filename: ")
        if file in self.harddrive:
            crypted = self.txt[file]
            decrypted= a2t(crypted)
            print("Analyzing...")
            time.sleep(1)
            print("Encryption found[ASCII]")
            time.sleep(0.5)
            if fl == None:
                print("[-]Not sure if file is encrypted. This will may cause false decryption or failure.")
                time.sleep(2)
            print("Decrypting...")
            time.sleep(0.6)
            if decrypted != None:
                print("[+]File decrypted.")
                time.sleep(0.4)
                print("File info: {}".format(decrypted))
                en = input("Write info to file? y/n ")
                if en == "y" or en == "Y":
                    self.txt[file] = decrypted
                    if fl != None:
                        fl = fl.group(1) + fl.group(2)
                        self.txt[fl] = self.txt[file]
                        del self.txt[file]
                        self.harddrive.remove(file)
                        self.harddrive.append(fl)
                    print("File modified.")
            else:
                print("[-]Decryption failed.")
        else:
            print("File not found.")
        if file == "data.txt":
            self.messages['Anonymous'][0].append(box("Ok, so just follow the trail in the file. btw install this new command from the attachment it's useful for collecting hashes"))
            self.messages['Anonymous'].append("hashdump_install.exe")
            self.messages['Anonymous'][0].append(box("OK, so take this one it is used to exploit vulnarabilities in systems. Scan them first and then find a good exploit. Don't forget to use 'getsystem' to escalate privileges"))
            self.messages['Anonymous'].append("msf.exe")
            self.messages['Anonymous'][0].append(box("Oh, and use this to decrypt the collected hashes"))
            self.messages['Anonymous'].append("hashcat.exe")
            print("New messages!")
        print("Exiting..")

    def LAN_installer(self):
        print("Installing LAN interface...")
        time.sleep(2)
        self.LAN = True
        print("LAN installed")
        print("usage LAN [IP] [username:password](username and password can be hashes) and 'scan' to reveal devices on network.")

    def LAN_connect(self,ip,data):
        a = False
        if self.LAN_net != None:
            for x in self.LAN_net:
                if x.lan_address == ip:
                    if x.hashes == data:
                        a = True
                        i.me = x.n
                        print("Authenting as {}".format(data[:data.index(":")]))
                        time.sleep(0.5)
                        print("Using password: {}".format(data[data.index(":") + 1:]))
                        print("Connected.")
                        time.sleep(0.5)
            if not(a):
                print("Not such a device")

    def msf(self):
        print("""
                   Welcome to
         __    ___  ___                      _       
  /\/\  / _\  / __\/ __\___  _ __  ___  ___ | | ___  
 /    \ \ \  / _\ / /  / _ \| '_ \/ __|/ _ \| |/ _ \ 
/ /\/\ \_\ \/ /  / /__| (_) | | | \__ \ (_) | |  __/ 
\/    \/\__/\/   \____/\___/|_| |_|___/\___/|_|\___| 
                                                     
    """)
        exploit = ""
        ls = ["net_api","spoolss","net_identity","net_trojan","ms09_mail"]
        global IPls
        global IP
        global OBJls
        while True:
            en = input("msfconsole{}#> ".format(exploit))
            comms = en.split(" ")
            en = comms[0]
            comms = comms[1:]
            if en == "help":
                print("'scan [ip] [optional ip in LAN]' - to scan\n'expls' - to see exploits list\n'use [EXPLOIT NAME]' - to load exploit\n'show_options'\n'set [param] [value]' - to change a exploit setting\n'exploit' - to start exploiting ")
                
            elif en == "scan":
                ip = comms[0]
                ip2 = ""
                if len(comms) > 1:
                    ip2 = comms[1]
                for x in IPls:
                    if x.address == ip:
                        print("Scanning...")
                        time.sleep(1)
                        if ip2 != "":
                            for y in x.LAN_net:
                                if y.lan_address == ip2:
                                    x = y
                        try:
                            for vul in x.vuls:
                                print("Vulnerability detected!\nPossible {} exploit".format(vul))
                        except:
                            print("Can't find vulnerabilities")
            
            elif en == "expls":
                print("Exploits: ")
                time.sleep(1)
                for x in ls:
                    if x == "net_api":
                        info = "a simple easy exploit in port 445 although not very common vulnerability"
                    if x == "spoolss":
                        info = "uses user and pass of a computer(JUMP(first rhost)) to hack another system(uses LAN ip) in the JUMP's LAN"
                    if x == "net_identity":
                        info = "finds the global ip addresses of device in the JUMP's LAN"
                    if x == "net_trojan":
                        info = "uploads and runs file on vulnerable systems.(attacks port 2556)"
                    if x == "ms09_mail":
                        info = "attacks port 110(POP3) by sending emails with backdoor or system-scan virus"
                    print("'{}' - {}".format(x,info))
            elif en == "use":
                ex = comms[0]
                if ex in ls:
                    exploit = "({})".format(ex)
                    options = {}
                    if ex == "net_api":
                        options["LHOST"] = "127.0.0.1"
                        options["RHOST"] = ""
                    if ex == "spoolss":
                        options["LHOST"] = "127.0.0.1"
                        options["JUMP"] = ""
                        options["USERNAME"] = ""
                        options["PASSWORD"] = ""
                        options["RHOST"] = ""
                        options["MODE"] = "USER/PASS"
                    if ex == "net_identity":
                        options["JUMP"] = ""
                        options["RHOST"] = ""
                    if ex == "net_trojan":
                        options["LHOST"] = "127.0.0.1"
                        options["RHOST"] = ""
                        options["FILE"] = ""
                    if ex == "ms09_mail":
                        options["LHOST"] = "127.0.0.1"
                        options["RHOST"] = ""
                        options["EMAIL"] = ""
                else:
                    print("no such an exploit")
                    
            elif en == "show_options":
                ex = exploit[1:-1]
                for x in options.keys():
                    print("{}: {}".format(x,options[x]))
                if ex == "spoolss":
                    print("Can work also in HASH mode(uses hash username and decrypted password)")
            

            elif en == "set":
                if comms[0] in options.keys():
                    options[comms[0]] = comms[1]
                    print("{} set to {}".format(comms[0],comms[1]))
                else:
                    print("Unknown param")

            elif en == "exploit":
                ex = exploit[1:-1]
                rhost = ""
                for x in IPls:
                    if x.address == options["RHOST"]:
                          rhost = x
                if ex == "net_api":
                    print("Connecting to target...")
                    time.sleep(0.5)
                    if ex in rhost.vuls:
                        print("[+]Sending stage..")
                        time.sleep(2)
                        print("[+]Session opened!")
                        i.me = rhost.n
                        IP = rhost.address
                        break
                    else:
                        print("[-]Failed to send stage!(Target may not be vulnerable!)")
                if ex == "spoolss":
                    user = options['USERNAME']
                    paswd = options['PASSWORD']
                    jump = options['JUMP']
                    rhost = options['RHOST']
                    mode = options['MODE']
                    print("Connecting to JUMP...")
                    time.sleep(1)
                    for y in IPls:
                        if y.address == jump:
                            jump = y
                    nm = jump.name
                    if mode == "HASH":
                        nm = jump.hashes[:jump.hashes.index(":")]
                    if user == nm and paswd == jump.password:
                        print("[+]Connected to JUMP.")
                        print("Connecting to RHOST")
                        time.sleep(2)
                        for x in jump.LAN_net:
                            if x.lan_address == rhost:
                                rhost = x
                        if rhost != "" and ex in rhost.vuls and rhost in jump.LAN_net:
                            print("[+]Connected to RHOST.")
                            i.me = rhost.n
                            IP = rhost.address
                            break
                        else:
                            print("[-]Failed to connect to RHOST")
                            print("[-]RHOST not vulnerable or wrong RHOST address")
                    else:
                        print("[-]Failed to connect to JUMP")
                        print("[-]Wrong username and password for JUMP.")
                if ex == "net_identity":
                    jump = options['JUMP']
                    addr = options['RHOST']
                    for x in IPls:
                        if x.address == jump:
                            jump = x
                    print("Searching JUMP's LAN...")
                    time.sleep(1)
                    for y in jump.LAN_net:
                        if y.lan_address == addr:
                            ip = y.address
                    print("Found global address of {} --> {}".format(addr,ip))
                if ex == "net_trojan":
                    file = options['FILE']
                    for x in OBJls:
                        if x.address == options['RHOST']:
                            rhost = x
                    if file in self.harddrive:
                        print("Uploading file...")
                        time.sleep(2)
                        rhost.harddrive.append(file)
                        print("File installed.")
                    else:
                        print("{} not in harddrive".format(file))
                    

            elif en == "e":
                print("Goodbye")
                break
                        
            else:
                print("Unknown command")
            
class Instance:

    def __init__(self):
        self.me = "mine"

class Computers:

    
    def randromize(self, ml, mxl):
        min_len = ml
        max_len = mxl
        self.letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
        lenght = random.randint(min_len, max_len)
        c = 0
        self.pas = ""
        self.pas1 = ""
        while c < lenght:
            self.pas += self.letters[random.randint(0,len(self.letters) - 1)]
            self.pas1 += self.letters[random.randint(0,len(self.letters) - 1)]
            c += 1
        self.login = {"172.435.211.10":(self.pas, "brobro", 25), "173.545.23.4":(self.pas, "admin", 80), "95.126.234.24":(self.pas, "root", 445, 21)}
        global Login
        Login = self.login
        return self.pas

class PC1(Setup):
    n = "1"
    address = "172.435.211.10"
    ports = [445,25]
    name = "brobro"
    password = Computers.randromize(Computers,2,5)
    LAN_net = None
    hard = 0.1
    def __init__(self):
        self.getsys = [0,1,2,3]
        self.uid = "NT/Authority System"
        self.hashes = "Administrator:" + str(hash(self.password))
        self.cl = ["ls", "user", "getuid", "run", "mail", "web", "new", "help", "space", "connect","rm","cat","dis","download"]
        self.harddrive = ["explorer.shit","users.txt", "data[e].txt", "diction.txt"]
        self.messages = {"John":[[box("Hey did you heard about that guy yesterday?")], ""]}
        self.txt = {"users.txt":"me, you, him, she, it", "data.txt":t2a("An0Nym0us:If you are done with the job just connect to the station(ip:95.126.234.24)"), "diction.txt":"wert, qwert, asfg, wqdasd, gwqer,12d, 13e 213e1d, 3241dsd3, r4dsxc32,d3dsad34,dsdd, 13szc,13sadsd, 2313dasd"}
        self.bash = "Han_Solo#> "
        self.pspace = {"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.space = 2048
        self.used = 30
        
class RE4(Setup):
    n = "2"
    address = "173.545.23.4"
    ports = [445,80]
    name = "admin"
    LAN_net = None
    password = Computers.randromize(Computers,4,6)
    hard = 0.3
    def __init__(self):
        self.getsys = [0,1,2,3]
        self.uid = "NT/Authority System"
        self.hashes = "Admin:" + str(hash(self.password))
        self.cl = ["ls","user", "getuid", "run", 1, "web", "new", "help", "space","cat","rm","dis","download"]
        self.harddrive = ["server.db", "index.html", "main.html", "color.dll", "download.html"]
        self.bash = "rootRE4#> "
        self.txt = {"download.html":"<!Doctype html>"}
        self.pspace = {"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.space = 4000
        self.used = 400

class Station1(Setup):
    n = "3"
    address = "95.126.234.24"
    lan_address = "192.168.1.3"
    ports = [445,21]
    name = "root"
    vuls = ["net_api"]
    password = Computers.randromize(Computers,3,5)
    hard = 0.2
    def __init__(self):
        self.getsys = [2,3]
        self.uid = "NT/Authority System"
        self.hashes = "User:" + str(hash(self.password))
        self.cl = ["ls", "mail","user", "run","web", "new", "getuid","help", "space","cat","rm","dis","download"]
        self.harddrive = ["yup.txt","explorer.exe", "File.txt"]
        self.bash = "ST1$root#> "
        self.txt = {"yup.txt":"Nope", "File.txt":"0101010101101010101011010101101101010"}
        self.pspace = {"msf.exe":200,"LAN_installer.exe":100,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.messages = {"Admin":[[box("Alright so this is your access.")],"LAN_installer.exe"]}
        self.space = 4000
        self.used = 200
    

class Mainframe1(Setup):
    n = "4"
    address = "224.123.68.23"
    ports = [445]
    vuls = ["spoolss"]
    lan_address = "192.168.1.2"
    LAN_net = [Station1]
    name = "main_root"
    password = Computers.randromize(Computers,8,10)
    hard = 1
    def __init__(self):
        self.getsys = [1]
        self.uid = "NT/Authority System"
        self.hashes = "Mainframe:" + str(hash(self.password))
        self.cl = ["ls",  "run","web", "new","user","getuid","mail", "help", "space","cat","rm","dis","download"]
        self.harddrive = ["attack_list.txt","ddos.exe"]
        self.bash = "MAINFRAME#> "
        self.txt = {"attack_list[e].txt":t2a("We found out that the programm is in Votepad servers ip - 145.79.243.84")}
        self.pspace = {"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.messages = {"ARR":[[box("We are starting to attack RE4"),box("They have too strong defenses so will attack them with the secret weapon"),box("Target is down and we have the Decryptor :)"),box("I think a hacker recently got into RE4 servers. try to take him down")],""]}
        self.space = 8000
        self.used = 1000

class Votepad(Setup):
    n = "5"
    address = "145.79.243.84"
    ports = [445,2556]
    lan_address = "192.168.1.1"
    LAN_net = []
    name = "Pad"
    password = "*"
    hard = 1
    vuls = ["net_trojan"]
    def __init__(self):
        self.getsys = [1]
        self.uid = "NT/Authority System"
        self.hashes = "Vote:" + str(hash(self.password))
        self.cl = ["ls",  "run","web", "new","user","getuid","mail", "help", "space","cat","rm","dis","download"]
        self.harddrive = ["master[e].exe","ddos.exe"]
        self.bash = "Vote#> "
        self.txt = {}
        self.pspace = {"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.messages = {"AN0nIm0s":[[box("Give me the file now!"),box("Fuck off!!",True),box("OK, then >:)")],""]}
        self.space = 8000
        self.used = 1000

class Omnis1(Setup):
    n = "6"
    address = "123.45.40.175"
    ports = [445,25,24]
    lan_address = "192.168.1.1"
    LAN_net = []
    name = "omsu458"
    password = Computers.randromize(Computers,3,5)
    hard = 1
    vuls = ["net_api"]
    def __init__(self):
        self.getsys = [1]
        self.uid = "NT/Authority System"
        self.hashes = "Vote:" + str(hash(self.password))
        self.cl = ["ls",  "run","web", "new","user","getuid","mail", "help", "space","cat","rm","dis","download"]
        self.harddrive = []
        self.bash = "Vote#> "
        self.txt = {}
        self.pspace = {"msf.exe":200,"LAN_installer.exe":160,"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7, "hashdump_install.exe":30}
        self.messages = {"Mainframe":[[box("Ok i uploaded the file to the mainframe.",True),box("Good Job, now just wait until we get the decryptor.")],""]}
        self.space = 8000
        self.used = 1000




print("Please, do not resize your window.")
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
time.sleep(4)
IPls = [PC1,RE4,Station1,Mainframe1,Votepad,Omnis1]
i = Instance()
s = Setup()
pc = PC1()
RE = RE4()
st1 = Station1()
m1 = Mainframe1()
v = Votepad()
o1 = Omnis1()
OBJls = [pc,RE,st1,m1,v,o1]
Station1.LAN_net = [Mainframe1]
def searchC(eq):
    global IPls
    for x in IPls:
        if x.address == eq:
            return x
def Ncrack():
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    while True:
        print("""
        ███╗   ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
        ████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
        ██╔██╗ ██║██║     ██████╔╝███████║██║     █████╔╝ 
        ██║╚██╗██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
        ██║ ╚████║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
        ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
        'm' - to see methods for cracking
        's' - to start seting the cracking
        'e' - to exit
        'a' - for about
        """)
              
        ent = input("Enter option: ")
        if ent == 'm':
            print("You can use dictionary and brute force attacks with Ncrack, bruteforce guesses by trying one after another, dictonary uses a txt file to check password")
        elif ent == 'a':
            print("Ncrack is password breacking tool")
        if ent == 's':
            typ = input("Select method('[b]rute-force','[d]ictionary'): ")
            ip = input("Enter ip: ")
            p = input("Enter port: ")
            if ip == pc.address:
                a = pc
            elif ip == RE.address:
                a = RE
            elif ip == st1.address:
                a = st1
            elif ip == m1.address:
                a = m1
            if int(p) in a.ports:
                    
                if typ == "b" or typ == "bruteforce" or typ == "brute-force":
                        
                    print("Trying to connect...")
                    time.sleep(0.6)
                    print("Connected.")
                    time.sleep(0.3)
                    print("Starting to crack using bruteforce on port " + p)
                    if a.password == "*":
                        time.sleep(4)
                        print("password is changing and cannot be cracked.")
                        break
                    word = ""
                    counter = 0
                    while word != a.password:
                        for x in letters:
                            if x == a.password[counter]:
                                time.sleep(0.1)
                                print("Try " + word + x + " - SUCCESS")
                                word += x
                                counter += 1
                                break
                            else:
                                time.sleep(a.hard)
                                print("Try " + word + x + " - FAILED")
                    print("Password found: " + word)
                    print("The username is " + a.name)

                elif typ == "d" or typ == "dictionary":
                    found = False
                    self.ls()
                    ls = input("Enter dict name: ")
                    if ls in self.harddrive:
                        dic = self.txt[ls]
                        for x in dic:
                            if x != a.password:
                                print(x + " - FAILED")
                            else:
                                print(x + " - SUCCESS")
                                print("username: " + a.name)
                                print("password found: " + x)
                                found = True
                                break
                        if not(found):
                            print("Password not in dictionary.")
                else:
                    print("Unknown port")
        elif ent == 'e':
            break
while True:
    if "tracer.exe" in v.harddrive and lock:
        s.messages['tracer.exe(report)'] = [[],""]
        s.messages['tracer.exe(report)'][0].append(box("Waiting for connection to current server..."))
        s.messages['tracer.exe(report)'][0].append(box("User 123.45.40.175 connected to server."))
        s.messages['tracer.exe(report)'][0].append(box("123.45.40.175 downloaded master[e].exe."))
        s.messages['tracer.exe(report)'][0].append(box("123.45.40.175 deleted master[e].exe."))
        print("Reports from tracer.exe recieved.\nCheck mail")
        lock = False
    if i.me == "mine":
        enter = s.commands(input(s.bash))
    elif i.me == "1":
        enter = pc.commands(input(pc.bash))
    elif i.me == "2":
        enter = RE.commands(input(RE.bash))
    elif i.me == "3":
        enter = st1.commands(input(st1.bash))
    elif i.me == "4":
        enter = m1.commands(input(m1.bash))
    elif i.me == "5":
        enter = m1.commands(input(v.bash))
    if s.hash:
        pc.cl.append("hashdump")
        RE.cl.append("hashdump")
        st1.cl.append("hashdump")
        m1.cl.append("hashdump")
        v.cl.append("hashdump")
        o1.cl.append("hashdump")
    if s.LAN:
        pc.cl.append("LAN")
        RE.cl.append("LAN")
        st1.cl.append("LAN")
        m1.cl.append("LAN")
        pc.cl.append("scan")
        RE.cl.append("scan")
        st1.cl.append("scan")
        m1.cl.append("scan")
        v.cl.append("scan")
        o1.cl.append("scan")
