
<h1>Module 3. Defining Functions / Design Functions</h1>
<p>|__________________________________________|</p>

<h2>_WHAT'S THE MATTER IN THIS SECTION?_</h2>

[](http://www.composingprograms.com/pages/14-designing-functions.html)
http://www.composingprograms.com/pages/15-control.html

<p>|_____________________________________________________________________|</p>
<p>|____________________________________|</p>

<ul>
    <li><a href="#u1">1. Functions Definition</a></li>
    <li><a href="#u2">2. Rules for naming convention</a></li>
    <li><a href="#u3">3. Design Functions</a></li>
    <li><a href="#u4">4. Documentation</a></li>
    <li><a href="#u5">5. Default Argument Values </a></li>
    <li><a href="#u6">6. Difference between pure functions and non-pure functions</a></li>
    <li><a href="#u7">7. Compound Statements</a></li>
    <li><a href="#u8">8. Conditional Statements</a></li>
    <li><a href="#u9">9. Boolean Values</a></li>
    <li><a href="#u9">10. Boolean Operators</a></li>
    <li><a href="#u9">11. While Clouse</a></li>

</ul>


<h2 id="u1">1. Functions Definition</h2>

Function definitions consist of a **``def``** statement that indicates a **&lt;``name``&gt;** and a comma-separated list of named **&lt;``formal parameters``&gt;**, then a return statement, called the function body, that specifies the **&lt;``return`` expression&gt;** of the function, which is an expression to be evaluated whenever the function is applied:

<br>


```python
# Define statement
def <name>(<formal parameters>):
    return <return expression> 
    # Second line must be intended
```

---

```python
# Define square_x
def square_x(number):
    return number * number
```
---

```python
from operator import add,mul
# Having square() defined we can use it with a call expression
square_x(21)  # single value
square_x(add(3,5)) # call expression
square_x(square_x(5)) # call expression
```

---

```python
# Using square() as block to define other functions
def sum_squares(x,y):
    return add(square(x), square(y))

sum_squares(3,4)
```
---

```python
# Both <def> and assignt statement bind names to values, and any existing binding will be lost.

g():
    return 1

# g()
# 1

g = 2
# g
# 2

def g(h,i):
    return h + i

# g(1,3)
# 4 


```

---
<br>

<h2 id="u2">2. Rules for naming convention</h2>

1. **`Function` names** are **``lowercase``**, with words separated by underscores. Descriptive names are encouraged.

2. **Function names** typically evoke operations applied to arguments by the interpreter (e.g., ``print``, ``add``, ``square``) or the name of the quantity that results (e.g., ``max``, ``abs``, ``sum``).

3. **Parameter** names are **``lowercase``**, with words separated by underscores. **Single-word** names are preferred.

4. **Parameter** names should evoke the role of the parameter in the function, not just the kind of argument that is allowed.

5. **Single letter parameter** names are acceptable when their role is obvious, but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.


<h2 id="u3">3. Design Functions </h2>

Each function should have only one job.

Functions that have multiple jobs , should be devided in multiple functions.

Don't repeat yourself.

Functions should be defined generally. 
---

<br>


<h2 id="u4">4. Documentation </h2>

**Function** definition will often include `documentation`. 
 
`docstrings` are triple qouted
First line describe the job of the function.
 
Following lines can describe arguments and behavior;


```python
>>> def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas. # First Line

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```
---
Use `help` with the name of function to see it's `docstring`
```python
help(pressure)
```
---

<h2 id="u5">5. Default Argument Values </h2>

In Python, we can provide default values for the arguments of a function. When calling that function, arguments with default values are optional. If they are not provided, then the default value is bound to the formal parameter name instead.

```python
>>> def pressure(v, t, n=6.022e23):
        """Compute the pressure in pascals of an ideal gas.

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas (default: one mole)
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```

<h2 id="u6">6. Statements </h2>

Rather than being evaluated, `statements` are `executed`.

```python
# Consider this function
def square(x):
        mul(x, x) # Watch out! This call doesn't return a value.
```
The `body` of the function consists of an `expression`. An `expression` by itself is a valid statement, but the effect of the statement is that the mul function is called, and the `result is discarded`.
```python
def square(x):
        return mul(x, x)
```

<h2 id="u7">7. Compound Statements</h2>

<pre><code>
 A compound statement consists of one or more clauses:

&ltheader&gt:
    &ltstatement&gt
    &ltstatement&gt
    ...
&ltseparating header&gt:
    &ltstatement&gt
    &ltstatement&gt
    ...
...

Expressions, return statements, and assignment statements are simple statements.
A def statement is a compound statement. The suite that follows the def header defines the function body.
</code></pre>

<h2 id="u8">8. Conditional Statements</h2>

```python
# Conditional expressions

def absolute_value(x):
    """Return absolute value of X.
    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

    print('absolute_value(-5)', absolute_value(-5))
```
<pre>
A conditional statement in Python consists of a series of headers and suites: a required if clause, an optional sequence of elif clauses, and finally an optional else clause:

if &ltexpression>:
    <suite>
elif <expression>:
    <suite>
else:
    <suite>
</pre>

When executing a conditional statement, each clause is considered in order. The computational process of executing a conditional clause follows.

Evaluate the header's expression.
If it is a true value, execute the suite. Then, skip over all subsequent clauses in the conditional statement.
If the else clause is reached (which only happens if all if and elif expressions evaluate to false values), its suite is executed.

<h2 id="u9">9. Boolean Values</h2>

Python has two boolean values, called `True` and `False`. Boolean values represent truth values in logical expressions. The built-in comparison operations, `>,<, >=, <=, ==, !=, return these values.

4 < 2  
`False`
5 >= 5  
`True`

<h2 id="u10">10. Boolean Operators</h2>
Boolean operators. Three basic logical operators are also built into Python:

True and False
False
True or False
True
not False
True


<h2 id="u11">11. While clause</h2>

<pre>
A while clause contains a header expression followed by a suite:

while &ltexpression&gt:
    &ltsuite&gt
To execute a while clause:

Evaluate the header's expression.
If it is a true value, execute the suite, then return to step 1.
</pre>

```python
# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
print("total = ", total)
```
