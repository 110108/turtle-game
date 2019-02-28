import turtle
import random

sc = turtle.Screen()
sc.listen()
hero = turtle.Turtle()
#enemy = turtle.Turtle()
#sc.tracer(0)
speed=0
#global rot=0

def w():
    global speed
    speed = 1

def s():
    global speed
    speed = -1

def stop():
    global speed
    speed = 0

def a():
    hero.write("line 20")

def d():
    hero.write("line 22")


sc.onkeypress(w,"w")
sc.onkeyrelease(stop, "w")
sc.onkeyrelease(stop, "s")
sc.onkeypress(s,"s")
sc.onkeypress(a,"a")
sc.onkeypress(d,"d")
sc.listen()

while True:
    hero.fd(speed)