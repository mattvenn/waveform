import turtle
from math import pi

# as fast as we can
turtle.speed(0)


# here's our circle function
def circle(x=0, y=0, r=10, segments=20):
    # work out the amount to go fowards and the amount to turn
    c = 2 * pi * r
    l = c / segments
    a = 360 / segments

    # move to the bottom of the circle
    turtle.penup()
    turtle.goto(x-l/2, y-r)
    turtle.pendown()

    # draw the circle
    for s in range(segments):
        turtle.forward(l)
        turtle.left(a)

# hide the turtle so it doesn't get printed or laser cut
turtle.hideturtle()

# open the file and read each line into a list called lines
fh = open('results.csv')
lines = fh.readlines()

# some settings:

min_width = -350 # start off on the left
max_width = 350 # how far we go before starting a new line
laser_spacing = 5  # space to leave between beads
min_size = 4  # smallest bead
max_size = 25  # largest bead
thread_r = 1  # hole for thread

# scaling is how we scale the numbers in the file to size of circles
# make this number bigger or smaller till all your beads fit on the screen
scaling = max_size / 10000.0

# some variables we'll need
last_size = 0
y = 0
x = min_width

for line in lines:
    # split the csv into 2 parts
    num, sample = line.split(',')
    # and turn them both from strings to ints
    num = int(num)
    sample = int(sample)

    # scale the size to something small enough to cut
    size = sample * scaling

    # if the size is too small, make sure it's big enough
    if size < min_size:
        size = min_size

    # stop any circle from being too big
    if size > max_size:
        print("circle too big, limiting")
        size = max_size

    # draw the circle
    print("drawing circle %d, sample = %d size = %d" % (num, sample, size))
    x = x + size + last_size + laser_spacing
    # for the outer circle
    circle(r=size, x=x, y=y)
    # for the thread hole
    circle(r=thread_r, x=x, y=y)
    last_size = size

    if x > max_width:
        x = min_width
        y += 2 * max_size + laser_spacing

# this line exports the canvas to an eps file we can laser cut
turtle.getscreen().getcanvas().postscript(file="circles.eps")
print("done")
turtle.done()
