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
penup()
goto(-300,-300)
setx(0)
sety(0)
max_r = 0
min_size = 10
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
	circle(r=size, x=x,y=y)
	x += size * 2
	if x > max_width:
		x = 0
		row_height = max_r * 2
		max_r = 0
		y += row_height
getscreen().getcanvas().postscript(file="circles.eps")
done()

    

