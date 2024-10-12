###############
# ASCII CODES #
###############

# ASCII codes are a specific number associated with each unique character.
# These codes are not exclusive to Python, and are actually more of a standard
# that many languages and systems adhere to. You can search up an ASCII table
# online to get any specific code you need. Python has built-in functions to
# convert ASCII code (decimal) to/from a single character.

# To convert a character to a code, we use the ord() function.

print(ord("a")) #97, the ASCII code for the letter "a"
# The letter "b" is 98, "c" is 99, and so on.

print(ord("A")) #65
# Capital letters come before actually. "B" is 66, "C" is 67 and so on. "Z" is
# 96 and as we've seen, "a" 97.

print(ord("$")) #36
# Other characters have their own codes.
# This only works for strings of one character

# To go the other way around, we use the chr() function.

print(chr(70)) # F, the character for ASCII code 70

# EXAMPLE
# Write a program that shifts each letter in a string to the left by 3 steps
# according to ASCII table
def ASCII_shifter(s):
    result = ""
    for i in range(0, len(s)):
        code = ord(s[i])
        code = code - 3
        result = result + chr(code)
    return result
print(ASCII_shifter("Python"))

# You can think of the above function as a little cypher you can use to mask
# text. All you have to do is write a function that shifts the characters back
# three spots and voila! A decrypted message. I leave that to you :P 

#####################
# ESCAPE CHARACTERS #
#####################

# There are special characters that we sometimes deal with.
    # \n: The newline character: Printed when we press the "enter" key.
    # \t: The tab character: Printed when we press the "tab" key.
# Such special characters can be used in Python using escape characters. To
# include a newline character in a string we can use the escape character "\n"
# in the string:
message = "hello\nworld"
print(message)

# \n is stored as a single character even though it looks like two
print(ord("\n")) #10

# Another escape character is \t which represents the tab character.
# It is useful as a separator when displaying values:
# print uses space as separator by default
print("Joe", 85)
print("Mama", 90)

# Escaping is more general that just these two characters. Escaping is actually 
# the practice of placing a backslash (\) in front of a character so that it 
# does not get interpreted in any special way. Consider an example from a 
# previous lecture:

kind_message = 'Im going to "assisinate" the "president" of the United States'
# I was not able to place an apostrophe in "I'm" because the single-quote 
# character (') is ascribed the special meaning of containing the string. 
# We can use the escape character (\) to tell python not to interpret the 
# single-quote as a special character and treat it as a normal character, 
# allowing the single-quote to "escape" from its duties.
kind_message = 'I\'m going to "assisinate" the "president" of the United States'
print(kind_message)
# Now, the kind message is also properly punctuated.

##############################
# KEYWORD ARGUMENTS (KWARGS) #
##############################

# Functions in Python can have what we call "Keyword arguments". They are
# like normal arguments we give to functions, but they already have a special
# name associated with them. This means we need to know their names to use them
# in the first place, meaning we must RTFM (read the fucking manual). The 
# familiar print() function has a special keyword argument called "sep", and it
# specifies the separation between things it is printing. Using "\t" as
# separator:

print("Joe", 85, sep="\t")
print("Mama", 90, sep="\t")

# Keyword arguments must always come after the regular arguments (which we call
# positional arguments). For the print() function, it's a little meaningless to
# call them positional arguments since we're allowed to give it as many things
# to print as we want, so potition doesn't matter. For the insert(index, item)
# function we saw earlier though, the arguments are definitely positional.
# Regardless, all keyword arguments go last, but due to their name being
# specified, their order doesn't matter!

# We'll come back to functions at a later time and explain how we can make our
# own function have these special keyword arguments.

####################################
# CONTROLLING THE print() FUNCTION #
####################################

# Separator can be any string
print("Alice", 90, 3.14, sep=", ")
# Alice, 90, 3.14

print("Alice", 90, 3.14, sep="|")
# Alice|90|3.14

# Can be longer than a single character
print("Joe Mama", "Gottem", sep=" OOOOOOOOOOOOOOOO ")

# By default, print() function displays the newline character \n at end of line.
print("Zooie") # \n is displayed after e
print() # no arguments, just prints \n

# We can change the end character using another keyword argument to print()
# function end=
print("A sequence of numbers:")
print(1, end=",")
print(4, end=",")
print(9, end=",")

# Notice how these get printed on the same line.

print() # We do this to skip a line (basically prints a single newline "\n")

# This is useful in a loop
N = 10
for i in range(N-1):
    print(i*i, end=", ") # add  a comma and a space
print((N-1)*(N-1), end="")
print()

# This is what I was talking about with the order of keyword arguments not
# mattering. For the print function, you can write "sep=" or "end=" in any
# order, so long as they both come after the positional arguments

# MULTILINE STRINGS
# using \n, we can create a single string containing multiple lines:

shopping_list = "Shopping list\n- Milk\n- Eggs\n- Vegemite"
print(shopping_list)

# Python provides a better way to create multiline strings using triple quotes
# ''' or """

shopping_list = '''Shopping list
- Vegemite
- Vegemite
- Vegemite
- Vegemite
- Vegemite
- Vegemite
- Vegemite
- Vegemite
- Vegemite
'''
print(shopping_list)
