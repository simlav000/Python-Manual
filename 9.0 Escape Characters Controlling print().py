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
