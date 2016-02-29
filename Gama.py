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
        self.messages = {"Hello":("I am some one offering you job if you accept reply", "")}
        self.files = ["Ncrack", "Port scanner"]
        self.pspace = {"dict.txt":200,"data.txt":15,"Decryptor.exe":15,"Web_open.exe":2,"explorer.exe":20, "File.txt":10, "Ncrack.exe":10,"Port_scanner.exe":3,"Web_crawler.exe":7}
        
        self.space = 2048
        self.used = 30
        self.hard = None
        self.mes = None
        self.tx = None
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
        try:
            if self.cl[9:10][0] == ent:
                self.harddrive = self.hard
                self.messages = self.mes
                self.txt = self.tx
                self.bash = self.basher
                self.hard = None
                self.mes = None
                self.tx = None
                self.basher = None
                print("Disconnected.")
                self.cl = ["ls",  "run", "mail", "web", "new", "help", "space", "connect", "del"]
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
                fls.append(self.harddrive[int(en) - 1])
                enter = input("'d' - confirm, 'c' - cancel ")
                if enter == "d" and self.harddrive[int(en) - 1][-1:-4:-1] == "exe": 
                    self.download(fls, 30, self.hard)
                    
                elif enter == "d" and self.harddrive[int(en) - 1][-1:-4:-1] == "txt" or self.harddrive[int(en) - 1][-1:-5:-1][::-1] == "html":
                    c = 0
                    for x in self.harddrive:
                        if x == self.harddrive[int(en) - 1]:
                            break
                        if x[len(x) - 1: len(x) - 4: -1] == "txt":
                            c += 1
                    self.tx.append(self.txt[c-1])
                    if self.harddrive[int(en) - 1][-1:-4:-1] == "txt":
                        self.used += self.pspace[self.harddrive[int(en) - 1][len(self.harddrive[int(en) - 1]) - 4]]
                    
                    self.used += self.pspace[tx]
                    self.hard.append(self.harddrive[int(en) - 1])
                    print("File downloaded")
                else:
                    print("Download cancelled")

        except IndexError:
            pass
        
        else:
            self.error()
            
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
            self.txt.append(ent)
            print("Text written.")

    def run(self, pr):
        if len(pr) < 3:
            print("Wrong syntax: run [program.extension]")
        elif pr[len(pr) - 1: len(pr) - 4: -1] == "txt" or pr[-1:-4:-1] == "html":
            c = 0
            for x in self.harddrive:
                if x == pr:
                    break
                if x[len(x) - 1: len(x) - 4: -1] == "txt" or x[-1:-4:-1] == "html":
                    c += 1
            print("Data of file " + pr)
            print(self.txt[c])
            
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
            if enter[0] == "r":
                    self.reply(enter[2:])
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
            self.mail()
        if mess == "Good Job":
            print("Reply sent")
            self.messages['Problem'] = ("It seems there is a problem with this website. i think the page for the downloads has been moved. Just download the attachment from this mail and use the program on the website reply when ready", "Web_crawler.exe")
            print("New message received check mail!")
            self.mail()
        if mess == "Problem":
            print("Reply sent")
            c = Computers()
            c.randromize(4,6)
            self.messages['Hacking time'] = ("Hmm i see... You will need to run the downloads page manualy. Usually you can do this from the website but something is blocking you. You need to access their server and 'run' the file you got from the crawler 'download.html' - right?","")
            print("New message received check mail!")
            self.mail()

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
                ent = input(str(len(files)) + " files are trying to download.('c - to cancel, 'y' - to download, 'i' - for inforamtion about the files)")
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
                    pc = PC1()
                    self.hard = self.harddrive
                    self.mes = self.messages
                    self.tx = self.txt
                    self.basher = self.bash
                    self.harddrive = pc.harddrive
                    self.messages = pc.mas
                    self.txt = pc.txt
                    self.bash = pc.bash
                    self.cl.append("dis")
                    self.cl.append("download")
                    
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

class PC1:
    
    harddrive = ["explorer.txt","users.txt", "data.txt", "dict.txt"]
    mas = {"New":("Hey did you heard about that guy yesterday?", "")}
    txt = ["me, you, him, she, it", "0xDB38A9477910E9334E3B9262C9847032905BC33DA2FF7B6E4F0C30EE503BDFEB77ED552E043FC205A4C44CB652633438", "wert, qwert, asfg, wqdasd, gwqer,12d, 13e 213e1d, 3241dsd3, r4dsxc32,d3dsad34,dsdd, 13szc,13sadsd, 2313dasd"]
    bash = "Han_Solo#> "

class RE4:


    se = Setup
    harddrive = ["server.db", "index.html", "main.html", "color.dll", "download.html"]
    bash = "root#> "
    txt = ["""<!doctype html><html itemscope="" itemtype="http://schema.org/SearchResultsPage" lang="bg"><head><meta content="/images/branding/RE4g/1x/RE4g_standard_color_128dp.png" itemprop="image"><link href="/images/branding/product/ico/RE4g_lodp.ico" rel="shortcut icon"><meta content="origin" id="mref" name="referrer"><title>http port - RE4 Търсене</title>   <script>(function(){window.RE4={kEI:'ur6bVsq-CMeZsgHR6I_ICw',kEXPI:'1350255,1350276,3700244,3700385,4028790,4029815,4031109,4032678,4033307,4036527,4038012,4038214,4039268,4041776,4042783,4042787,4043041,4043492,4044542,4044606,4044954,4045023,4045096,4045293,4045841,4046043,4046304,4046399,4046835,4046837,4046904,4047449,4047593,4048854,4048909,4048980,4049063,4049550,4049554,4050281,4050780,4050912,4050914,4050981,4051105,4051154,4051540,4051714,4051825,4052316,4052751,4052772,4052776,4052802,4052954,4054037,4054223,4054232,4054284,4055217,4055276,4055390,4055496,4055506,4055718,4055744,4055757,4055996,4056038,4056126,4056127,4056247,4056359,4056366,4056486,4056490,4056611,4056722,4057139,4057169,4057184,4057378,4057552,4057784,4057836,4057859,4058227,8300272,8300290,8502315,8502347,8502691,8502888,8502937,8502986,8503108,8503136,10200083,10201554,10201587',authuser:0,j:{en:1,bv:24,pm:'p',u:'b66fe97',qbp:0},kscs:'b66fe97_24'};RE4.kHL='bg';})();(function(){RE4.lc=[];RE4.li=0;RE4.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||RE4.kEI};RE4.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};RE4.https=function(){return"https:"==window.location.protocol};RE4.ml=function(){return null};RE4.wl=function(a,b){try{RE4.ml(Error(a),!1,b)}catch(d){}};RE4.time=function(){return(new Date).getTime()};RE4.log=function(a,b,d,e,g){a=RE4.logUrl(a,b,d,e,g);if(""!=a){b=new Image;var c=RE4.lc,f=RE4.li;c[f]=b;b.onerror=b.onload=b.onabort=function(){delete c[f]};window.RE4&&window.RE4.vel&&window.RE4.vel.lu&&window.RE4.vel.lu(a);b.src=a;RE4.li=f+1}};RE4.logUrl=function(a,b,d,e,g){var c="",f=RE4.ls||"";if(!d&&-1==b.search("&ei=")){var h=RE4.getEI(e),c="&ei="+h;-1==b.search("&lei=")&&((e=RE4.getLEI(e))?c+="&lei="+e:h!=RE4.kEI&&(c+="&lei="+RE4.kEI))}a=d||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+c+f+"&zx="+RE4.time();/^http:/i.test(a)&&RE4.https()&&(RE4.ml(Error("a"),!1,{src:a,glmm:1}),a="");return a};RE4.y={};RE4.x=function(a,b){RE4.y[a.id]=[a,b];return!1};RE4.load=function(a,b,d){RE4.x({id:a+k++},function(){RE4.load(a,b,d)})};var k=0;})();
RE4.j.b=(!!location.hash&&!!location.hash.match('[#&]((q|fp)=|tbs=rimg|tbs=simg|tbs=sbi)'))
||(RE4.j.qbp==1);RE4.arwt=function(a){a.href=document.getElementById(a.id.substring(1)).href;return!0};(function(){'use strict';var k=this,l=Date.now||function(){return+new Date};var t={};var w=function(a,d){if(null===d)return!1;if("contains"in a&&1==d.nodeType)return a.contains(d);if("compareDocumentPosition"in a)return a==d||Boolean(a.compareDocumentPosition(d)&16);for(;d&&a!=d;)d=d.parentNode;return d==a};var x=function(a,d){return function(b){b||(b=window.event);return d.call(a,b)}},B=function(a){a=a.target||a.srcElement;!a.getAttribute&&a.parentNode&&(a=a.parentNode);return a},C="undefined"!=typeof navigator&&/Macintosh/.test(navigator.userAgent),D="undefined"!=typeof navigator&&!/Opera/.test(navigator.userAgent)&&/WebKit/.test(navigator.userAgent),E={A:1,INPUT:1,TEXTAREA:1,SELECT:1,BUTTON:1},F=function(){this._mouseEventsPrevented=!0},G={A:13,BUTTON:0,CHECKBOX:32,COMBOBOX:13,GRIDCELL:13,LINK:13,LISTBOX:13,MENU:0,MENUBAR:0,MENUITEM:0,MENUITEMCHECKBOX:0,MENUITEMRADIO:0,OPTION:0,RADIO:32,RADIOGROUP:32,RESET:0,SUBMIT:0,TAB:0,TREE:13,TREEITEM:13},H=function(a){return(a.getAttribute("type")||a.tagName).toUpperCase()in aa},I=function(a){return(a.getAttribute("type")||a.tagName).toUpperCase()in ba},aa={CHECKBOX:!0,OPTION:!0,RADIO:!0},ba={COLOR:!0,DATE:!0,DATETIME:!0,"DATETIME-LOCAL":!0,EMAIL:!0,MONTH:!0,NUMBER:!0,PASSWORD:!0,RANGE:!0,SEARCH:!0,TEL:!0,TEXT:!0,TEXTAREA:!0,TIME:!0,URL:!0,WEEK:!0},ca={A:!0,AREA:!0,BUTTON:!0,DIALOG:!0,IMG:!0,INPUT:!0,LINK:!0,MENU:!0,OPTGROUP:!0,OPTION:!0,PROGRESS:!0,SELECT:!0,TEXTAREA:!0};var J=function(){this.v=this.o=null},L=function(a,d){var b=K;b.o=a;b.v=d;return b};J.prototype.s=function(){var a=this.o;this.o&&this.o!=this.v?this.o=this.o.__owner||this.o.parentNode:this.o=null;return a};var M=function(){this.w=[];this.o=0;this.v=null;this.R=!1};M.prototype.s=function(){if(this.R)return K.s();if(this.o!=this.w.length){var a=this.w[this.o];this.o++;a!=this.v&&a&&a.__owner&&(this.R=!0,L(a.__owner,this.v));return a}return null};var K=new J,O=new M;var Q=function(){this.T=[];this.o=[];this.s=[];this.R={};this.v=null;this.w=[];P(this,"_custom")},da="undefined"!=typeof navigator&&/iPhone|iPad|iPod/.test(navigator.userAgent),R=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^\s+/,"").replace(/\s+$/,"")},ea=/\s*;\s*/,ia=function(a,d){return function(b){var c=d;if("_custom"==c){c=b.detail;if(!c||!c._type)return;c=c._type}var e;if("click"==c&&(C&&b.metaKey||!C&&b.ctrlKey||2==b.which||null==b.which&&4==b.button||b.shiftKey))c="clickmod";else{var f;f=b.which||b.keyCode||b.key;D&&3==f&&(f=13);if(13!=f&&32!=f)f=!1;else{var m=B(b),q=(m.getAttribute("role")||m.type||m.tagName).toUpperCase(),h;(h="keydown"!=b.type)||("getAttribute"in m?(h=(m.getAttribute("role")||m.tagName).toUpperCase(),h=!I(m)&&("COMBOBOX"!=h||"INPUT"!=h)&&!m.isContentEditable):h=!1,h=!h);(h=
h||b.ctrlKey||b.shiftKey||b.altKey||b.metaKey||H(m)&&32==f)||((h=m.tagName in E)||(h=m.getAttributeNode("tabindex"),h=null!=h&&h.specified),h=!(h&&!m.disabled));h?f=!1:(m="INPUT"!=m.tagName.toUpperCase()||m.type,h=!(q in G)&&13==f,f=(0==G[q]%f||h)&&!!m)}f&&(c="clickkey")}q=b.srcElement||b.target;f=S(c,b,q,"",null);var g;b.path?(O.w=b.path,O.o=0,O.v=this,O.R=!1,m=O):m=L(q,this);for(;h=m.s();){g=e=h;h=c;var n=g.__jsaction;if(!n){var u=void 0,n=null;"getAttribute"in g&&(n=g.getAttribute("jsaction"));if(u=n){n=t[u];if(!n){for(var n={},y=u.split(ea),z=0,fa=y?y.length:0;z<fa;z++){var r=y[z];if(r){var A=r.indexOf(":"),N=-1!=A,ga=N?R(r.substr(0,A)):"click",r=N?R(r.substr(A+1)):r;n[ga]=r}}t[u]=n}g.__jsaction=n}else n=ha,g.__jsaction=n}"clickkey"==h?h="click":"click"!=h||n.click||(h="clickonly");g={S:h,action:n[h]||"",event:null,W:!1};f=S(g.S,g.event||b,q,g.action||"",e,f.timeStamp);if(g.W||g.action)break}f&&"touchend"==f.eventType&&(f.event._preventMouseEvents=F);if(g&&g.action){if(g="clickkey"==c)g=
B(b),g=(g.type||g.tagName).toUpperCase(),(g=32==(b.which||b.keyCode||b.key)&&"CHECKBOX"!=g)||(g=B(b),q=(g.getAttribute("role")||g.tagName).toUpperCase(),g=g.tagName.toUpperCase()in ca&&"A"!=q&&!H(g)&&!I(g)||"BUTTON"==q);g&&(b.preventDefault?b.preventDefault():b.returnValue=!1);if("mouseenter"==c||"mouseleave"==c)if(g=b.relatedTarget,!("mouseover"==b.type&&"mouseenter"==c||"mouseout"==b.type&&"mouseleave"==c)||g&&(g===e||w(e,g)))f.action="",f.actionElement=null;else{var c={},p;for(p in b)"function"!==
typeof b[p]&&"srcElement"!==p&&"target"!==p&&(c[p]=b[p]);c.type="mouseover"==b.type?"mouseenter":"mouseleave";c.target=c.srcElement=e;c.bubbles=!1;f.event=c;f.targetElement=e}}else f.action="",f.actionElement=null;e=f;a.v&&(p=S(e.eventType,e.event,e.targetElement,e.action,e.actionElement,e.timeStamp),"clickonly"==p.eventType&&(p.eventType="click"),a.v(p,!0));if(e.actionElement){"A"!=e.actionElement.tagName||"click"!=e.eventType&&"clickmod"!=e.eventType||(b.preventDefault?b.preventDefault():b.returnValue=
!1);if(a.v)a.v(e);else{var v;if((p=k.document)&&!p.createEvent&&p.createEventObject)try{v=p.createEventObject(b)}catch(la){v=b}else v=b;e.event=v;a.w.push(e)}if("touchend"==e.event.type&&e.event._mouseEventsPrevented){b=e.event;for(var ma in b);l()}}}},S=function(a,d,b,c,e,f){return{eventType:a,event:d,targetElement:b,action:c,actionElement:e,timeStamp:f||l()}},ha={},ja=function(a,d){return function(b){var c=a,e=d,f=!1;"mouseenter"==c?c="mouseover":"mouseleave"==c&&(c="mouseout");if(b.addEventListener){if("focus"==c||"blur"==c||"error"==c||"load"==c)f=!0;b.addEventListener(c,e,f)}else b.attachEvent&&("focus"==c?c="focusin":"blur"==c&&(c="focusout"),e=x(b,e),b.attachEvent("on"+c,e));return{S:c,U:e,V:f}}},P=function(a,d){if(!a.R.hasOwnProperty(d)){var b=ia(a,d),c=ja(d,b);a.R[d]=b;a.T.push(c);for(b=0;b<a.o.length;++b){var e=a.o[b];e.s.push(c.call(null,e.o))}"click"==d&&P(a,"keydown")}};Q.prototype.U=function(a){return this.R[a]};var W=function(a,d){var b=new ka(d),c;a:{for(c=0;c<a.o.length;c++)if(T(a.o[c],d)){c=!0;break a}c=!1}if(c)return a.s.push(b),b;U(a,b);a.o.push(b);V(a);return b},V=function(a){for(var d=a.s.concat(a.o),b=[],c=[],e=0;e<a.o.length;++e){var f=a.o[e];X(f,d)?(b.push(f),Y(f)):c.push(f)}for(e=0;e<a.s.length;++e)f=a.s[e],X(f,d)?b.push(f):(c.push(f),U(a,f));a.o=c;a.s=b},U=function(a,d){var b=d.o;da&&(b.style.cursor="pointer");for(b=0;b<a.T.length;++b)d.s.push(a.T[b].call(null,d.o))},ka=function(a){this.o=a;this.s=[]},T=function(a,d){for(var b=a.o,c=d;b!=c&&c.parentNode;)c=c.parentNode;return b==c},X=function(a,d){for(var b=0;b<d.length;++b)if(d[b].o!=a.o&&T(d[b],a.o))return!0;return!1},Y=function(a){for(var d=0;d<a.s.length;++d){var b=a.o,c=a.s[d];b.removeEventListener?b.removeEventListener(c.S,c.U,c.V):b.detachEvent&&b.detachEvent("on"+c.S,c.U)}a.s=[]};var Z=new Q;W(Z,window.document.documentElement);P(Z,"click");P(Z,"focus");P(Z,"focusin");P(Z,"blur");P(Z,"focusout");P(Z,"error");P(Z,"load");P(Z,"change");P(Z,"dblclick");P(Z,"input");P(Z,"keyup");P(Z,"keydown");P(Z,"keypress");P(Z,"mousedown");P(Z,"mouseenter");P(Z,"mouseleave");P(Z,"mouseout");P(Z,"mouseover");P(Z,"mouseup");P(Z,"touchstart");P(Z,"touchend");P(Z,"touchcancel");P(Z,"speech");(function(a){window.RE4.jsad=function(d){a.v=d;a.w&&(0<a.w.length&&d(a.w),a.w=null)};window.RE4.jsaac=function(d){return W(a,d)};window.RE4.jsarc=function(d){Y(d);for(var b=!1,c=0;c<a.o.length;++c)if(a.o[c]===d){a.o.splice(c,1);b=!0;break}if(!b)for(c=0;c<a.s.length;++c)if(a.s[c]===d){a.s.splice(c,1);break}V(a)}})(Z);}).call(window);(function(){'use strict';var f=this,g=function(d,e){var b=d.split("."),a=f;b[0]in a||!a.execScript||a.execScript("var "+b[0]);for(var c;b.length&&(c=b.shift());)b.length||void 0===e?a[c]?a=a[c]:a=a[c]={}:a[c]=e};var h=[];g("RE4.jsc.xx",h);g("RE4.jsc.x",function(d){h.push(d)});}).call(window);(function(){RE4.c={c:{a:true,d:false,i:false,m:true,n:false}};RE4.sn='web';(function(){function f(a,b,c){g.push({o:a,v:b,w:c});a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent&&a.attachEvent("on"+b,c)}function e(a,b,c){a.addEventListener?a.removeEventListener(b,c,!1):a.attachEvent&&a.detachEvent("on"+b,c)}var g=[];RE4.timers={};RE4.startTick=function(a,b){var c=b&&RE4.timers[b].t?RE4.timers[b].t.start:RE4.time();RE4.timers[a]={t:{start:c},e:{},it:{},m:{}};(c=window.performance)&&c.now&&(RE4.timers[a].wsrt=Math.floor(c.now()))};RE4.tick=
function(a,b,c){RE4.timers[a]||RE4.startTick(a);c=c||RE4.time();b instanceof Array||(b=[b]);for(var d=0;d<b.length;++d)RE4.timers[a].t[b[d]]=c};RE4.c.e=function(a,b,c){RE4.timers[a].e[b]=c};RE4.bit=function(a,b){RE4.timers[a]||RE4.startTick(a);var c=RE4.timers[a].it[b];c||(c=RE4.timers[a].it[b]=[]);var d=c.push({s:RE4.time()})-1;return function(){c[d]&&(c[d].e=RE4.time())}};RE4.c.b=function(a){var b=RE4.timers.load.m;b[a]&&RE4.wl("ch_mab",{m:a});b[a]=
!0};RE4.c.u=function(a){var b=RE4.timers.load.m;if(b[a]){b[a]=!1;for(a in b)if(b[a])return;RE4.csiReport()}else RE4.wl("ch_mnb",{m:a})};RE4.rll=function(a,b,c){var d=function(b){c(b);e(a,"load",d);e(a,"error",d)};f(a,"load",d);b&&f(a,"error",d)};RE4.ull=function(){for(var a;a=g.shift();)e(a.o,a.v,a.w)};RE4.iTick=function(a){var b=RE4.time();RE4.tick("load","iml",b);a=a.id||a.src||a.name;RE4.tick("iml",a,b);RE4.c.c.a&&RE4.tick("aft",a,b)};RE4.afte=!0;RE4.aft=
function(a){RE4.c.c.a&&RE4.afte&&RE4.tick("aft",a.id||a.src||a.name)};RE4.startTick("load");RE4.c.b("pr");RE4.c.b("xe")})();})();</script><style>[dir='ltr'],[dir='rtl']{unicode-bidi:-moz-isolate;unicode-bidi:isolate}bdo[dir='ltr'],bdo[dir='rtl']{unicode-bidi:bidi-override;unicode-bidi:-moz-isolate-override;unicode-bidi:isolate-override}#logo{display:block;height:37px;overflow:hidden;position:relative;width:95px}#logo img{border:0;left:0;position:absolute;top:-41px}#logo span{background:url(/images/nav_logo242.png) no-repeat;cursor:pointer;overflow:hidden}#logocont{z-index:1;padding-left:13px;padding-right:10px;margin-top:-2px;padding-top:6px}.big #logocont{padding-left:13px;padding-right:12px}.sbibod{background-color:#fff;border:1px solid #d9d9d9;border-top-color:none;height:38px;vertical-align:top;}.srp .sbibod{border-right:0}.lst{border:0;margin-top:5px;margin-bottom:0}.lst:focus{outline:none}#lst-ib{color:#000}.gsfi,.lst{font:16px arial,sans-serif;line-height:26px !important;height:26px !important;}#gs_st0{line-height:38px;padding:0 8px;margin-top:-1px;position:static}.gsfs{font:16px arial,sans-serif}.lsb{background:transparent;border:0;font-size:0;height:30px;outline:0;width:100%}.sbico{background:url(/images/nav_logo242.png) no-repeat -107px -55px;color:transparent;display:inline-block;height:24px;width:24px;margin:7px auto}#sblsbb{text-align:center;border-bottom-left-radius:0;border-top-left-radius:0;height:40px;margin:0;padding:0;width:40px;min-width:38px !important;background-color:#4285f4;background-image:none;border:none;}#sblsbb:hover{background-image:none;border:none;background-color:#3b78e7}#sblsbb:active{background-color:#3367d6}#sbds{border:0;margin-left:0}.hp .nojsb,.srp .jsb{display:none}.kpbb,.kprb,.kpgb,.kpgrb{-moz-border-radius:2px;border-radius:2px;color:#fff}.kpbb:hover,.kprb:hover,.kpgb:hover,.kpgrb:hover{-moz-box-shadow:0 1px 1px rgba(0,0,0,0.1);box-shadow:0 1px 1px rgba(0,0,0,0.1);color:#fff}.kpbb:active,.kprb:active,.kpgb:active,.kpgrb:active{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);box-shadow:inset 0 1px 2px rgba(0,0,0,0.3)}.kpbb{background-color:#4d90fe;background-image:-moz-linear-gradient(top,#4d90fe,#4787ed);background-image:linear-gradient(top,#4d90fe,#4787ed);border:1px solid #3079ed}.kpbb:hover{background-color:#357ae8;background-image:-moz-linear-gradient(top,#4d90fe,#357ae8);background-image:linear-gradient(top,#4d90fe,#357ae8);border:1px solid #2f5bb7}a.kpbb:link,a.kpbb:visited{color:#fff}.kprb{background-color:#dd4b39;background-image:-moz-linear-gradient(top,#dd4b39,#d14836);background-image:linear-gradient(top,#dd4b39,#d14836);border:1px solid #dd4b39}.kprb:hover{background-color:#c53727;background-image:-moz-linear-gradient(top,#dd4b39,#c53727);background-image:linear-gradient(top,#dd4b39,#c53727);border:1px solid #b0281a;border-bottom-color:#af301f}.kprb:active{background-color:#b0281a;background-image:-moz-linear-gradient(top,#dd4b39,#b0281a);background-image:linear-gradient(top,#dd4b39,#b0281a)}.kpgb{background-color:#3d9400;background-image:-moz-linear-gradient(top,#3d9400,#398a00);background-image:linear-gradient(top,#3d9400,#398a00);border:1px solid #29691d}.kpgb:hover{background-color:#368200;background-image:-moz-linear-gradient(top,#3d9400,#368200);background-image:linear-gradient(top,#3d9400,#368200);border:1px solid #2d6200}.kpgrb{background-color:#f5f5f5;background-image:-moz-linear-gradient(top,#f5f5f5,#f1f1f1);background-image:linear-gradient(top,#f5f5f5,#f1f1f1);border:1px solid #dcdcdc;color:#555}.kpgrb:hover{background-color:#f8f8f8;background-image:-moz-linear-gradient(top,#f8f8f8,#f1f1f1);background-image:linear-gradient(top,#f8f8f8,#f1f1f1);border:1px solid #dcdcdc;color:#333}a.kpgrb:link,a.kpgrb:visited{color:#555}#sfopt{display:inline-block;float:right;line-height:normal}.lsd{font-size:11px;position:absolute;top:3px;left:16px}.tsf{background:none}.tsf-p{position:relative;}.logocont{left:0;position:absolute;}.sfibbbc{padding-bottom:2px;padding-top:3px;width:638px}.sbtc{position:relative}.sbibtd{line-height:0;max-width:650px;overflow:visible;white-space:nowrap}.sbibps{padding:0px 9px 0;padding-top:0 !important;width:570px}.sfopt{height:28px;position:relative}#sform{height:34px}.hp .sfsbc{display:none}#searchform{width:100%}.hp #searchform{position:absolute;top:311px}.srp #searchform{position:absolute;top:15px}#sfdiv{max-width:484px}.hp .big #sfdiv{max-width:568px;}.srp #sfdiv{max-width:600px;overflow:hidden}.srp #tsf{position:relative;top:-8px}.sfsbc{display:inline-block;float:right;margin-right:1px;vertical-align:top;width:40px;margin-right:9px}.sfbg{background:#f1f1f1;height:69px;left:0;position:absolute;width:100%}.sfbgg{background-color:#f1f1f1;border-bottom:1px solid #666;border-color:#e5e5e5;height:69px}#pocs{background:#fff1a8;color:#000;font-size:10pt;margin:0;padding:5px 7px}#pocs.sft{background:transparent;color:#777}#pocs a{color:#11c}#pocs.sft a{color:#36c}#pocs>div{margin:0;padding:0}#cnt{padding-top:15px;}#subform_ctrl{min-height:11px}</style><style id="ostyle">.gb_Xa{display:none!important}@-moz-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}#gbq2{display:block}#gbqf{display:block;margin:0;margin-right:60px;white-space:nowrap}.gbqff{border:none;display:inline-block;margin:0;padding:0;vertical-align:top;width:100%}.gbqfqw,#gbqfb,.gbqfwa{vertical-align:top}#gbqfaa,#gbqfab,#gbqfqwb{position:absolute}#gbqfaa{left:0}#gbqfab{right:0}.gbqfqwb,.gbqfqwc{right:0;left:0;height:100%}.gbqfqwb{padding:0 8px}#gbqfbw{display:inline-block;vertical-align:top}#gbqfb{border:1px solid transparent;border-bottom-left-radius:0;border-top-left-radius:0;height:30px;margin:0;outline:none;padding:0 0;width:60px;-moz-box-shadow:none;box-shadow:none;-moz-box-sizing:border-box;box-sizing:border-box;background:#4285f4;background:-moz-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=1)}#gbqfb:hover{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}#gbqfb:focus{-moz-box-shadow:inset 0 0 0 1px #fff;box-shadow:inset 0 0 0 1px #fff}#gbqfb:hover:focus{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15),inset 0 0 0 1px #fff;box-shadow:0 1px 0 rgba(0,0,0,.15),inset 0 0 0 1px #fff}#gbqfb:active:active{border:1px solid transparent;-moz-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-moz-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=1)}.gbqfi{background-position:-428px 0;display:inline-block;margin:-1px;height:30px;width:30px}.gbqfqw{background:#fff;background-clip:padding-box;border:1px solid #cdcdcd;border-color:rgba(0,0,0,.15);border-right-width:0;height:30px;-moz-box-sizing:border-box;box-sizing:border-box}#gbfwc .gbqfqw{border-right-width:1px}#gbqfqw{position:relative}.gbqfqw.gbqfqw:hover{border-color:#a9a9a9;border-color:rgba(0,0,0,.3)}.gbqfwa{display:inline-block;width:100%}.gbqfwb{width:40%}.gbqfwc{width:60%}.gbqfwb .gbqfqw{margin-left:10px}.gbqfqw.gbqfqw:active,.gbqfqw.gbqfqwf.gbqfqwf{border-color:#4285f4}#gbqfq,#gbqfqb,#gbqfqc{background:transparent;border:none;height:20px;margin-top:4px;padding:0;vertical-align:top;width:100%}#gbqfq:focus,#gbqfqb:focus,#gbqfqc:focus{outline:none}.gbqfif,.gbqfsf{color:#222;font:16px arial,sans-serif}#gbqfbwa{display:none;text-align:center;height:0}#gbqfbwa .gbqfba{margin:16px 8px}#gbqfsa,#gbqfsb{font:bold 11px/27px Arial,sans-serif!important;vertical-align:top}.gb_fa .gbqfqw.gbqfqw,.gb_X .gbqfqw.gbqfqw{border-color:rgba(255,255,255,1);-moz-box-shadow:0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 2px rgba(0,0,0,.2)}.gb_fa #gbqfb,.gb_X #gbqfb{-moz-box-shadow:0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 2px rgba(0,0,0,.2)}.gb_fa #gbqfb:hover,.gb_X #gbqfb:hover{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_fa #gbqfb:active,.gb_X #gbqfb:active{-moz-box-shadow:inset 0 2px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:inset 0 2px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gbqfb,.gbqfba,.gbqfbb{cursor:default!important;display:inline-block;font-weight:bold;height:29px;line-height:29px;min-width:54px;padding:0 8px;text-align:center;text-decoration:none!important;-moz-border-radius:2px;border-radius:2px;-moz-user-select:-moz-none}.gbqfba:focus{border:1px solid #4d90fe;outline:none;-moz-box-shadow:inset 0 0 0 1px #fff;box-shadow:inset 0 0 0 1px #fff}.gbqfba:hover{border-color:#c6c6c6;color:#222!important;-moz-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15);background:#f8f8f8;background:-moz-linear-gradient(top,#f8f8f8,#f1f1f1);background:linear-gradient(top,#f8f8f8,#f1f1f1);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#f8f8f8,endColorstr=#f1f1f1,GradientType=1)}.gbqfba:hover:focus{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15),inset 0 0 0 1px #fff;box-shadow:0 1px 0 rgba(0,0,0,.15),inset 0 0 0 1px #fff}.gbqfb::-moz-focus-inner{border:0}.gbqfba::-moz-focus-inner{border:0}.gbqfba{border:1px solid #dcdcdc;border-color:rgba(0,0,0,0.1);color:#444!important;font-size:11px;background:#f5f5f5;background:-moz-linear-gradient(top,#f5f5f5,#f1f1f1);background:linear-gradient(top,#f5f5f5,#f1f1f1);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#f5f5f5,endColorstr=#f1f1f1,GradientType=1)}.gbqfba:active{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1)}@-moz-keyframes gb__nb{0%{-moz-transform:scale(0,0);transform:scale(0,0)}20%{-moz-transform:scale(1.4,1.4);transform:scale(1.4,1.4)}50%{-moz-transform:scale(.8,.8);transform:scale(.8,.8)}85%{-moz-transform:scale(1.1,1.1);transform:scale(1.1,1.1)}to{-moz-transform:scale(1.0,1.0);transform:scale(1.0,1.0)}}@keyframes gb__nb{0%{-moz-transform:scale(0,0);transform:scale(0,0)}20%{-moz-transform:scale(1.4,1.4);transform:scale(1.4,1.4)}50%{-moz-transform:scale(.8,.8);transform:scale(.8,.8)}85%{-moz-transform:scale(1.1,1.1);transform:scale(1.1,1.1)}to{-moz-transform:scale(1.0,1.0);transform:scale(1.0,1.0)}}.gb_ac{background-position:-314px -38px;opacity:.55;height:100%;width:100%}.gb_b:hover .gb_ac,.gb_b:focus .gb_ac{opacity:.85}.gb_bc .gb_ac{background-position:-463px 0}.gb_cc{background-color:#cb4437;-moz-border-radius:8px;border-radius:8px;font:bold 11px Arial;color:#fff;line-height:16px;min-width:14px;padding:0 1px;position:absolute;right:0;text-align:center;text-shadow:0 1px 0 rgba(0,0,0,0.1);top:0;visibility:hidden;z-index:990}.gb_dc .gb_cc,.gb_dc .gb_ec,.gb_dc .gb_ec.gb_fc{visibility:visible}.gb_ec{padding:0 2px;visibility:hidden}.gb_gc:not(.gb_hc) .gb_bb,.gb_gc:not(.gb_hc) .gb_ab{left:3px}.gb_cc.gb_ic{-moz-animation:gb__nb .6s 1s both ease-in-out;animation:gb__nb .6s 1s both ease-in-out;-moz-perspective-origin:top right;perspective-origin:top right;-moz-transform:scale(1,1);transform:scale(1,1);-moz-transform-origin:top right;transform-origin:top right}.gb_ic .gb_ec{visibility:visible}.gb_fa .gb_b .gb_ac{background-position:0 0;opacity:.7}.gb_fa .gb_bc .gb_ac{background-position:-279px -38px}.gb_fa .gb_b:hover .gb_ac,.gb_fa .gb_b:focus .gb_ac{opacity:.85}.gb_X .gb_b .gb_ac{background-position:-349px -38px;opacity:1}.gb_X .gb_bc .gb_ac{background-position:-393px 0}.gb_fa .gb_cc,.gb_X .gb_cc{border:none}.gb_gc .gb_jc{font-size:14px;font-weight:bold;top:0;right:0}.gb_gc .gb_b{display:inline-block;vertical-align:middle;-moz-box-sizing:border-box;box-sizing:border-box;height:30px;width:30px}.gb_gc .gb_ab{border-bottom-color:#e5e5e5}.gb_kc{background-color:rgba(0,0,0,.55);color:#fff;font-size:12px;font-weight:bold;line-height:20px;margin:5px;padding:0 2px;text-align:center;-moz-box-sizing:border-box;box-sizing:border-box;-moz-border-radius:50%;border-radius:50%;height:20px;width:20px}.gb_kc.gb_lc{background-position:-194px -21px}.gb_kc.gb_mc{background-position:-194px -46px}.gb_b:hover .gb_kc,.gb_b:focus .gb_kc{background-color:rgba(0,0,0,.85)}#gbsfw.gb_nc{background:#e5e5e5;border-color:#ccc}.gb_fa .gb_kc{background-color:rgba(0,0,0,.7)}.gb_X .gb_kc.gb_kc,.gb_X .gb_dc .gb_kc.gb_kc,.gb_X .gb_dc .gb_b:hover .gb_kc,.gb_X .gb_dc .gb_b:focus .gb_kc{background-color:#fff;color:#404040}.gb_X .gb_kc.gb_lc{background-position:-70px 0}.gb_X .gb_kc.gb_mc{background-position:-219px 0}.gb_dc .gb_kc.gb_kc{background-color:#db4437;color:#fff}.gb_dc .gb_b:hover .gb_kc,.gb_dc .gb_b:focus .gb_kc{background-color:#a52714}.gb_dc .gb_kc.gb_mc{background-position:-194px -46px}.gb_N .gbqfi::before{left:-428px;top:0}.gb_ub .gbqfb:focus .gbqfi{outline:1px dotted #fff}#gbsfw{min-width:400px;overflow:visible}.gb_Eb,#gbsfw.gb_g{display:block;outline:none}#gbsfw.gb_qa iframe{display:none}.gb_Fb{padding:118px 0;text-align:center}.gb_Hb{background:no-repeat center 0;color:#aaa;font-size:13px;line-height:20px;padding-top:76px;background-image:url('//ssl.gstatic.com/gb/images/a/f5cdd88b65.png')}.gb_Hb a{color:#4285f4;text-decoration:none}.gb_ea .gb_b{background-position:-132px -38px;opacity:.55}.gb_fa .gb_ea .gb_b{background-position:-132px -38px}.gb_X .gb_ea .gb_b{background-position:-463px -35px;opacity:1}.gb_ga.gb_ha{min-height:196px;overflow-y:auto;width:320px}.gb_ia{-moz-transition:height .2s ease-in-out;transition:height .2s ease-in-out}.gb_ja{background:#fff;margin:0;min-height:100px;padding:28px;padding-right:27px;text-align:left;white-space:normal;width:265px}.gb_ka{background:#f5f5f5;cursor:pointer;height:40px;overflow:hidden}.gb_la{position:relative}.gb_ka{display:block;line-height:40px;text-align:center;width:320px}.gb_la{display:block;line-height:40px;text-align:center}.gb_la.gb_ma{line-height:0}.gb_ka,.gb_ka:visited,.gb_ka:active,.gb_la,.gb_la:visited{color:#737373;text-decoration:none}.gb_la:active{color:#737373}#gb a.gb_ka,#gb a.gb_ka:visited,#gb a.gb_ka:active,#gb a.gb_la,#gb a.gb_la:visited{color:#737373;text-decoration:none}#gb a.gb_la:active{color:#737373}.gb_la,.gb_ja{display:none}.gb_ca,.gb_ca+.gb_la,.gb_na .gb_la,.gb_na .gb_ja{display:block}.gb_la:hover,.gb_la:active,#gb a.gb_la:hover,#gb a.gb_la:active{text-decoration:underline}.gb_la{border-bottom:1px solid #ebebeb;left:28px;width:264px}.gb_na .gb_ka{display:none}.gb_la:last-child{border-bottom-width:0}.gb_oa .gb_O{display:initial}.gb_oa.gb_pa{height:100px;text-align:center}.gb_oa.gb_pa img{padding:34px 0;height:32px;width:32px}.gb_oa .gb_3{background-image:url('//ssl.gstatic.com/gb/images/p1_8b13e09b.png');background-size:64px 1996px;background-position:0 -552px}.gb_oa .gb_3+img{border:0;margin:8px;height:48px;width:48px}.gb_oa div.gb_qa{background:#ffa;-moz-border-radius:5px;border-radius:5px;padding:5px;text-align:center}.gb_oa.gb_ra,.gb_oa.gb_sa{padding-bottom:0}.gb_oa.gb_ta,.gb_oa.gb_sa{padding-top:0}.gb_oa.gb_sa a,.gb_oa.gb_ta a{top:0}.gb_ua .gb_ka{margin-top:0;position:static}.gb_va{display:inline-block}.gb_wa{margin:-12px 28px 28px;position:relative;width:264px;-moz-border-radius:2px;border-radius:2px;-moz-box-shadow:0 1px 2px rgba(0,0,0,0.1),0 0 1px rgba(0,0,0,0.1);box-shadow:0 1px 2px rgba(0,0,0,0.1),0 0 1px rgba(0,0,0,0.1)}.gb_5{background-image:url('//ssl.gstatic.com/gb/images/p1_8b13e09b.png');background-size:64px 1996px;display:inline-block;margin:8px;vertical-align:middle;height:64px;width:64px}.gb_xa{color:#262626;display:inline-block;font:13px/18px Arial,sans-serif;margin-right:80px;padding:10px 10px 10px 0;vertical-align:middle;white-space:normal}.gb_ya{font:16px/24px Arial,sans-serif}.gb_za,#gb#gb .gb_za{color:#427fed;text-decoration:none}.gb_za:hover,#gb#gb .gb_za:hover{text-decoration:underline}.gb_Aa .gb_ja{position:relative}.gb_Aa .gb_O{position:absolute;top:28px;left:28px}.gb_ka.gb_Ba{display:none;height:0}.gb_Za{background-size:32px 32px;-moz-border-radius:50%;border-radius:50%;display:block;margin:-1px;overflow:hidden;position:relative;height:32px;width:32px}.gb_Za:hover,.gb_Za:focus{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Za:active{-moz-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Za:active::after{background:rgba(0,0,0,.1);-moz-border-radius:50%;border-radius:50%;content:'';display:block;height:100%}.gb_0a{cursor:pointer;line-height:30px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_b.gb_0a{width:auto}.gb_0a:hover,.gb_0a:focus{opacity:.85}.gb_1a .gb_0a,.gb_1a .gb_2a{line-height:26px}#gb#gb.gb_1a a.gb_0a,.gb_1a .gb_2a{font-size:11px;height:auto}.gb_3a{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_4a:hover .gb_3a{opacity:.85}.gb_X .gb_0a,.gb_X .gb_3a{opacity:1}#gb#gb.gb_X.gb_X a.gb_0a,#gb#gb .gb_X.gb_X a.gb_0a{color:#fff}.gb_X.gb_X .gb_3a{border-top-color:#fff;opacity:1}.gb_fa .gb_Za:hover,.gb_X .gb_Za:hover,.gb_fa .gb_Za:focus,.gb_X .gb_Za:focus{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_5a .gb_6a,.gb_7a .gb_6a{position:absolute;right:1px}.gb_6a.gb_R,.gb_8a.gb_R,.gb_4a.gb_R{flex:0 1 auto;flex:0 1 main-size}.gb_9a.gb_W .gb_0a{width:30px!important}.gb_0a~.gb_ab,.gb_0a~.gb_bb{left:auto;right:6.5px}.gb_cb{outline:none}.gb_db,#gb a.gb_db.gb_db,.gb_eb a,#gb .gb_eb.gb_eb a{color:#36c;text-decoration:none}.gb_db:active,#gb a.gb_db:active,.gb_db:hover,#gb a.gb_db:hover,.gb_eb a:active,#gb .gb_eb a:active,.gb_eb a:hover,#gb .gb_eb a:hover{text-decoration:underline}.gb_fb{margin:20px}.gb_gb,.gb_hb{display:inline-block;vertical-align:top}.gb_gb{margin-right:20px;position:relative}.gb_ib{-moz-border-radius:50%;border-radius:50%;overflow:hidden}.gb_jb{background-size:96px 96px;border:none;vertical-align:top;height:96px;width:96px}.gb_kb{background:rgba(78,144,254,.7);bottom:0;color:#fff;font-size:9px;font-weight:bold;left:0;line-height:9px;position:absolute;padding:7px 0;text-align:center;width:96px}.gb_ib .gb_kb{background:rgba(0,0,0,.54)}.gb_lb{font-weight:bold;margin:-4px 0 1px 0}.gb_mb{color:#666}.gb_eb{color:#ccc;margin:6px 0}.gb_eb a{margin:0 10px}.gb_eb a:first-child{margin-left:0}.gb_eb a:last-child{margin-right:0}.gb_hb .gb_nb{background:#4d90fe;border-color:#3079ed;font-weight:bold;margin:10px 0 0 0;color:#fff}#gb .gb_hb a.gb_nb.gb_nb{color:#fff}.gb_hb .gb_nb:hover{background:#357ae8;border-color:#2f5bb7}.gb_ob{background:#f5f5f5;border-top:1px solid #ccc;border-color:rgba(0,0,0,.2);padding:10px 0;width:100%;display:table}.gb_ob .gb_nb{margin:0 20px}.gb_ob>div{display:table-cell;text-align:right}.gb_ob>div:first-child{text-align:left}.gb_ob .gb_pb{display:block;text-align:center}.gb_qb .gb_ab{border-bottom-color:#fef9db}.gb_rb{background:#fef9db;font-size:11px;padding:10px 20px;white-space:normal}.gb_rb b,.gb_db{white-space:nowrap}.gb_sb{background:#f5f5f5;border-top:1px solid #ccc;border-top-color:rgba(0,0,0,.2);max-height:230px;overflow:auto}.gb_tb{border-top:1px solid #ccc;border-top-color:rgba(0,0,0,.2);display:block;padding:10px 20px}.gb_ub .gb_tb:focus .gb_vb{outline:1px dotted #fff}.gb_tb:hover{background:#eee}.gb_tb:first-child,.gb_wb:first-child+.gb_tb{border-top:0}.gb_wb{display:none}.gb_xb{cursor:default}.gb_xb:hover{background:transparent}.gb_yb{border:none;vertical-align:top;height:48px;width:48px}.gb_vb{display:inline-block;margin:6px 0 0 10px}.gb_xb .gb_yb,.gb_xb .gb_vb{opacity:.4}.gb_zb{color:#000}.gb_xb .gb_zb{color:#666}.gb_Ab{color:#666}.gb_Bb{background:#f5f5f5;border-top:1px solid #ccc;border-top-color:rgba(0,0,0,.2);display:block;padding:10px 20px}.gb_Cb{background-position:-244px 0;display:inline-block;margin:1px 0;vertical-align:middle;height:25px;width:25px}.gb_N .gb_Cb::before{left:-244px;top:0}.gb_Db{color:#427fed;display:inline-block;padding:0 25px 0 10px;vertical-align:middle;white-space:normal}.gb_Bb:hover .gb_Db{text-decoration:underline}#gb#gb a.gb_O{color:#404040;text-decoration:none}#gb#gb a.gb_P,#gb#gb span.gb_P{text-decoration:none}#gb#gb a.gb_P,#gb#gb span.gb_P{color:#000}.gb_P{opacity:.75}#gb#gb a.gb_P:hover,#gb#gb a.gb_P:focus{opacity:.85;text-decoration:underline}.gb_Q.gb_R{display:none;padding-left:15px;vertical-align:middle}.gb_Q.gb_R:first-child{padding-left:0}.gb_S.gb_R{display:inline-block}.gb_Q span{opacity:.55;-moz-user-select:text}.gb_T .gb_S.gb_R{flex:0 1 auto;flex:0 1 main-size;display:-webkit-flex;display:flex}.gb_U .gb_S.gb_R{display:none}.gb_Q .gb_P{display:inline-block;line-height:24px;outline:none;vertical-align:middle}.gb_S .gb_P{min-width:60px;overflow:hidden;flex:0 1 auto;flex:0 1 main-size;text-overflow:ellipsis}.gb_V .gb_S .gb_P{min-width:0}.gb_W .gb_S .gb_P{width:0!important}#gb#gb.gb_X a.gb_P,#gb#gb.gb_X span.gb_P,#gb#gb .gb_X a.gb_P,#gb#gb .gb_X span.gb_P{color:#fff}#gb#gb.gb_X span.gb_P,#gb#gb .gb_X span.gb_P{opacity:.7}.gb_Vc{display:inline-block;padding:0 0 0 15px;vertical-align:middle}.gb_Vc:first-child,#gbsfw:first-child+.gb_Vc{padding-left:0}.gb_jc{position:relative}.gb_b{display:inline-block;outline:none;vertical-align:middle;-moz-border-radius:2px;border-radius:2px;-moz-box-sizing:border-box;box-sizing:border-box;height:30px;width:30px;color:#000;cursor:default;text-decoration:none}#gb#gb a.gb_b{color:#000;cursor:default;text-decoration:none}.gb_ab{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:6.5px;top:37px;z-index:1;height:0;width:0;-moz-animation:gb__a .2s;animation:gb__a .2s}.gb_bb{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:6.5px;z-index:1;height:0;width:0;-moz-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:#ccc;border-bottom-color:rgba(0,0,0,.2);top:36px}x:-o-prefocus,div.gb_bb{border-bottom-color:#ccc}.gb_ga{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);-moz-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:0;top:44px;-moz-animation:gb__a .2s;animation:gb__a .2s;-moz-border-radius:2px;border-radius:2px;-moz-user-select:text}.gb_Vc.gb_g .gb_ab,.gb_Vc.gb_g .gb_bb,.gb_Vc.gb_g .gb_ga,.gb_g.gb_ga{display:block}.gb_Vc.gb_g.gb_wd .gb_ab,.gb_Vc.gb_g.gb_wd .gb_bb{display:none}.gb_xd{position:absolute;right:0;top:44px;z-index:-1}.gb_1a .gb_ab,.gb_1a .gb_bb,.gb_1a .gb_ga{margin-top:-10px}.gb_Ca{background:#f8f8f8;border:1px solid #c6c6c6;display:inline-block;line-height:28px;padding:0 12px;-moz-border-radius:2px;border-radius:2px}.gb_Da{background:#f8f8f8;display:inline-block;line-height:28px;padding:0 12px;-moz-border-radius:2px;border-radius:2px}.gb_Ca,#gb a.gb_Ca.gb_Ca,.gb_Da{color:#666;cursor:default;text-decoration:none}#gb a.gb_Da.gb_Da{cursor:default;text-decoration:none}.gb_Da{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-moz-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Da.gb_Da{color:#fff}.gb_Da:hover{-moz-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Da:active{-moz-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-moz-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}.gb_Ib{min-width:127px;overflow:hidden;position:relative;z-index:987}.gb_Jb{position:absolute;padding:0 20px 0 15px}.gb_Kb .gb_Jb{right:100%;margin-right:-127px}.gb_Lb{display:inline-block;outline:none;vertical-align:middle}.gb_Mb .gb_Lb{position:relative;top:2px}.gb_Lb .gb_Nb,.gb_Ob{display:block}.gb_Pb{border:none;display:block;visibility:hidden}.gb_Lb .gb_Nb{background-position:0 -35px;height:33px;width:92px}.gb_Ob{background-repeat:no-repeat}.gb_X .gb_Lb .gb_Nb{background-position:-296px 0}.gb_fa .gb_Lb .gb_Nb{background-position:-97px 0;opacity:.54}.gb_yd{display:inline-block;line-height:normal;position:relative;z-index:987}.gb_Pd .gb_b{background-position:-498px -35px;opacity:.55;height:30px;width:30px}.gb_Pd .gb_b:hover,.gb_Pd .gb_b:focus{opacity:.85}.gb_Pd .gb_ab{border-bottom-color:#f5f5f5}#gbsfw.gb_Qd{background:#f5f5f5;border-color:#ccc}.gb_X .gb_Pd .gb_b{background-position:-428px -35px;opacity:1}.gb_fa .gb_Pd .gb_b{background-position:-498px 0;opacity:.7}.gb_fa .gb_Pd .gb_b:hover,.gb_fa .gb_Pd .gb_b:focus{opacity:.85}.gb_Ie{color:#000;font:13px/27px Arial,sans-serif;left:0;min-width:1152px;position:absolute;top:0;-moz-user-select:-moz-none;width:100%}.gb_Sd{font:13px/27px Arial,sans-serif;position:relative;height:60px;width:100%}.gb_1a .gb_Sd{height:28px}#gba{height:60px}#gba.gb_1a{height:28px}#gba.gb_Je{height:90px}#gba.gb_Je.gb_1a{height:58px}.gb_Sd>.gb_R{height:60px;line-height:58px;vertical-align:middle}.gb_1a .gb_Sd>.gb_R{height:28px;line-height:26px}.gb_Sd::before{background:#e5e5e5;bottom:0;content:'';display:none;height:1px;left:0;position:absolute;right:0}.gb_Sd{background:#f1f1f1}.gb_Ke .gb_Sd{background:#fff}.gb_Ke .gb_Sd::before,.gb_1a .gb_Sd::before{display:none}.gb_fa .gb_Sd,.gb_X .gb_Sd,.gb_1a .gb_Sd{background:transparent}.gb_fa .gb_Sd::before{background:#e1e1e1;background:rgba(0,0,0,.12)}.gb_X .gb_Sd::before{background:#333;background:rgba(255,255,255,.2)}.gb_R{display:inline-block;flex:0 0 auto;flex:0 0 main-size}.gb_R.gb_Le{float:right;order:1}.gb_Me{white-space:nowrap}.gb_T .gb_Me{display:-webkit-flex;display:flex}.gb_Me,.gb_R{margin-left:0!important;margin-right:0!important}.gb_Nb{background-image:url('//ssl.gstatic.com/gb/images/i1_1967ca6a.png');background-size:528px 68px}@media (min-resolution:1.25dppx),(-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25){.gb_Nb{background-image:url('//ssl.gstatic.com/gb/images/i2_2ec824b0.png')}}.gb_9a{min-width:315px;padding-left:30px;padding-right:30px;position:relative;text-align:right;z-index:986;align-items:center;justify-content:flex-end;-moz-user-select:-moz-none}.gb_1a .gb_9a{min-width:0}.gb_9a.gb_R{flex:1 1 auto;flex:1 1 main-size}.gb_8b{line-height:normal;position:relative;text-align:left}.gb_8b.gb_R,.gb_xe.gb_R,.gb_2a.gb_R{flex:0 1 auto;flex:0 1 main-size}.gb_ye,.gb_ze{display:inline-block;padding:0 0 0 15px;position:relative;vertical-align:middle}.gb_xe{line-height:normal;padding-right:15px}.gb_9a .gb_xe.gb_U{padding-right:0}.gb_2a{color:#404040;line-height:30px;min-width:30px;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}#gb.gb_1a.gb_1a .gb_4d,#gb.gb_1a.gb_1a .gb_8b>.gb_ze .gb_5d{background:none;border:none;color:#36c;cursor:pointer;filter:none;font-size:11px;line-height:26px;padding:0;-moz-box-shadow:none;box-shadow:none}#gb.gb_1a.gb_X .gb_4d,#gb.gb_1a.gb_X .gb_8b>.gb_ze .gb_5d{color:#fff}.gb_1a .gb_4d{text-transform:uppercase}.gb_9a.gb_V{padding-left:0;padding-right:29px}.gb_9a.gb_Ae{max-width:400px}.gb_Be{background-clip:content-box;background-origin:content-box;opacity:.27;padding:22px;height:16px;width:16px}.gb_Be.gb_R{display:none}.gb_Be:hover,.gb_Be:focus{opacity:.55}.gb_Ce{background-position:-219px -25px}.gb_De{background-position:-194px 0;padding-left:30px;padding-right:14px;position:absolute;right:0;top:0;z-index:990}.gb_5a:not(.gb_7a) .gb_De,.gb_V .gb_Ce{display:inline-block}.gb_5a .gb_Ce{padding-left:30px;padding-right:0;width:0}.gb_5a:not(.gb_7a) .gb_Ee{display:none}.gb_9a.gb_R.gb_V,.gb_V:not(.gb_7a) .gb_8b{flex:0 0 auto;flex:0 0 main-size}.gb_Be,.gb_V .gb_xe,.gb_7a .gb_8b{overflow:hidden}.gb_5a .gb_xe{padding-right:0}.gb_V .gb_8b{padding:1px 1px 1px 0}.gb_5a .gb_8b{width:75px}.gb_9a.gb_Fe,.gb_9a.gb_Fe .gb_Ce,.gb_9a.gb_Fe .gb_Ce::before,.gb_9a.gb_Fe .gb_xe,.gb_9a.gb_Fe .gb_8b{-moz-transition:width .5s ease-in-out,min-width .5s ease-in-out,max-width .5s ease-in-out,padding .5s ease-in-out,left .5s ease-in-out;transition:width .5s ease-in-out,min-width .5s ease-in-out,max-width .5s ease-in-out,padding .5s ease-in-out,left .5s ease-in-out}.gb_T .gb_9a{min-width:0}.gb_9a.gb_W,.gb_9a.gb_W .gb_8b,.gb_9a.gb_He,.gb_9a.gb_He .gb_8b{min-width:0!important}.gb_9a.gb_W,.gb_9a.gb_W .gb_R{-moz-box-flex:0 0 auto!important;flex:0 0 auto!important}.gb_9a.gb_W .gb_2a{width:30px!important}.gb_Sd ::-webkit-scrollbar{height:15px;width:15px}.gb_Sd ::-webkit-scrollbar-button{height:0;width:0}.gb_Sd ::-webkit-scrollbar-thumb{background-clip:padding-box;background-color:rgba(0,0,0,.3);border:5px solid transparent;-moz-border-radius:10px;border-radius:10px;min-height:20px;min-width:20px;height:5px;width:5px}.gb_Sd ::-webkit-scrollbar-thumb:hover,.gb_Sd ::-webkit-scrollbar-thumb:active{background-color:rgba(0,0,0,.4)}#gb.gb_Pe{min-width:980px}#gb.gb_Pe .gb_Od{min-width:0;position:static;width:0}.gb_Pe .gb_Sd{background:transparent;border-bottom-color:transparent}.gb_Pe .gb_Sd::before{display:none}.gb_Pe.gb_Pe .gb_Q{display:inline-block}.gb_Pe.gb_9a .gb_xe.gb_U{padding-right:15px}.gb_T.gb_Pe .gb_S.gb_R{display:-webkit-flex;display:flex}.gb_Pe.gb_T #gbqf{display:block}.gb_Pe #gbq{height:0;position:absolute}.gb_Pe.gb_9a{z-index:987}sentinel{}#gbq .gbgt-hvr,#gbq .gbgt:focus{background-color:transparent;background-image:none}.gbqfh#gbq1{display:none}.gbxx{display:none !important}#gbq{line-height:normal;position:relative;top:0px;white-space:nowrap}#gbq{left:0;width:100%}#gbq2{top:0px;z-index:986}#gbq4{display:inline-block;max-height:29px;overflow:hidden;position:relative}.gbqfh#gbq2{z-index:985}.gbqfh#gbq2{margin:0;margin-left:0 !important;padding-top:0;position:relative;top:310px}.gbqfh #gbqf{margin:auto;min-width:534px;padding:0 !important}.gbqfh #gbqfbw{display:none}.gbqfh #gbqfbwa{display:block}.gbqfh #gbqf{max-width:572px;min-width:572px}.gbqfh .gbqfqw{border-right-width:1px}
.gbii::before{content:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s32-c-mo/photo.jpg);position:absolute}.gbip::before{content:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s96-c-mo/photo.jpg);position:absolute}@media (min-resolution:1.25dppx),(-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25){.gbii::before{content:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s64-c-mo/photo.jpg)}.gbip::before{content:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s192-c-mo/photo.jpg)}.gbii::before,.gbip::before{-webkit-transform:scale(.5);-moz-transform:scale(.5);-ms-transform:scale(.5);-o-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:0 0;-moz-transform-origin:0 0;-ms-transform-origin:0 0;-o-transform-origin:0 0;transform-origin:0 0}}
.gbii{background-image:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s32-c-mo/photo.jpg)}.gbip{background-image:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s96-c-mo/photo.jpg)}@media (min-resolution:1.25dppx),(-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25){.gbii{background-image:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s64-c-mo/photo.jpg)}.gbip{background-image:url(//lh5.RE4usercontent.com/-1Bowf8B4Ajc/AAAAAAAAAAI/AAAAAAAAAAA/PVYD2YGpUz0/s192-c-mo/photo.jpg)}}
</style><style data-jiis="cc" id="gstyle">body{color:#000;margin:0;overflow-y:scroll}body{background:#fff}a.gb1,a.gb2,a.gb3,.link{color:#1a0dab !important}.ts{border-collapse:collapse}.ts td{padding:0}.g{line-height:1.2;text-align:left}.ti,.bl{display:inline}.ti{display:inline-table}#rhs_block{padding-bottom:15px}a:link,.w,#prs a:visited,#prs a:active,.q:active,.q:visited,.kl:active,.tbotu{color:#1a0dab}.mblink:visited,a:visited{color:#609}.cur,.b{font-weight:bold}.j{width:42em;font-size:82%}.s{max-width:42em}.sl{font-size:82%}.hd{position:absolute;width:1px;height:1px;top:-1000em;overflow:hidden}.f,.f a:link,.m{color:#666}.c h2{color:#666}.mslg cite{display:none}.ng{color:#dd4b39}h1,ol,ul,li{margin:0;padding:0}.g,body,html,input,.std,h1{font-size:small;font-family:arial,sans-serif}.c h2,h1{font-weight:normal}.blk a{color:#000}#nav a{display:block}#nav .i{color:#a90a08;font-weight:bold}.csb,.ss,.micon,.close_btn,.mbi{background:url(/images/nav_logo242.png) no-repeat;overflow:hidden}.csb,.ss{background-position:0 0;height:40px;display:block}.mbi{background-position:-153px -70px;display:inline-block;float:left;height:13px;margin-right:3px;margin-top:4px;width:13px}.mbt{color:#11c;float:left;font-size:13px;margin-right:5px;position:relative}#nav td{padding:0;text-align:center}.ch{cursor:pointer}h3,.med{font-size:medium;font-weight:normal;margin:0;padding:0}#res h3{font-size:18px}.e{margin:2px 0 .75em}.slk div{padding-left:12px;text-indent:-10px}.blk{border-top:1px solid #6b90da;background:#f0f7f9}#cnt{clear:both}#res{padding-right:1em;margin:0 16px}.xsm{font-size:x-small}ol li{list-style:none}.sm li{margin:0}.gl,#foot a,.nobr{white-space:nowrap}#foot #navcnt a{color:#4285f4;font-weight:normal}#foot #navcnt .cur{color:rgba(0,0,0,0.87);font-weight:normal}.sl,.r{display:inline;font-weight:normal;margin:0}.r{font-size:medium}h4.r{font-size:small}.vshid{display:none}.gic{position:relative;overflow:hidden;z-index:0}.nwd{font-size:10px;padding:0 16px 30px 16px;text-align:center}#rhs{display:block;margin-left:712px;padding-bottom:10px;min-width:268px}#nyc{bottom:0;display:none;left:0;margin-left:663px;min-width:317px;overflow:hidden;position:fixed;right:0;visibility:visible}.mdm #nyc{margin-left:683px}.mdm #rhs{margin-left:732px}.big #nyc{margin-left:743px}.big #rhs{margin-left:792px;}body .big #subform_ctrl{margin-left:229px}.rhslink{width:68px}.rhsdw .rhslink{width:156px}.rhsimg{width:70px}.rhsimg.rhsdw{width:158px}.rhsimg.rhsn1st{margin-left:16px}#nyc .rhsvw,#rhs .scrt.rhsvw,#rhs table.rhsvw{border:0}#nyc .rhsvw{padding-left:0;padding-right:0}#rhs .rhsvw{border:1px solid #ebebeb;padding-left:15px;padding-right:15px;position:relative;width:424px}#nyc .rhsvw{width:424px}#center_col .rhsl4,#center_col .rhsl5,#center_col .rhsn5{display:none}#rhs .rhstc4 .rhsvw,#nyc.rhstc4 .rhsvw{width:336px}#rhs .rhstc3 .rhsvw,#nyc.rhstc3 .rhsvw{width:248px}.rhstc4 .rhsg4,.rhstc3 .rhsg4,.rhstc3 .rhsg3{background:none !important;display:none !important}.rhstc5 .rhsl5,.rhstc5 .rhsl4,.rhstc4 .rhsl4{background:none !important;display:none !important}.rhstc4 .rhsn4{background:none !important;display:none !important}.nrgt{margin-left:22px}.mslg .vsc{border:1px solid transparent;border-radius:2px;-moz-border-radius:2px;-moz-transition:opacity .2s ease;margin-top:2px;padding:3px 0 3px 5px;transition:opacity .2s ease;width:250px}.mslg>td{padding-right:6px;padding-top:4px}button.vspib{display:none}div.vspib{background:transparent;bottom:0;cursor:default;height:auto;margin:0;min-height:40px;padding-left:9px;padding-right:4px;position:absolute;right:-37px;top:-2px;width:28px;z-index:3}.nyc_open div.vspib{z-index:103}div.vspib:focus{outline:none}.vspii .vspiic{background:url(/images/nav_logo242.png);background-position:-3px -260px;width:15px;height:13px;margin-left:6px;margin-top:-7px;opacity:.3;position:absolute;top:50%;visibility:hidden}.vsh .vsc:hover .vspii .vspiic{visibility:visible}.vsh .vspib .vspii:hover .vspiic{opacity:1;visibility:visible;-moz-transition:opacity .25s ease}.vsh .vsdth .vspiic{opacity:1;visibility:visible;-moz-transition:opacity 1.5s ease}.nyc_open.vsh .vsdth .vspiic,.nyc_open.vsh .vspib .vspii:hover .vspiic{-moz-transition:0}.vspib:focus .vspiic{opacity:1;visibility:visible}.vsh .vspib:focus .vspiic{opacity:.3;visibility:hidden}.vso .vspiic,.vso .vspib:focus .vspiic{opacity:1;visibility:visible}.vspii{border:1px solid transparent;border-radius:2px;border-right:none;cursor:default;user-select:none;-moz-user-select:none}.vsh.nyc_opening .vsc:hover .vspii,.vsh.nyc_open .vsc:hover .vspii,.vso .vspii{background-color:#fafafa;border-color:#e6e6e6;height:100%}.vsh.nyc_open .mslg .vsc:hover,.vsh.nyc_opening .mslg .vsc:hover{border-right-color:#ebebeb}.vso .vspib{padding-right:0}.nyc_open #nycx{background:url(/images/nav_logo242.png) no-repeat;background-position:-140px -230px;height:11px;width:11px}.vsc{display:inline-block;position:relative;width:100%}#res h3.r{display:block;overflow:hidden;text-overflow:ellipsis;-moz-text-overflow:ellipsis;white-space:nowrap}#res h3.inl{display:inline;white-space:normal}em{font-weight:bold;font-style:normal}ol,ul,li{border:0;margin:0;padding:0}.g{margin-top:0;margin-bottom:23px}.ibk{display:-moz-inline-box;display:inline-block;vertical-align:top}.tsw{width:595px}#cnt{min-width:833px;margin-left:0}.mw{max-width:1197px}.big .mw{max-width:1250px}#cnt #center_col,#cnt #foot{width:528px}.gbh{top:24px}#gbar{margin-left:8px;height:20px}#guser{margin-right:8px;padding-bottom:5px !important}.mbi{margin-bottom:-1px}.uc{padding-left:8px;position:relative;margin-left:128px;}.ucm{padding-bottom:5px;padding-top:5px;margin-bottom:8px}.col{float:left}#leftnavc,#center_col,#rhs{position:relative}#center_col{margin-left:138px;margin-right:254px;padding:0 8px;padding:0 8px 0 8px}.mdm #center_col{margin-left:138px;padding:0 8px}.big #center_col{margin-left:138px;padding:0 8px}#subform_ctrl{font-size:11px;margin-right:480px;position:relative;z-index:99}#subform_ctrl a.gl{color:#1a0dab}#center_col{clear:both}#res{border:0;margin:0;padding:0 8px;}#ires{padding-top:6px}.micon,.close_btn{border:0}.close_btn{background-position:-138px -84px;float:right;height:14px;width:14px}.mitem{border-bottom:1px solid transparent;line-height:29px;opacity:1.0;}.mitem .kl{padding-left:16px}.mitem .kl:hover,.msel .kls:hover{color:#222;display:block}.mitem>.kl{color:#222;display:block}.msel{color:#dd4b39;cursor:pointer}.msel .kls{border-left:5px solid #dd4b39;padding-left:11px}.mitem>.kl,.msel{font-size:13px}#tbd{display:block;min-height:1px}.tbt{font-size:13px;line-height:1.2}.tbnow{white-space:nowrap}.tbos,.tbots{font-weight:bold}.tbst{margin-top:8px}#iszlt_sel.tbcontrol_vis{margin-left:0}.tbpc,.tbpo{font-size:13px}.tbpc,.tbo .tbpo{display:inline}.tbo .tbpc,.tbpo,#set_location_section{display:none}.lco #set_location_section{display:block}#cdr_opt{padding-left:8px;text-indent:0}.tbou #cdr_frm{display:none}#cdr_frm,#cdr_min,#cdr_max{color:rgb(102,102,102)}#cdr_min,#cdr_max{font-family:arial,sans-serif;width:100%}#cdr_opt label{display:block;font-weight:normal;margin-right:2px;white-space:nowrap}a:link,.w,.q:active,.q:visited{cursor:pointer}.osl a,.gl a,#tsf a,a.mblink,a.gl,a.fl,.slk a,.bc a,.flt,a.flt u,.blg a,#appbar a{text-decoration:none}.osl a:hover,.gl a:hover,#tsf a:hover,a.mblink:hover,a.gl:hover,a.fl:hover,.slk a:hover,.bc a:hover,.flt:hover,a.flt:hover u,.tbotu:hover,.blg a:hover{text-decoration:underline}#tads a,#tadsb a,#res a,#rhs a,#taw a{text-decoration:none}#brs a,.nsa,.tbt a,.tbotu:hover,#tbpi,#nycntg a:hover,.fl,.navend span,#botstuff a,.flt:hover u,.mlocsel span,#rhs .gl a,#nav a.pn{text-decoration:none}#ss-box a:hover{text-decoration:none}.osl{color:#777}#gbi,#gbg{border-color:#a2bff0 #558be3 #558be3 #a2bff0}#gbi a.gb2:hover,#gbg a.gb2:hover,.mi:hover{background-color:#558be3}#guser a.gb2:hover,.mi:hover,.mi:hover *{color:#fff !important}#guser{color:#000}#imagebox_bigimages .th{border:0}#epbar{border:1px solid #eee;font-size:small;left:-8px;margin-bottom:10px;padding-bottom:10px;padding-top:5px;padding-left:7px;position:relative;width:548px}#epbar #epb-notice{margin:5px 0}#epbar #epb-lm{margin-right:10px}.vsc:hover .lupin,.intrlu:hover .lupin,.lupin.luhovm,#ires:hover .vsc:hover .lupin.luhovm{background-image:url(/images/mappins_red.png) !important}#ires:hover .lupin.luhovm{background-image:url(/images/mappins_grey.png) !important}.vsc:hover .lucir,.intrlu:hover .lucir,.lucir.luhovm,#ires:hover .vsc:hover .lucir.luhovm{background-image:url(/images/mapcircles_red.png) !important}#ires:hover .lucir.luhovm{background-image:url(/images/mapcircles_grey.png) !important}#foot .ftl{margin-right:12px}#foot{visibility:hidden}#fll a,#bfl a{color:#1a0dab;margin:0 12px;text-decoration:none}.stp{margin:7px 0 17px}body{color:#222}.s{color:#545454}.s .st em,.st.s.std em{color:#6a6a6a}.s a:visited em{color:#609}.s a:active em{color:#dd4b39}.sfcc{width:833px;}.big .sfcc{max-width:1129px}.big #tsf{}#topstuff .obp{padding-top:6px}.slk{margin-top:6px !important}.st{line-height:1.4;word-wrap:break-word}.kt{border-spacing:2px 0;margin-top:1px}.esw{vertical-align:text-bottom;}.cpbb,.kpbb,.kprb,.kpgb,.kpgrb,.ksb{-moz-border-radius:2px;border-radius:2px;cursor:default;font-family:arial,sans-serif;font-size:11px;font-weight:bold;height:27px;line-height:27px;margin:2px 0;min-width:54px;padding:0 8px;text-align:center;-moz-transition:all 0.218s;transition:all 0.218s,visibility 0s;-moz-user-select:none;}.ab_button{-moz-border-radius:2px;border-radius:2px;cursor:default;font-family:arial,sans-serif;font-size:11px;font-weight:bold;height:27px;line-height:27px;margin:2px 0;min-width:54px;padding:0 8px;text-align:center;-moz-transition:all 0.218s;transition:all 0.218s,visibility 0s;-moz-user-select:none;}.kbtn-small{min-width:26px;width:26px}.ab_button.left{-moz-border-radius:2px 0 0 2px;border-radius:2px 0 0 2px;border-right-color:transparent;margin-right:0}.ab_button.right{-moz-border-radius:0 2px 2px 0;border-radius:0 2px 2px 0;margin-left:-1px}.ksb{background-color:#f5f5f5;background-image:-moz-linear-gradient(top,#f5f5f5,#f1f1f1);background-image:linear-gradient(top,#f5f5f5,#f1f1f1);border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,0.1);color:#444;}.ab_button{background-color:#f5f5f5;background-image:-moz-linear-gradient(top,#f5f5f5,#f1f1f1);background-image:linear-gradient(top,#f5f5f5,#f1f1f1);border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,0.1);color:#444;}a.ksb,.div.ksb{color:#444;text-decoration:none;cursor:default}a.ab_button{color:#444;text-decoration:none;cursor:default}.cpbb:hover,.kpbb:hover,.kprb:hover,.kpgb:hover,.kpgrb:hover,.ksb:hover{-moz-box-shadow:0 1px 1px rgba(0,0,0,0.1);box-shadow:0 1px 1px rgba(0,0,0,0.1);-moz-transition:all 0.0s;transition:all 0.0s}.ab_button:hover{-moz-box-shadow:0 1px 1px rgba(0,0,0,0.1);box-shadow:0 1px 1px rgba(0,0,0,0.1);-moz-transition:all 0.0s;transition:all 0.0s}#hdtb-tls:hover{-moz-box-shadow:0 1px 1px rgba(0,0,0,0.1);box-shadow:0 1px 1px rgba(0,0,0,0.1);-moz-transition:all 0.0s;transition:all 0.0s}.ksb:hover{background-color:#f8f8f8;background-image:-moz-linear-gradient(top,#f8f8f8,#f1f1f1);background-image:linear-gradient(top,#f8f8f8,#f1f1f1);border:1px solid #c6c6c6;color:#222;}.ab_button:hover{background-color:#f8f8f8;background-image:-moz-linear-gradient(top,#f8f8f8,#f1f1f1);background-image:linear-gradient(top,#f8f8f8,#f1f1f1);border:1px solid #c6c6c6;color:#222;}#hdtb-tls:hover{background-color:#f8f8f8;background-image:-moz-linear-gradient(top,#f8f8f8,#f1f1f1);background-image:linear-gradient(top,#f8f8f8,#f1f1f1);border:1px solid #c6c6c6;color:#222;}.ksb:active{background-color:#f6f6f6;background-image:-moz-linear-gradient(top,#f6f6f6,#f1f1f1);background-image:linear-gradient(top,#f6f6f6,#f1f1f1);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);}.ab_button:active{background-color:#f6f6f6;background-image:-moz-linear-gradient(top,#f6f6f6,#f1f1f1);background-image:linear-gradient(top,#f6f6f6,#f1f1f1);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);}#hdtb-tls:active{background-color:#f6f6f6;background-image:-moz-linear-gradient(top,#f6f6f6,#f1f1f1);background-image:linear-gradient(top,#f6f6f6,#f1f1f1);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);}.ksb.ksbs,.ksb.ksbs:hover{background-color:#eee;background-image:-moz-linear-gradient(top,#eee,#e0e0e0);background-image:linear-gradient(top,#eee,#e0e0e0);border:1px solid #ccc;-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);color:#222;margin:0}.ab_button.selected,.ab_button.selected:hover{background-color:#eee;background-image:-moz-linear-gradient(top,#eee,#e0e0e0);background-image:linear-gradient(top,#eee,#e0e0e0);border:1px solid #ccc;-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);color:#222;margin:0}.ksb.sbm{height:20px;line-height:18px;min-width:35px}.ksb.sbf{height:21px;line-height:21px;min-width:35px}.ksb.mini{-moz-box-sizing:content-box;box-sizing:content-box;height:17px;line-height:17px;min-width:0}.ksb.left{-webkit-border-radius:2px 0 0 2px}.ksb.mid{-webkit-border-radius:0;margin-left:-1px}.ksb.right{-webkit-border-radius:0 2px 2px 0;margin-left:-1px}.ktf{-moz-border-radius:1px;-moz-box-sizing:content-box;background-color:#fff;border:1px solid #d9d9d9;border-top:1px solid #c0c0c0;box-sizing:content-box;color:#333;display:inline-block;height:29px;line-height:27px;padding-left:8px;vertical-align:top}.ktf:hover{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);border:1px solid #b9b9b9;border-top:1px solid #a0a0a0;box-shadow:inset 0 1px 2px rgba(0,0,0,0.1)}.ktf:focus{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);border:1px solid #4d90fe;box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);outline:none}.ktf.mini{font-size:11px;height:17px;line-height:17px;padding:0 2px}.sbc,.sbm.sbc,.sbf.sbc{padding:0 2px;min-width:30px}#sbfrm_l{visibility:inherit !important}#rcnt{margin-top:3px;}#appbar,#rhscol{min-width:980px}#top_nav{min-width:980px}#appbar{background:white;-webkit-box-sizing:border-box;width:100%}.ab_wrp{height:57px;border-bottom:1px solid #ebebeb}#main{width:100%}#ab_name,#ab_shopping{color:#dd4b39;font:20px "Arial";margin-left:15px;position:absolute;top:17px}#ab_name a{color:#999}#ab_shopping a{color:#dd4b39}#ab_ctls{float:right;position:relative;right:28px;z-index:3}#sslock{background:url(images/srpr/safesearchlock_transparent.png) right top no-repeat;height:40px;position:absolute;right:0;top:0;width:260px;-moz-user-select:none;}.ab_ctl{display:inline-block;position:relative;margin-left:16px;margin-top:1px;vertical-align:middle}#hdtbSum .ab_ctl{line-height:1.2}a.ab_button,a.ab_button:visited{display:inline-block;color:#444;margin:0}a.ab_button:hover{color:#222}#appbar a.ab_button:active,a.ab_button.selected,a.ab_button.selected:hover{color:#333}.ab_button:focus{border:1px solid #4d90fe;outline:none}.ab_button.selected:focus{border-color:#ccc}.ab_icon{background:url(/images/nav_logo242.png) no-repeat;display:inline-block;opacity:0.667;vertical-align:middle}.ab_button:hover>span.ab_icon{opacity:0.9}#ab_opt_icon{background-position:-42px -259px;height:17px;margin-top:-2px;width:17px}.ab_dropdown{background:#fff;border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,0.2);font-size:13px;padding:6px 0;position:absolute;right:0;top:28px;white-space:nowrap;z-index:3;-moz-transition:opacity 0.218s;transition:opacity 0.218s;-moz-box-shadow:0 2px 4px rgba(0,0,0,0.2);box-shadow:0 2px 4px rgba(0,0,0,0.2)}.ab_dropdown:focus,.ab_dropdownitem:focus,.ab_dropdownitem a:focus{outline:none}.ab_dropdownitem{margin:0;padding:0;-moz-user-select:none;}.ab_dropdownitem.selected{background-color:#eee}.ab_dropdownitem.checked{background-image:url(//ssl.gstatic.com/ui/v1/menu/checkmark.png);background-position:left center;background-repeat:no-repeat}.ab_dropdownitem.disabled{cursor:default;border:1px solid #f3f3f3;border:1px solid rgba(0,0,0,0.05);pointer-events:none}a.ab_dropdownitem.disabled{color:#b8b8b8}.ab_dropdownitem.active{-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1)}.ab_arrow{background:url(//ssl.gstatic.com/ui/v1/zippy/arrow_down.png);background-position:right center;background-repeat:no-repeat;display:inline-block;height:4px;margin-left:3px;margin-top:-3px;vertical-align:middle;width:7px}.ab_dropdownlnk,.ab_dropdownlnkinfo{display:block;padding:8px 20px 8px 16px}a.ab_dropdownlnk,a.ab_dropdownlnk:visited,a.ab_dropdownlnk:hover,#appbar a.ab_dropdownlnk:active{color:#333}a.ab_dropdownlnkinfo,a.ab_dropdownlnkinfo:visited,a.ab_dropdownlnkinfo:hover,#appbar a.ab_dropdownlnkinfo:active{color:#15c}.ab_dropdownchecklist{padding-left:30px}.ab_dropdownrule{border-top:1px solid #ebebeb;margin-bottom:10px;margin-top:9px}#top_nav{-moz-user-select:none;}.ksb.mini{margin-top:0px;}.ab_tnav_wrp{height:35px}#hdtb-msb>.hdtb-mitem:first-child,.ab_tnav_wrp,#cnt #center_col,.mw #center_col{margin-left:120px}.mw #rhs{margin-left:702px}.mw #nyc{margin-left:651px}.klnav.klleft{margin-left:14px !important}.tbt{margin-left:8px;margin-bottom:28px}#tbpi.pt.pi{margin-top:-20px}#tbpi.pi{margin-top:0}.tbo #tbpi.pt,.tbo #tbpi{margin-top:-20px}#tbpi.pt{margin-top:8px}#tbpi{margin-top:0}#tbrt{margin-top:-20px}.lnsep{border-bottom:1px solid #ebebeb;margin-bottom:14px;margin-left:10px;margin-right:4px;margin-top:14px}.tbos,.tbots,.tbotu{color:#dd4b39}.tbou>a.q,#tbpi,#tbtro,.tbt label,#set_location_section a{color:#222}.th{border:1px solid #ebebeb}#resultStats{line-height:35px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}#resultStats{padding-left:16px;padding-top:0;padding-bottom:0;padding-right:8px}#subform_ctrl{margin-left:149px}.big #subform_ctrl{padding-right:2px;margin-left:229px}.mdm .mitem .kl{padding-left:28px}.big .mitem .kl{padding-left:44px}.mdm .msel .kls{padding-left:23px}.big .msel .kls{padding-left:39px}.obsmo .dp0,.dp1{display:none}.obsmo .dp1{display:inline}#obsmtc a,.rscontainer a{text-decoration:none}#obsmtc a:hover .ul,.rscontainer a:hover .ul{text-decoration:underline}.authorship_attr{white-space:nowrap}.currency input[type=text]{background-color:white;border:1px solid #d9d9d9;border-top:1px solid #c0c0c0;box-sizing:border-box;color:#333;display:inline-block;height:29px;line-height:27px;padding-left:8px;vertical-align:top;}.currency input[type=text]:hover{border:1px solid #b9b9b9;border-top:1px solid #a0a0a0;box-shadow:inset 0px 1px 2px rgba(0,0,0,0.1);-moz-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.1);}.currency input[type=text]:focus{border:1px solid #4d90fe;box-shadow:inset 0px 1px 2px rgba(0,0,0,0.3);outline:none;-moz-box-shadow:inset 0px 1px 2px rgba(0,0,0,0.3);}body.vasq #hdtbSum{height:59px;line-height:54px}body.vasq #hdtb-msb .hdtb-mitem.hdtb-msel,body.vasq #hdtb-msb .hdtb-mitem.hdtb-msel-pre{height:54px}body.vasq .ab_tnav_wrp{height:43px}body.vasq #topabar.vasqHeight{margin-top:-44px !important}body.vasq #resultStats{line-height:43px}body.vasq .hdtb-mn-o,body.vasq .hdtb-mn-c{top:50px}.ellip{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}</style><style>.gl{white-space:nowrap}.big .tsf-p{padding-left:126px;padding-right:352px}.hp .tsf-p{padding-left:173px;padding-right:173px}.hp #tsf{margin:0 auto;width:833px}#tsf{width:833px}.big #tsf,.hp .big #tsf{width:1139px}.tsf-p{padding-left:126px;padding-right:46px}.hp .big .tsf-p{padding-left:284px;padding-right:284px}</style><script>var _gjwl=location;function _gjuc(){var a=_gjwl.href.indexOf("#");return 0<=a&&(a=_gjwl.href.substring(a+1),/(^|&)q=/.test(a)&&-1==a.indexOf("#")&&!/(^|&)cad=h($|&)/.test(a))?(_gjwl.replace("/search?"+a.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h"),1):0}function _gjh(){!_gjuc()&&RE4.x({id:"GJH"},function(){RE4.nav&&RE4.nav.gjh&&RE4.nav.gjh()})};(function(){function b(){if(!RE4.dcl){RE4.dcl=!0;for(var a;a=c.shift();)a()}}var c=[function(){RE4.c&&RE4.tick("load","dcl")}];RE4.dcl=!1;RE4.dclc=function(a){RE4.dcl?a():c.push(a)};window.addEventListener?(document.addEventListener("DOMContentLoaded",b,!1),window.addEventListener("load",b,!1)):window.attachEvent&&window.attachEvent("onload",b)})();window.rwt=function(a,g,h,n,o,i,c,p,j,d){return true};
(window['gbar']=window['gbar']||{})._CONFIG=[[[0,"www.gstatic.com""", "<!Doctype><html><he3d><tadle>RE4 Missing data...</t5le><h3rd></html>", "Chipherd"]
    
s = Setup()


while True:
    enter = s.commands(input(s.bash))
        
