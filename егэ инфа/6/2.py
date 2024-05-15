from turtle import *
tracer(0)
k=10
for me in range(2):
    forward(21*k)
    right(90)
    forward(27*k)
    right(90)
penup()
forward(9*k)
right(90)
forward(10*k)
left(90)
pendown()
for u in range(2):
    forward(86*k)
    right(90)
    forward(47*k)
    right(90)
penup()
for x in range(-10,30):
    for y in range(-30,5):
        setpos(x*k,y*k)
        dot(4,'black')
done()