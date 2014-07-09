from turtle import *
from math import pi

speed(0)

def circle(x=0,y=0,r=10,segments=30):
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

fh = open('results.csv')
lines = fh.readlines()

max_width = 300
row_height = 100
x = 0
y = 0
laser_spacing = 5
max_r = 0
min_size = 15
last_size = 0
thread_r = 2
for line in lines:
    num, size = line.split(',')
    num = int(num)
    size = int(size)
    size += min_size
    size = size * 0.5
    if size > row_height:
        print("circle too big, limiting")
        size = row_height
    if size > max_r:
        max_r = size
    print("drawing circle %d, size %d" % (num,size))
    x = x + size + last_size + laser_spacing
    #for the outer circle
    circle(r=size, x=x,y=y)
    #for the thread hole
    circle(r=thread_r, x=x,y=y)
    last_size = size
    if x > max_width:
        x = 0
        row_height = max_r * 2
        max_r = 0
        y += row_height + laser_spacing
getscreen().getcanvas().postscript(file="circles.eps")
done()

    

