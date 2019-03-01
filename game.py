import turtle
import random

sc = turtle.Screen()
sc.listen()
hero = turtle.Turtle()
enemy = turtle.Turtle()
coin = turtle.Turtle()
#sc.tracer(0)
speed=0
rot=0

def w():
    global speed
    speed = 5

def s():
    global speed
    speed = -5

def stop():
    global speed
    speed = 0

def a():
    global rot
    rot = 5

def d():
    global rot
    rot = -5

def cease():
    global rot
    rot = 0


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
    hero.fd(speed)
    hero.left(rot)