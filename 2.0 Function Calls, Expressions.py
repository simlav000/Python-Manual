##################
# FUNCTION CALLS #
##################

# Functions take zero or more input values, perform an action or computation,
# and return the result (if any).
# A function call looks like this:
# function_name(argument_1, argument_2, ..., argument_n)
# The number of arguments required by a function depends on how it was implemented.

# When it comes to built-in functions, it is often required to read
# documentation to know how a function is expected to be used. Here's a handy
# page which lists all the basic built-in Python functions:
# https://docs.python.org/3/library/functions.html The following are a few of
# the built-ins available in Python

##########
# type() |
##########
# We've seen this one already.

###########
# print() #
###########
# This one too. But there's more to this one.
# It is worth noting that print() can take many inputs at the same time!
# All you have to do is seperate the inputs using commas and it will print all inputs with spaces in between

# EXAMPLE
x = "can"
print("print()", x, "take many inputs")

######################
# GETTING USER INPUT #
######################
# We use input() function to ask for input data from the keyboard.

# input(prompt): Displays the prompt string and waits for the user to enter one
# line of input text in the terminal. The remaining code will not run until
# this input is entered. The function returns the text entered by user as a
# string, which can be stored in a variable.

number = input("Credit card number now: ")

print("I will buy illegal drugs using the credit card with number: ", number)

# Despite entering a number, all input recieved from the Python shell is of
# type string. Thus, if we wish to perform some sort of mathematical operation
# on said input, we must convert it to a float or int

number = int(number)

print("I will purchase ", number * 2, " percocets and consume them immediately")

# for legal reasons this is a joke

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
sex = 69.69
print(str(age), str(sex))
# Works on both ints and floats!
# In the previous lecture, we had tried to call len(1234) which didn't work since
# len() wants a string. If you wanted to count the number of digits in some number,
# you could get around this doing len(str(1234)). This turns 1234 into a string
# so that len() can count it easily.

########################
# FUNCTION COMPOSITION #
########################

# We have breifly touched on this topic when printing the type of a variable.
# Function composition is applying or calling one function with the result of
# another. Consider the following two examples:

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

# We can use function composition to simplify the above percocets code
number = int(input("Credit card number again hurry now: "))
print("I will purchase ", number * 2, " explosives from the explosives store")

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

#####################################################################
# ORDER OF OPERATIONS - PEMDAS (Please Excuse My Dark Ambient Swag) #
#####################################################################

# When an expression contains multiple operators, which one is applied first?
# All Python operators have a PRECEDENCE and ASSOCIATIVITY:
# Precedence - for two different kinds of operators, which is applied first?
# Associativity - for two operators with the same precedence, which is first?

# The following web page contains a handy table listing the hierarchy with some
# examples: https://medium.com/@thoashook/operations-in-python-69bbbef781a4

# Generally however, you don't need to memorize this.
# I've not spoken much about this yet, but an immensely important facet of
# programming is writing code that other people can actually read. The order of
# operations from one programming language to another may or may not be the
# same, but one thing is true for all of them: parentheses () have highest
# precedence.

# This means that instead of writing some garbage like "x = 12 //4 + 2 **4–5"
# where only a Python developper who remembers the precedence of all operators
# can understand, use parentheses to make clear what you are trying to do

x = (12 // 4) + (2 ** 4) - 5
print(x)


