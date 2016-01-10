import turtle

input("Use 'w,a,s,d' to move, space to shoot, mouse click to teleport.(Enter for start) ")
#screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")
#player
pen = turtle.Turtle()
pen.pu()
pen.color("green")
pen.speed(0)
#defs
spd = 1
m = pen
def f():
    global spd
    spd += 1
    
def ri():
    pen.right(30)
    

def le():
    pen.left(30)

def slow():
    global spd
    spd -= 1

def shoot():
    global pen
    bull = turtle.Turtle()
    bull.shape("circle")
    bull.pu()
    bull.speed(100)
    bull.shapesize(0.5, 0.5, 0.5)
    bull.setposition(round(pen.xcor(), 1), round(pen.ycor(), 1))
    bull.left(pen.heading())
    bull.speed(2)
    bull.forward(200)
    bull.ht()
    print(bull.shapesize())

turtle.onkeypress(f, "w")
turtle.onkeypress(ri, "d")
turtle.onkeypress(le, "a")
turtle.onkeypress(slow, "s")
turtle.onkeypress(shoot, "space")
screen.onclick(pen.goto)
wasd = screen.textinput("Name", "Name: ")
turtle.listen()
# main part
while True:
    pen.forward(spd)
