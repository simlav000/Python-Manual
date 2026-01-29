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
print(ASCII_shifter("Secret (Shh)"))

# You can think of the above function as a little cypher you can use to mask
# text. All you have to do is write a function that shifts the characters back
# three spots and voila! A decrypted message. I leave that to you.

#####################
# ESCAPE CHARACTERS #
#####################

# There are special characters that we sometimes deal with.
    # \n: The newline character: Printed when we press the "enter" key.
    # \t: The tab character: Printed when we press the "tab" key.
    # \r: Carriage return: If I ever use it I'll tell you what it does.

# Escaping is more general than just these two characters. As foreshadowed
# in chapter 10 (2 in binary), placing a backslash (\) in front of a character
# neutralizes its abilities.

# Consider the task of using apostrophes and quotes in a string.
# We need to pick one flavour of quote to surround the string ("") or ('').
# We can prevent a quotation mark in our string from terminating it early:
"This will supposedly \"prevent and error\" from occuring"

# We can also properly punctuate a phrase contained in single quotes
'Look mom I\'m not crashing!'
