import turtle
import random

#setup
#screen
sc = turtle.Screen()
#hero
hero = turtle.Turtle()
hero.pu()
hero.shape("turtle")
hero.goto(-random.randint(200,400),-random.randint(200,400))
#enemy
enemy = turtle.Turtle()
enemy.shape("triangle")
enemy.pu()
#coin
coin = turtle.Turtle()
coin.shape("circle")
coin.pu()
coin.goto(random.randint(-300,300),random.randint(-300,300))
#random vars
speed=0
rot=0

sc.tracer(0)

def w():
    global speed
    speed = 1

def s():
    global speed
    speed = 1

def stop():
    global speed
    speed = 0

def a():
    global rot
    rot = 1

def d():
    global rot
    rot = -1

def cease():
    global rot
    rot = 0

def move(turtle, speed, rot):
    turtle.fd(speed)
    turtle.left(rot)
    

def screenWrap(turtle):
    if(turtle.xcor()>465):
        turtle.goto(-465,turtle.ycor())
    elif(turtle.xcor()<-465):
        turtle.goto(465,turtle.ycor())
    if(turtle.ycor()>500):
        turtle.goto(turtle.xcor(),-390)
    elif(turtle.ycor()<-390):
        turtle.goto(turtle.xcor(),390)

def chase(target, this):
    this.setheading(this.towards(target))
    this.forward(0.15)

def caught(target, this):
    if(target.distance(this) < 20):
        return True
    return False
def loss():
    sc.bgcolor("red")

def win():
    sc.bgcolor("green")

sc.onkeypress(w,"w")
sc.onkeyrelease(stop, "w")
sc.onkeyrelease(stop, "s")
sc.onkeypress(s,"s")
sc.onkeypress(a,"a")
sc.onkeyrelease(cease, "a")
sc.onkeyrelease(cease, "d")
sc.onkeypress(d,"d")
#
sc.onkeypress(w,"Up")
sc.onkeyrelease(stop, "Up")
sc.onkeyrelease(stop, "Down")
sc.onkeypress(s,"Down")
sc.onkeypress(a,"Left")
sc.onkeyrelease(cease, "Left")
sc.onkeyrelease(cease, "Right")
sc.onkeypress(d,"Right")
sc.listen()

while ((not caught(hero,enemy))and(not caught(coin,hero))):
    sc.update()
    move(hero, speed/5, rot/2)
    chase(hero, enemy)
    if(caught(hero,enemy)):
        loss()
    if(caught(coin,hero)):
        win()
    screenWrap(hero)