from turtle import *
tracer(0)
k=20
for i in range(2):
    forward(5*k)
    left(90)
    back(13*k)
    left(90)
penup()
back(10*k)
right(90)
forward(9*k)
left(90)
pendown()
for n in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
penup()
for x in range(-10,30):
    for y in range(-15,5):
        setpos(x*k,y*k)
        dot(4,'black')
done()