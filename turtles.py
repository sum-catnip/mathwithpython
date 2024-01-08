from turtle import *
from typing import List

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

# convex
def polygon(sides: int, side: int):
    for _ in range(sides):
        fd(side)
        right(360 / sides)

def squiral(increment: int):
    for i in range(60):
        square(increment * (i +1))
        right(5)

def starral(increment: int):
    for i in range(60):
        star(increment * (i +1))
        right(5)

def star(side: int):
    for _ in range(5):
        fd(side)
        # interior angle
        # 180 / 5 = 36
        # exterior angle
        # 180 - 36 = 144
        right(144)

def seqsum(n: int) -> int:
    return sum(range(n+1))

def factors(n: int) -> List[int]:
    return [i for i in range(1, n+1) if not n % i]

def gcf(a: int, b: int) -> int:
    return max(set(factors(a)).intersection(factors(b)))

shape('turtle')
#square(100)
#squircle(100)
#triangle(100)
#polygon(5, 100)
#squiral(5)
#star(100)
#starral(5)
#print(seqsum(100))
print(factors(120))
print(gcf(150, 138))
#done()
