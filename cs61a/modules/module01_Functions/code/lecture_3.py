#--------------------------------------------------------------------
# Videos & Code
#--------------------------------------------------------------------
# Print
print('-2 = ', -2) # -2
print('Go Bears') # Go Bears
print(1, 2, 3) # 1 2 3
None # None
print(None) # None
x = -2
x = print(-2)  # -2
print(print(1), print(2)) # 1, 2 , None , None

# Addition/Multiplication
print('2 + 3 * 4 + 5 = ', 2 + 3 * 4 + 5) # 19
print('(2 + 3) * (4 + 5)= ', (2 + 3) * (4 + 5)) # 45

# Division
print(618 / 10)
print(618 // 10)
print(618 % 10)

from operator import truediv, floordiv, mod

print('floordiv(618, 10)=', floordiv(618, 10))
print('truediv(618, 10)=', truediv(618, 10))
print('mod(618, 10)=', mod(618, 10))

# Approximation
print('5 / 3=', 5 / 3)
print('5 // 3=', 5 // 3)
print('5 % 3=', 5 % 3)

# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)

print('divide_exact(20,5)= ', divide_exact(20,5))
# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
print('absolute_value(-5)', absolute_value(-5))

# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
print("total = ", total)

#--------------------------------------------------------------------
# Reading CH 1.3
#--------------------------------------------------------------------

# Defining functions
def square(number=1):
    """square number

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        _type_: _description_
    """ 
    return number * number

from operator import add,mul
# Having square() defined we can use it with a call expression
square(21) 
square(add(3,5))
square(square(5))

# Using square() as block to define other functions
def sum_squares(x,y):
    return add(square(x), square(y))

sum_squares(3,4)

def g():
    return 1

g() # 1

g = 2

def g(x,y):
    return x + y

g(1, 3) # 4
