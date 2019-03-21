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
w0.pu()
w0.ht()
w0.goto(-475,385)
w1=turtle.Turtle()
w1.pu()
w1.ht()
w1.goto(375,385)
#enemies
enemy = turtle.Turtle()
enemy.shape("triangle")
enemy.pu()
enemy0 = turtle.Turtle()
enemy0.shape("triangle")
enemy0.pu()
#coin
coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.pu()
coin.goto(random.randint(-300,300),random.randint(-300,300))
#random vars
p1score=0
p2score=0
heroSpeed=0
heroRot=0
villanSpeed=0
villanRot=0


#over on line 92
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

def writeScore():
    w0.clear()
    w1.clear()

    if(p1score>=3):
        w0.write("Player One Wins!")
        w1.write("Player One Wins!")
    elif(p2score>=3):
        w0.write("Player Two Wins!")
        w1.write("Player Two Wins!")
    else:
        w0.write("Player one Score: "+str(p1score))
        w1.write("Player two Score: "+str(p2score))

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

def restart():
    coin.goto(random.randint(-300,300),random.randint(-300,300))
    villan.goto(random.randint(200,400),random.randint(200,400))
    hero.goto(-random.randint(200,400),-random.randint(200,400))
    enemy.goto(0,0)
    enemy0.goto(0,0)

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

while (p1score<3 and p2score<3):
    sc.update()
    writeScore()
    move(hero, heroSpeed/10, heroRot/2)
    move(villan, villanSpeed/10, villanRot/2)
    chase(hero, enemy, .05)
    chase(villan, enemy0, .05)
    if(caught(hero,enemy)):
        loss()
    if(caught(coin,hero)):
        win()
        p1score+=1
        restart()
    if(caught(coin,villan)):
        p2score+=1
        sc.bgcolor("purple")
        restart()
    screenWrap(hero)
    screenWrap(villan)
writeScore()