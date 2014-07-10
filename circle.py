from turtle import *
from math import pi

#as fast as we can
speed(0)

#here's our circle function
def circle(x=0,y=0,r=10,segments=30):
    #work out the amount to go fowards and the amount to turn
    c = 2 * pi * r
    l = c / segments
    a = 360 / segments

    #move to the bottom of the circle
    penup()
    goto(x-l/2,y-r)
    pendown()

    #draw the circle
    for s in range(segments):
        forward(l)
        left(a)

#hide the turtle so it doesn't get printed or laser cut
hideturtle()

#open the file and read each line into a list called lines
fh = open('results.csv')
lines = fh.readlines()

#some variables we'll need
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
    #split the csv into 2 parts
    num, size = line.split(',')
    #and turn them both from strings to ints
    num = int(num)
    size = int(size)
   
    #scale the size to something small enough to cut
    size = size * 0.01

    #if the size is too small, we still need a bead, so add a bit on
    size += min_size

    #stop any circle from being too big
    if size > row_height:
        print("circle too big, limiting")
        size = row_height
    #keep a track of the max size
    if size > max_r:
        max_r = size

    #draw the circle
    print("drawing circle %d, size %d" % (num,size))
    x = x + size + last_size + laser_spacing
    #for the outer circle
    circle(r=size, x=x,y=y)
    #for the thread hole
    circle(r=thread_r, x=x,y=y)
    last_size = size

    #this part is for the arrangement of the circles on the page
    if x > max_width:
        x = 0
        row_height = max_r * 2
        max_r = 0
        y += row_height + laser_spacing

#this line exports the canvas to an eps file we can laser cut
getscreen().getcanvas().postscript(file="circles.eps")
print("done")
done()
