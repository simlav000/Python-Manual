def is_even(x):
    return (x % 2) == 0

# CHALLENGE 1. Write a function that takes 3 integers x,y,z as inputs and
# prints out True if y is an even number between x and z. False otherwise.
# Assume all 3 numbers are different. You can use "is_even()" from above simply
# by calling it!

def challenge(x, y, z):
    return x < y and y < z and is_even(y)

# Testing to see if this is legit:
print(challenge(1,2,3)) # True (Good)
print(challenge(3,2,3)) # False (Good)
print(challenge(1,2,1)) # False (Good)

# Obviously, this is not the only valid solution. So long as you obtain the
# same results as me with these test cases, you're probably good!

# 2. Make the truth table for "P and Q"
# #-----------------#
# | P | Q | P and Q |
# | T | T |    T    |
# | T | F |    F    |
# | F | T |    F    |
# | F | F |    F    |
# #-----------------#
# Again, an "and" statement is only true if both expressions are True.
# Everything else is False.
