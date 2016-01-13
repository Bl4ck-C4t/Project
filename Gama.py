class Setup:
    
    def __init__(self):
        self.bash = "root#> "
        print("Enter username: ")
        ent = input(self.bash)
        self.bash = ent + "#> "
        print("Use 'help' to see commands")
        self.cl = ["ls", "run", "mail", "web", "new", "help"]
        self.harddrive = ["explorer.exe", "File.txt"]
        self.txt = ["Something..."]
        self.messages = {"New1":"Hello"}
        
    def ls(self):
        for x in enumerate(self.harddrive, start=1):
            print(str(x[0]) + ". " + x[1])

    def error(self):
        print("Unrecognized/Unknown command. Type 'help' for syntax")
        
    def commands(self, ent):
        if self.cl[0] == ent:
            self.ls()

        elif self.cl[4] == ent:
            self.new()

        elif self.cl[1] == ent[:3]:
            self.run(ent[4:])

        elif self.cl[5] == ent:
            self.help()

        elif self.cl[2] == ent[:4]:
            self.mail(ent[5:])
        
        else:
            self.error()
            
    def new(self):
        print("Enter file name: ")
        ent = input(s.bash)
        self.harddrive.append(ent + ".txt")
        print("Enter text: ")
        ent = input(s.bash)
        self.txt.append(ent)
        print("Text written.")

    def run(self, pr):
        if len(pr) < 3:
            print("Wrong syntax: run [program.extension]")
        elif pr[len(pr) - 1: len(pr) - 4: -1] == "txt":
            c = 0
            for x in self.harddrive:
                if x == pr:
                    break
                if x[len(x) - 1: len(x) - 4: -1] == "txt":
                    c += 1
            print("Data of file " + pr)
            print(self.txt[c])

    def help(self):
        print("ls - list programs, new - make a txt file, run - runs a program, mail - check mail.")

    def mail(self, email):
        if email == '':
            for x in enumerate(self.messages, start=1):
                print(str(x[0]) + ". " + x[1])
            enter = input("Type a message to view('e' to exit) ")
            while enter != "e":
                for x in enumerate(self.messages, start=1):
                    if x[0] == int(enter):
                        print("Message: " + self.messages[x[1]])
                        break
                for x in enumerate(self.messages, start=1):
                    print(str(x[0]) + ". " + x[1])
                enter = input("Type a message to view('e' to exit) ")
        else:
            print("Message " + email + ": " + self.messages[email] )
        
        
s = Setup()
while True:
    enter = s.commands(input(s.bash))
    
