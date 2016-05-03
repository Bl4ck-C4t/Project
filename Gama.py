import time
import random
class Setup:
    
    def __init__(self):
        c = Computers()
        c.randromize(2,5)
        c.logins()
        self.bash = "root#> "
        print("Enter username: ")
        ent = input(self.bash)
        self.bash = ent + "#> "
        print("Use 'help' to see commands")
        self.cl = ["ls",  "run", "mail", "web", "new", "help", "space", "connect","del"]
        self.harddrive = ["explorer.exe", "File.txt"]
        self.txt = ["Something..."]
        self.messages = {"Hello":["I am some one offering you job if you accept reply", ""]}
        self.files = ["Ncrack", "Port scanner"]
        self.pspace = {"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7}
        self.comp = "mine"
        self.space = 2048
        self.used = 30
        self.hard = None
        self.mes = None
        self.txt = {}
        self.basher = None
        self.generated = False
        self.login = c.login
        self.letters = c.letters
        self.crawling = False


    def admin(self):
        self.harddrive.append("Ncrack.exe")
        self.harddrive.append("Port_scanner.exe")
        self.harddrive.append("Web_crawler.exe")
        print("Hi shadow!")
        self.bash = "MasterShadow#> "


        
    def ls(self):
        for x in enumerate(self.harddrive, start=1):
            print(str(x[0]) + ". " + x[1])

    def error(self):
        print("Unrecognized/Unknown command. Type 'help' for syntax")
        
    def commands(self, ent):
        if self.cl[0:1][0] == ent:
            self.ls()

        elif "admin" == ent:
            self.admin()

        elif self.cl[4:5][0] == ent:
            self.new()

        elif self.cl[1:2][0] == ent[:3]:
            self.run(ent[4:])

        elif self.cl[5:6][0] == ent:
            self.help()

        elif self.cl[2:3][0] == ent[:4]:
            self.mail()

        elif self.cl[3:4][0] == ent[:3]:
            self.web(ent[4:])

        elif self.cl[6:7][0] == ent:
            print("You have {}/{}".format(self.used, self.space))

        elif self.cl[7:8][0] == ent[:7]:
            self.connect(ent[8:], ent[:-3:-1])

        elif self.cl[8:9][0] == ent[:6]:
            if self.hard == None:
                abc = self.harddrive
            elif self.hard != None:
                abc = self.hard
            if ent[7:] == "":
                put = input("File to delete: ")
                ent = ent + " " + put
            if ent[7:] in abc:
                abc.remove(ent[7:])
                self.used -= self.pspace[ent[7:]]
                print(ent[7:] + " deleted.")
            elif not(ent[7:] in abc):
                print("File not in harddrive.")

        elif not(ent in self.cl):
            self.error()
        try:
            if self.cl[9:10][0] == ent:
                s.comp = "mine"
                print("Disconnected.")
                if "data.txt" in self.harddrive:
                    print("New message check mail!")
                    self.messages['Good Job'] = ("Well done, you recovered the file next i will need you to decrypt it. Use this website to download the decryptor: 'www.RE4.com' for any problems reply this", "")
                    c = Computers()
                    c.randromize(4,6)
                if "download.html" in self.harddrive:
                    print("New message check mail!")
                    self.messages['Well done'] = ("You got the downloads page just use this tool to get the files :D.","Web_open.exe")
                    c = Computers()
                    c.randromize(7,9)
        except IndexError:
            pass
        try:
            if self.cl[10] == ent:
                fls = []
                print("Select Files: ")
                for x in enumerate(self.harddrive, start=1):
                    print(str(x[0]) + "." + " " + x[1])
                en = input("Select file to download('d' - confirm, 'c' - cancel) ")
                for x in enumerate(self.harddrive, start=1):
                    print(str(x[0]) + "." + " " + x[1])
                fls.append(self.harddrive[int(en) - 1])
                enter = input("'d' - confirm, 'c' - cancel ")
                if enter == "d" and fls[0][::-1][:3] == "exe":
                    self.download(fls, 30, s.harddrive)
                    print("File downloaded!")
                if fls[0][::-1][:3] == "txt" or fls[0][::-1][:3] == "html":
                    file = fls[0]
                    file_txt = self.txt[file]
                    s.txt[file] = file_txt
                    s.used += s.pspace[file]
                    s.harddrive.append(file)
                    print("File downloaded!")
                else:
                    print("Download cancelled")
                        

        except IndexError:
            pass

    def new(self):
        print("Enter file name: ")
        name = input(s.bash)
        self.harddrive.append(name + ".txt")
        print("Enter text: ")
        ent = input(s.bash)
        space = int(len(ent) / 10)
        if self.used + space <= self.space:
            self.pspace[name] = space
            self.used += space
            self.txt[name + ".txt"] = ent
            print("Text written.")

    def run(self, pr):
        if len(pr) < 3:
            print("Wrong syntax: run [program.extension]")
        elif pr[len(pr) - 1: len(pr) - 4: -1] == "txt" or pr[-1:-4:-1] == "html":
            print("Data of file " + pr)
            print(self.txt[pr])
            
        elif pr in self.harddrive:
            a = ""
            for x in pr:
                if x == ".":
                    break
                else:
                    a += x
            getattr(Setup, a)(self)
            
        else:
            print("Program not found.")

    def help(self):
        print("ls - list programs, new - make a txt file, run - runs a program, mail - check mail, web - to access web, 'space' - space on harddrive, 'connect' - to connect to other computers, 'dis' - to disconnect from connected computer.")

    def mail(self):
        
        for x in enumerate(self.messages, start=1):
            print(str(x[0]) + ". " + x[1] + "(" + self.messages[x[1]][1] + ")")
        enter = input("Type a message to view('e' to exit, 'r [message title]' to reply', 'd' - to download attachment) ")
        while enter != "e":
            if enter[0] == "r" and len(enter) > 1:
                    self.reply(enter[2:])
            elif enter[0] == "r" and len(enter) == 1:
                conti = input("Enter message name: ")
                self.reply(conti)
            elif enter[0] == "d":
                tp = input("Type name of message to download attachment from: ")
                if tp in self.messages.keys():
                    if self.messages[tp][1] != "":
                        memory = 0
                        for x in self.messags[tp][1:]:
                            memory += self.pspace[x]
                        self.download([self.messages[tp][1]], memory, self.harddrive)
                    else:
                        print("No attachment.")
                else:
                    print("Unknown message.")
            else:
                for x in enumerate(self.messages, start=1):
                    if x[0] == int(enter):
                        print("")
                        print("Message: " + self.messages[x[1]][0])
                        break
                for x in enumerate(self.messages, start=1):
                    print(str(x[0]) + ". " + x[1])
            enter = input("Type a message to view('e' to exit, 'r [message title]' to reply', 'd' - to download attachment) ")
       
    def reply(self, mess):
        if mess == "Hello":
            print("Reply sent")
            self.messages['Start working'] = ("So you decieded to take the job ok. So first download these two files from the link 'www.h4u.com' use the 'web' command to do it", "")        
            print("New message received check mail!")
        if mess == "Good Job":
            print("Reply sent")
            self.messages['Problem'] = ("It seems there is a problem with this website. i think the page for the downloads has been moved. Just download the attachment from this mail and use the program on the website reply when ready", "Web_crawler.exe")
            print("New message received check mail!")
        if mess == "Problem":
            print("Reply sent")
            c = Computers()
            c.randromize(4,6)
            self.messages['Hacking time'] = ("Hmm i see... You will need to run the downloads page manualy. Usually you can do this from the website but something is blocking you. You need to access their server and 'run' the file you got from the crawler 'download.html' - right?","")
            print("New message received check mail!")
            

    def web(self, url):
        if url == "www.h4u.com":
            self.download(["Ncrack.exe", "Port_scanner.exe"], self.pspace['Ncrack.exe'] + self.pspace['Port_scanner.exe'], self.harddrive)
            self.messages['Getting used'] = ("So you managed to download the files. Ok so this is what you need to do: with the Port scanner scan for open ports '172.435.211.10' when you find use Ncracj to ahck the password and at the end connect to the computer and download the file data.txt, and also try downloading the file dict.txt - it will be useful later. ", "")
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
                    print("This website will give you the best possble encrypting tools")
                    ent = input("Select option: ")
                elif ent[0] == "d":
                    input("1 file is trying to download proceed?(y/n) ")
                    if self.crawling:
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
            self.download(["Decryptor.exe"],self.pspace['Decryptor.exe'])
            print("New message check mail.")
            self.messages['Nice'] = ("Beutiful now just decrypt the file and send me the text from it.","")
            
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
                if self.used + size > self.space:
                    print("No space to download files, try deleting some things")
                    c = "c"
                    break
                c = 10
                while c < 110:
                    print(" "+"_"*10);print("|" + "#"*int((c/10)) + "_"*int((10 - (c/10))) + "|"); print(str(c) + "%")
                    c += 10
                    time.sleep(size/20)
                print("Files downloaded")
                for x in files:
                    putin.append(x)
                self.used += size
                break
            else:
                print("Download canceled!")
                break
            ent = input(str(len(files)) + " files are trying to download.('c - to cancel, 'y' - to download, 'i' - for inforamtion about the files) ")
        if ent == "c":
            print("Download canceled!")
            
            
            
    def Ncrack(self):
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
        while ent != 'e':
            if ent == 'm':
                print("You can use dictionary and brute force attacks with Ncrack, bruteforce guesses by trying one after another, dictonary uses a txt file to check password")
                ent = input("Enter option: ")
            elif ent == 'a':
                print("Ncrack is password breacking tool")
                ent = input("Enter option: ")
            if ent == 's':
                typ = input("Select method('[b]rute-force','[d]ictionary'): ")
                ip = input("Enter ip: ")
                p = input("Enter port: ")
                if int(p) in self.login[ip][2:]:
                    
                    if typ == "b" or typ == "bruteforce" or typ == "brute-force":
                        
                        print("Trying to connect...")
                        time.sleep(0.6)
                        print("Connected.")
                        time.sleep(0.3)
                        print("Starting to crack using bruteforce on port " + p)
                        word = ""
                        counter = 0
                        while word != self.login[ip][0]:
                            for x in self.letters:
                                if x == self.login[ip][0][counter]:
                                    time.sleep(0.1)
                                    print("Try " + word + x + " - SUCCESS")
                                    word += x
                                    counter += 1
                                    break
                                else:
                                    time.sleep(0.1)
                                    print("Try " + word + x + " - FAILED")
                        print("Password found: " + word)
                        print("The username is " + self.login[ip][1])
                        ent = "e"

                    elif typ == "d" or typ == "dictionary":
                        self.ls()
                        ls = input("Enter dict name: ")
                        if ls in self.harddrive:
                            c = 0
                            for x in self.harddrive:
                                if x == pr:
                                    break
                                if x[len(x) - 1: len(x) - 4: -1] == "txt":
                                    c += 1
                            txt = self.txt[c]
                            for x in txt:
                                print("Sex")
                else:
                    print("Unknown port")
            else:
                ent = input("Enter option: ")
                
    def connect(self, ip, port):
        if ip == '':
            ip = input("Enter ip:port: ")
            for x in ip:
                if x == ":":
                    port = ip[ip.index(x) + 1:]
                    break
        elif ip == "172.435.211.10":
            port = input("Enter port: ")
            user = input("Enter username: ")
            pas = input("Enter password: ")
            if int(port) in self.login[ip][2:]:
                if user == self.login['172.435.211.10'][1] and pas == self.login['172.435.211.10'][0]:
                    print("Connected.")
                    self.comp = "1"
                else:
                    print("Wrong details")
            else:
                print("The port is currently closed")

        elif ip == "173.545.23.4":
            port = input("Enter port: ")
            user = input("Enter username: ")
            pas = input("Enter password: ")
            if int(port) in self.login[ip][2:]:
                if user == self.login['173.545.23.4'][1] and pas == self.login['173.545.23.4'][0]:
                    print("Connected.")
                    pc = RE4()
                    self.hard = self.harddrive
                    self.mes = self.messages
                    self.tx = self.txt
                    self.basher = self.bash
                    self.harddrive = pc.harddrive
                    self.txt = pc.txt
                    self.bash = pc.bash
                    self.cl = ["ls", "run", 123, 1, 7, "help", "space", 8, "del", "dis", "download"]
                    
                else:
                    print("Wrong details")
            else:
                print("Port is curently closed")
                
    def Port_scanner(self):
        print("""
        Welcome to the Port Scanner
        'p' - to start scaning
        'e' - for exit
    """)

        ent = input("Select option: ")
        if ent == 'p':
            ip = input("Enter ip: ")
            if ip in self.login.keys():
                if self.login[ip] != "":
                    print("Scanning...")
                    time.sleep(1)
                    print(str(len(self.login[ip][2:])) + " ports found")
                for x in self.login[ip][2:]:
                    if x == 25:
                          print("25 - Telnet port OPEN")
                    elif x == 80:
                        print("80 - Http port OPEN")
            else:
                print("No such ip.")
        else:
            print("Goodbye")

    def Web_crawler(self):
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
        while ent != "e":
            if ent == "a":
                print("The crawler is used to catch sends and responses between servers and pages")
                ent = input("Select option: ")
            elif ent == "c":
                url = input("Enter page url: ")
                print("Now enter the page from the 'web' ")
                self.crawling = True
                while self.crawling:
                    enter = input(s.bash)
                    if enter == "web " + url:
                        print("Attaching to page.")
                        time.sleep(0.5)
                        print("Attaching to page..")
                        time.sleep(0.5)
                        print("Attaching to page...")
                        time.sleep(0.5)
                        print("Connected.")
                    elif enter == "run Web_crawler.exe":
                        print("Stopped crawling")
                        self.crawling = False
                    else:
                        s.commands(enter)
            elif ent == "s":
                self.crawling = False
                print("Stoped crawling")


    def Web_open(self):
        self.ls()
        ent = input("Type filename to open website: ")
        if ent in self.harddrive or ent in self.hard:
            if ent[-1:-6:-1][::-1] == ".html":
                name = ent[:len(ent)-5]
                if name == "downloads":
                    self.web("www.R4.com")

            else:
                print("Unknown format.")
        else:
            print("File not in harddrive.")
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
            

    def logins(self):
        self.login = {"172.435.211.10":(self.pas, "brobro", 25), "173.545.23.4":(self.pas, "admin", 80)}

class PC1(Setup):
    def __init__(self):
        self.cl = ["ls",  "run", "mail", "web", "new", "help", "space", "connect","del"]
        self.harddrive = ["explorer.shit","users.txt", "data.txt", "diction.txt"]
        self.messages = {"New":("Hey did you heard about that guy yesterday?", "")}
        self.txt = {"users.txt":"me, you, him, she, it", "data.txt":"0xDB38A9477910E9334E3B9262C9847032905BC33DA2FF7B6E4F0C30EE503BDFEB77ED552E043FC205A4C44CB652633438", "diction.txt":"wert, qwert, asfg, wqdasd, gwqer,12d, 13e 213e1d, 3241dsd3, r4dsxc32,d3dsad34,dsdd, 13szc,13sadsd, 2313dasd"}
        self.bash = "Han_Solo#> "
        self.pspace = {"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7}
        self.space = 2048
        self.used = 30
class RE4:


    se = Setup
    harddrive = ["server.db", "index.html", "main.html", "color.dll", "download.html"]
    bash = "root#> "
    txt = ["<!Doctype html>"]
    
s = Setup()
pc = PC1()
pc.cl.append("dis")
pc.cl.append("download")

while True:
    if s.comp == "mine":
        enter = s.commands(input(s.bash))
    elif s.comp == "1":
        enter = pc.commands(input(pc.bash))
