""" Lecture 1. Functions """
# Numeric Expressions
from operator import add, mul
print(2020)
print(2020 + 20)
print("-1 + 2 + 3 + 4 * (5 // 6) + 7 * 8 * 9 =", -
      1 + 2 + 3 + 4 * (5 // 6) + 7 * 8 * 9)

# Call Expressions
print("max(3, 4.5)= ", max(3, 4.5))  # 4.5
print("pow(100, 2)= ", pow(100, 2))
print("pow(2, 100)= ", pow(2, 100))

# Importing & Arithmetic Call Expressions
print("add(1, 2)= ", add(1, 2))
print("add(4, 6)= ", add(4, 6))
print("mul(add(2,3), mul(22,3))= ", mul(add(2, 3), mul(22, 3)))

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt

shakespear_url = open("/workspaces/working/cs61a/weeks/week01/shakespear.txt")
total_text = shakespear_url.read().split()
# print(total_text)
print("File Length= ", len(total_text))
print("First 25 words = ", total_text[:25])


print("The: ", total_text.count('the'))
print("thou: ", total_text.count('thou'))
print("you: ", total_text.count('you'))
print(", : ", total_text.count(','))

# Sets (A datatype that store unique values)
words = set(total_text)  # from 980637
print("len of set = ", len(words))  # to 33505
print("print the word with the max length = ", max(words))
print(max(words, key=len))

# Reversals
print('draw'[::-1])

for w in words:
    if w == w[::-1] and len(w) < 4:
        print("Result < 4", w)

for w in words:
    if w == w[::-1] and len(w) == 4:
        print("Result == 4", w)

for w in words:
    if w == w[::-1] and len(w) > 6:
        print("Result > 6", w)
