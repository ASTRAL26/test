import turtle
import random
turtle.delay(0)
myturtle = turtle.Turtle()

def square():
    for i in range(0,4):
        myturtle.forward(100)
        myturtle.left(90)

def circle():
    for i in range(0,360):
        myturtle.forward(1)
        myturtle.left(1)

def snails():
    for i in range(0,10):
        myturtle.forward(80+i*10)
        myturtle.left(90)

def snailc(tour):
    for i in range(0,360*tour):
        myturtle.forward(1+i/750)
        myturtle.left(1)

def ex3():
        myturtle.left(random.randint(0,360))
        myturtle.forward(random.randint(100,500))

def toutdroit():
    while 1:
        myturtle.forward(1)

def rturn():
    while 1:
        myturtle.forward(5)
        myturtle.left(random.randint(0,4)*90)

def listortue(n):
    liste=[]
    for i in range(0,n):
        liste.append(turtle.Turtle())
    return liste

def rtortue(liste):
    for tortue in liste:
        tortue.pencolor(random.random(),random.random(),random.random())
        tortue.goto(random.randint(-300,300),random.randint(-300,300))

liste1=listortue(10)
n=3

def agariotortue(liste):
    for tortues in liste:
        tortues.penup()
        tortues.color(1,0,0)
        tortues.goto(random.randint(-300,300),random.randint(-300,300))
    while 1:
        myturtle.forward(10)
        myturtle.left(random.randint(0,4)*90)
        myturtle.color(0,1,0)
        myturtle.shapesize(n)

agariotortue(liste1)

input()