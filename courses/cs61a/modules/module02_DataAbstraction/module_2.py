# native data type literals
print(type(2)) # < class 'int'>

# numeric types:
# integers(int)
# real numbers(float)
# complex numbers(complex)

print(type(1.5)) # <class 'float'>

print(type(1 + 1j)) #<class 'complex'>

# Non-numeric types. Values can represent many other types
# of data, such as sounds, images, locations, 
# web addresses, network connections, and more. 

# Sequences Ordered collection of values.
# Length - sequence of finite length 
# Start at index 0.

# Lists
# Tons of behaviors / arbitrary length

digits = [1, 8 , 2, 8]
len(digits) # 4
print(digits[3]) # 8

digits_op = [2,7] + digits * 2
print(digits_op) # 2,7, 1,8,2,8,1,8,2,8

# list of lists
pair =[[10,20], [30,40]]
print(pair[0]) # 10, 20
print()