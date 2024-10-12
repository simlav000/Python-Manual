################################
# INDEXING AND SLICING STRINGS #
################################

# They say there are three genuienly hard problems in programming:
# 1) Naming variables and functions so that they are understandable.
# 2) Off-by-one errors.

# Recall that a string is a sequence of characters.
# Each character, therefore, has a postition or an INDEX
# Indices starts at zero. For example, for the string "Hello":

# H | e | l | l | o
# ------------------
# 0 | 1 | 2 | 3 | 4

# Indices must be integers, not floats.
# Python also allows negative indices, going from right to left:

#  H  |  e  |  l  |  l  |  o
# ----------------------------
# -5  | -4  | -3  | -2  | -1

# For any string "s"
# Valid positive index values are from 0 to len(s)-1
# Valid negative index values are from -len(s) to -1
# Square brackets [] are used to get letter in a string at a given index

message = "Hello"
print(message[0]) #H
# Read this as: "message at the index zero is 'H'"
print(message[1]) #e
print(message[2]) #l
print(message[3]) #l
print(message[4]) #o

#######################
# TRAVERSING A STRING #
#######################

# We can use for loops with range() functions to go over a string letter by
# letter

message = "deez nuts haha gottem"
for i in range(len(message)):
    print(message[i])


# We can also make use of something called the ENHANCED FOR-LOOP.
# This is a spin on the above for loop that only works on ITERABLE objects. 
# We'll explore what this means and where to find other iterable objects later,
# but for now, know that strings are iterable. This means we can do something 
# like:
letters = "bcmrst"
for character in letters:
    print(character + "ake")

# What's happening here is that, thanks to the way python strings (and other 
# iterable objects) are implemented, the for-loop pattern:
# "for component in iterable" just loops over all components. For strings, the
# components are the individual characters. The for loop also knows to stop when
# there are no characters left.

#################################
# USING SLICE TO GET SUBSTRINGS #
#################################
# Things that can be iterated over (iterables) can also often be sliced.
# Using slice notation we can get parts of a string.

# The syntax for this is
"""
string[start:end:step]
"""
# start, end, and step must all be integers.
# This notation works exactly the same as the range() function.
# This means your slice starts at "start", but ends at "end minus one".

fruit = "pineapple"
print(fruit[4:7]) # app

# Slice the string starting at index 4 (which is the fifth letter: "a") up to
# (but excluding) index 7 (8th letter) We can see now why range(), by default,
# starts at 0. All indices in Python, and many other languages, start at 0.
# This is confusing and frustrating at first, but eventually you'll get the
# hang of it.

# This is how we invert a string!
print(fruit[::-1]) # elppaenip

# This works by putting nothing in the "start" and "stop" fields. This
# generally means we keep the start and stop as default, taking the entire
# string, but our "step" is -1, mimicking the "countdown" example from the
# previous lecture when calling range(start, stop, -1)

# CHALLENGE
alphabet = "abcdefghijklmnopqrstuvwxyz"
# 1. Slice "alphabet" to print every other letter starting at "a"
# I.E: "acegikmoqsuwy"
# (Basically skipping every second letter of the english alphabet).

# 2. Now every other letter but starting at "b"
# I.E: "bdfhjlnprtvxz"
