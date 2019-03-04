import turtle
import random

#setup
#screen
sc = turtle.Screen()
sc.tracer(0)
#hero
hero = turtle.Turtle()
hero.pu()
hero.shape("turtle")
hero.goto(-random.randint(200,400),-random.randint(200,400))
#villan (p2)
villan = turtle.Turtle()
villan.pu()
villan.shape("turtle")
villan.goto(random.randint(200,400),random.randint(200,400))
#writers
w0=turtle.Turtle()
w0.ht()
#w0.
w1=turtle.Turtle()
#enemy
enemy = turtle.Turtle()
enemy.shape("triangle")
enemy.pu()
#coin
coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.pu()
coin.goto(random.randint(-300,300),random.randint(-300,300))
#random vars
heroSpeed=0
heroRot=0
villanSpeed=0
villanRot=0


def w():
    global heroSpeed
    heroSpeed = 1

def s():
    global heroSpeed
    heroSpeed = 1

def stop():
    global heroSpeed
    heroSpeed = 0

def a():
    global heroRot
    heroRot = 1

def d():
    global heroRot
    heroRot = -1

def cease():
    global heroRot
    heroRot = 0

def up():
    global villanSpeed
    villanSpeed = 1

def down():
    global villanSpeed
    villanSpeed = 1

def stopv():
    global villanSpeed
    villanSpeed = 0

def left():
    global villanRot
    villanRot = 1

def right():
    global villanRot
    villanRot = -1

def ceasev():
    global villanRot
    villanRot = 0

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

def chase(target, this, speed):
    this.setheading(this.towards(target))
    this.forward(speed)

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
sc.onkeypress(up,"Up")
sc.onkeyrelease(stopv, "Up")
sc.onkeyrelease(stopv, "Down")
sc.onkeypress(down,"Down")
sc.onkeypress(left,"Left")
sc.onkeyrelease(ceasev, "Left")
sc.onkeyrelease(ceasev, "Right")
sc.onkeypress(right,"Right")
sc.listen()

while (((not caught(hero,enemy))and(not caught(coin,hero)))and((not caught(villan,enemy))and(not caught(coin,villan)))):
    sc.update()
    move(hero, heroSpeed/10, heroRot/2)
    move(villan, villanSpeed/10, villanRot/2)
    chase(hero, enemy, .05)
    if(caught(hero,enemy)):
        loss()
    if(caught(coin,hero)):
        win()
    if(caught(hero,villan)):
        sc.bgcolor("purple")
    screenWrap(hero)
    screenWrap(villan)