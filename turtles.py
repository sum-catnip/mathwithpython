from turtle import *

def square(side: int):
    for _ in range(4):
        fd(side)
        right(90)


def squircle(rad: int):
    for _ in range(60):
        square(rad)
        right(5)

def triangle(side: int):
    for _ in range(3):
        fd(side)
        right(120)

def polygon(sides: int, side: int):
    for _ in range(sides):
        fd(side)
        right(360 / sides)

def squiral(increment: int):
    for i in range(60):
        square(increment * (i +1))
        right(5)

shape('turtle')
#square(100)
#squircle(100)
#triangle(100)
#polygon(5, 100)
squiral(5)
done()
