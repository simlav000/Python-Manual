##################
# FUNCTION CALLS #
##################

# Functions take zero or more input values. They may return something. They may
# also have some "effect" on "objects".

# A function call looks like this:
# func_name(arg_1, arg_2, ..., arg_n)
# Recall: arguments are passed to functions.
# The number of arguments required by a function depends on its implementation.

# When it comes to built-in functions, it is often required to read
# documentation to know how a function is expected to be used. Here's a handy
# page which lists all the basic built-in Python functions:
# https://docs.python.org/3/library/functions.html
# We'll be listing a good few of them here. But first...

##############################
# KEYWORD ARGUMENTS (KWARGS) #
##############################

# Functions in Python can have what we call "Keyword arguments" (KWARGS). They
# are like normal arguments we give to functions, but they already have a 
# special name associated with them. This means we need to know their names to 
# use them in the first place, so we have to "read documentation". 

# The familiar print() function has a special keyword argument called "sep",
# which specifies the separation between things it is printing. 
print("time", "money", sep=" = ")

# Keyword arguments must always come after the regular arguments (which we call
# positional arguments). KWARGS are sometimes optional, in which case they are 
# designed to have an implicit default value. It is again up to you to read up
# on what these defaults are, but I'll show you a few of them.

# For print, the default separation is the empty string ("")
print("No", "space", sep="")
# You can make the separation any string you want.

# We can change the "end" character using another one of print()'s keyword
# arguments.
print("A sequence of numbers:")
print(1, end=", ")
print(4, end=", ")
print(9, end=", ")
# Notice how these get printed on the same line.
# We used to skip a line for every print statement. This was the "end"
# argument's default value's job. This default value is the special character
# "\n" (yes, both the slash and the n are grouped into a single character).
# This is called the "newline character" and it's a special one. "\n" gets 
# interpreted as a signal which forces a line break.

# These do the same thing (print an empty line)
print(end="\n")
print()

##################################
# OTHER PYTHON LIBRARY FUNCTIONS #
##################################

###########
# input() #
###########
# We use the input() function to ask for input data from the keyboard.

# input(prompt):
# prompt is a string. 
# Displays the prompt string and waits for the user to enter one
# line of input text in the terminal. The remaining code will not run until
# this input is entered. The function returns the text entered by user as a
# string, which can be stored in a variable.

number = input("Entrust me with you credit card number: ")
# Notice how input returns something, and we can catch it with the number
# variable.

# We have to be careful not to run away with this number as it isn't a true
# number just yet. It's a string. Users can only ever give us strings. It is
# our responsibility to interpret this is a number.

try:
    number = int(number)
except Exception as thats_not_a_number:
    print("Hey! Why don't you trust me???")

# As you can tell it takes quite some machinery to make taking input not crash
# our program.

print(f"Current Bank Balance: {number * -4}.00 $")

##########################
# MATHEMATICAL FUNCTIONS #
##########################

# min() function takes 2 or more numbers and returns the minimum
x = min(1, -4, 6)
print(x) # -4

# abs() function takes one number and returns the absolute value of the number
y = abs(-6)
print(y) # 6

# round() function rounds a float.
price = 101.61283
print(round(price))
# The round function takes in a second input for the rounding precision,
# in other words, how many numbers to keep in the final answer.
print(round(price, 3))

########################
# CONVERSION FUNCTIONS #
########################

# Convert to integer using int() 
# Convert a float to an integer. This has the side-effect of truncating the
# fractional part of a floating point number
price = 101.3213
print(int(price))
# You can also convert the string '1' to the integer 1, but trying it on the
# float '1.0' will throw an error.

# Convert to float using float()
# (e.g. to show zero cents)
price = 100
print(float(price))
# You can also convert both '1' AND '1.0' to floats! float() is a little more
# powerful than int() :p

# Convert to string using str()
age = 23
teeth = 31.5
print(str(age), str(teeth))
# Works on both ints and floats!
# In the previous lecture, we had tried to call len(1234) which didn't work since
# len() wants a string. If you wanted to count the number of digits in some number,
# you could get around this doing len(str(1234)). This turns 1234 into a string
# so that len() can count it easily.

########################
# FUNCTION COMPOSITION #
########################

# I just did this. That's what len(str(1234)) is. Function composition is applying
# or calling one function with the result of another. It can make things more 
# concise. Here are more examples:

# Using intermediate variables
x = -5
y = -8
abs_x = abs(x)
abs_y = abs(y)
z = min(abs_x, abs_y)
print(x, y, z)

# Using composition
x = -5
y = -8
z = min(abs(x), abs(y))
print(x, y, z)

# We often do this when we want a number as input
try:
    number = int(input("Credit card number again hurry now: "))
    print(fr"""Current Bank Balance: {number * 1200}.00 $ 
    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$
   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$__  $$ /$$__  $$|__  $$__/
      | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$  \ $$| $$  \ $$   | $$
      | $$| $$$$$$$$| $$      | $$$$$/  | $$$$$$$/| $$  | $$   | $$
 /$$  | $$| $$__  $$| $$      | $$  $$  | $$____/ | $$  | $$   | $$
| $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$   | $$
|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$| $$      |  $$$$$$/   | $$
 \______/ |__/  |__/ \______/ |__/  \__/|__/       \______/    |__/
""")
except Exception as thats_not_a_number:
    print("""Too bad, you would've won the
    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$
   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$__  $$ /$$__  $$|__  $$__/
      | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$  \ $$| $$  \ $$   | $$
      | $$| $$$$$$$$| $$      | $$$$$/  | $$$$$$$/| $$  | $$   | $$
 /$$  | $$| $$__  $$| $$      | $$  $$  | $$____/ | $$  | $$   | $$
| $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$   | $$
|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$| $$      |  $$$$$$/   | $$
 \______/ |__/  |__/ \______/ |__/  \__/|__/       \______/    |__/
""")
    


# This will only work if we trust our user enough to actually input an int!
# Otherwise this all goes to shit, since we have already seen that the int
# function breaks down when you give it a float or a string containing invalid
# characters

# NOTE: It is recommended to "comment out" lines 57 and 91 (the ones that use
# the input() function) so that you don't need to keep entering your beatufil
# credit card number every time you run this file. Comments are what I've been
# typing in this whole time btw. They are lines of plain text that do not run.
# You can "disable" lines of code by slapping a hashtag at the beginnning of
# the line.
