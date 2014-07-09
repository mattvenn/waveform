from turtle import *
from math import pi

speed(0)

def circle(x=0,y=0,r=10,segments=40):
    c = 2 * pi * r
    l = c / segments
    a = 360 / segments
    penup()
    goto(x-l/2,y-r)
    pendown()
    setheading(0)
    for s in range(segments):
        forward(l)
        left(a)

def cross():
    backward(10)
    forward(20)
    backward(10)
    left(90)
    backward(10)
    forward(20)

cross()
circle(r=100)
circle(r=100, x=100,y=0)
circle(r=100, x=200,y=0)
done()

    

