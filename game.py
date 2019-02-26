import turtle
#import pygame
import random

sc = turtle.Screen()
sc.listen()
hero = turtle.Turtle()
#enemy = turtle.Turtle()
sc.tracer(0)
w=False
a=False
s=False
d=False

def up():
  hero.write("line 16")


def getKeysDown(screen):
  sc.onkeypress(up,"w")
  #sc.onkey(down,"s")
  #sc.onkey(left,"a")
  #sc.onkey(right,"d")

def moveForward(dist):
  pass
while True:
  getKeysDown(sc)
  #print(w)