import math
import turtle

bob = turtle.Turtle()
print(bob)
#Having bob put his pen down before execution
bob.pd()

def square(t, length):
#for loop to create an almost never ending square
    for i in range(4):
        t.fd(length)
        t.rt(90)

def circle(t, r):
    for i in range(4):
        circumference = 2 * math.pi * r 
        n = int(circumference / 3) + 1
        length = circumference / n
        turtle._PolygonCoords(t, n, length)

square(bob, 100)

turtle.mainloop()