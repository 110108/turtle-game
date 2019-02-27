import turtle
#import pygame
import random

sc = turtle.Screen()
sc.listen()
hero = turtle.Turtle()
#enemy = turtle.Turtle()
#sc.tracer(0)
w=False
a=False
s=False
d=False

def isKeyDown(key):
    #

def w():
    while True:
        hero.fd(2)

def s():
    hero.fd(-2)
def a():
    hero.write("line 20")
def d():
    hero.write("line 22")

sc.onkeypress(w,"w")
sc.onkeypress(s,"s")
sc.onkeypress(a,"a")
sc.onkeypress(d,"d")
sc.listen()