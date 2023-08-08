"""
Lecture 2. Names
"""

f = min
f = max
g = min
h = max
max = g

print("max(f(2,g(h(1,5),3)), 4)= ", max(f(2,g(h(1,5),3)), 4))

# Imports
from math import pi
print(pi * 71 / 223)

from math import sin
print(sin) # built-in function sin
other_sin = sin  # redefine the names of functions, but they point to the exact same functions
print(other_sin) # built-in function sin

# Assignment
radius = 10
print("2 * rad = ", 2 * radius)

area_of = pi * radius
print("area = ", area_of)

circ = 2 * pi * radius
print("circ = ", circ)

radius = 20

# Function values
print(max) # built-in function min , look UP
print(max(2, 3)) # 2

f = max
print(f) # built-in function min
print(f(3,4)) # 3

max = 7 # going back to a numeric value 7
print(f(1, max)) # 7

f = 2 # going back to a numeric value 2
# print(f(3,4)) # f is not callable

print(__builtins__.max)

# User-defined functions
from operator import add, mul

def square(x):
    return mul(x, x)

print("square(5)= ", square(5))
print("(square(add(5,2))= ", square(add(5,2)))

def sum_squares(x, y):
    return add(square(x), square(y))

print("sum_squares(3, 4)= ",sum_squares(3, 4))
print("sum_squares(12, 3)= ",sum_squares(12, 3))


# area function
def area():
    return pi*radius*radius

area()
radius = 20
area()
radius = 20
area()




