import turtle
import random

#setup
#screen
sc = turtle.Screen()
hero = turtle.Turtle()
enemy = turtle.Turtle()
coin = turtle.Turtle()
speed=0
rot=0

sc.tracer(0)

def w():
    global speed
    speed = 0.15

def s():
    global speed
    speed = -0.15

def stop():
    global speed
    speed = 0

def a():
    global rot
    rot = .5

def d():
    global rot
    rot = -.5

def cease():
    global rot
    rot = 0

def screenWrap(turtle):
    if(turtle.xcor()>465):
        turtle.goto(-465,turtle.ycor())
    elif(turtle.xcor()<-465):
        turtle.goto(465,turtle.ycor())

sc.onkeypress(w,"w")
sc.onkeyrelease(stop, "w")
sc.onkeyrelease(stop, "s")
sc.onkeypress(s,"s")
sc.onkeypress(a,"a")
sc.onkeyrelease(cease, "a")
sc.onkeyrelease(cease, "d")
sc.onkeypress(d,"d")
sc.listen()

while True:
    sc.update()
    hero.fd(speed)
    hero.left(rot)
    screenWrap(hero)