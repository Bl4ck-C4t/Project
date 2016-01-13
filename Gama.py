class Setup:
    
    def __init__(self):
        self.bash = "root#> "
        print("Enter username: ")
        ent = input(self.bash)
        self.bash = ent + "#> "
        self.cl = ["ls", "run", "mail", "web", "new", "help"]
        self.harddrive = ["explorer.exe", "File.txt"]
        self.txt = ["Something..."]
        
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
            try:
                self.run(ent[4:])
            except IndexError:
                print("Wrong syntax: run [program.extension]")
                
		elif self.cl[5] == ent:
			self.help()
        
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
        if pr[len(pr) - 1: len(pr) - 4: -1] == "txt":
            c = 0
            for x in self.harddrive:
                if x == pr:
                    break
                if x[len(x) - 1: len(x) - 4: -1] == "txt":
                    c += 1
            print("Data of file " + pr)
            print(self.txt[c])
            
            
	def help(self):
		print("ls - shows files, new - creates files, run - runs flies")
        
s = Setup()
while True:
    enter = s.commands(input(s.bash))
