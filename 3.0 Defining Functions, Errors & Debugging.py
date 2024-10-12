###################
# KINDS OF ERRORS #
###################

# In messing around with Python, you have inevitably come across a few errors.
# There are different kinds of errors you will encounter:

# Syntax Errors: These occur when syntax is incorrect. This means misspelling
# keywords, missing quotes or parentheses etc. These are basically typos. They
# are patterns that you have written using your keyboard that the Python
# interpreter cannot understand. The program cannot run.

# Runtime Errors: Also called exceptions, these occur when there is a problem
# in the program during execution. All code executes until an exception occurs.
# The following code would produce a "NameError" because the variable y was not
# created before it was used. 
"""
x = 5
print("Value of x is", x)
print("Square of x is", y**2)
"""
# A "NameError" is one of the many possible kinds of Runtime errors.

# Runtime errors are another kind and are a bit harder to deal with since they
# are brought upon by faulty logic in the code you have written. Thankfully,
# both syntax and runtime errors generate an error message which is printed in
# the Python shell. These help in addressing the issue at hand.

# Semantic or logic errors are said to occur when a program executes without a
# problem but does not produce the correct/expected output. These are the
# hardest to deal with since there will not be a handy error message. These 
# kinds of errors happen because you made a mistake because you are supid.

#############
# DEBUGGING #
#############

# Debugging is the process of finding and removing these pesky logic
# errors from your program.

# Thonny's debugger is the goat. In Thonny, we can use debugging features to
# understand how expressions are evaluated. To show variables and their values,
# go to: View -> Variables. This should open a panel to the side listing all
# variables and their values by the time the program has finished running (this
# means it will not show you any intermediate values)
    
# There is a way to see these intermediate values though! You can run your
# program in debug mode by clicking the bug right next to the run button. From
# there we are given two options: 
# 1. Run the program line-by-line using "step over" button next to the bug. 
# 2. Inspect in detail what is happening in any specific line by pressing the 
#    "step into" button. 
# 3. If this is too much detail, you can either "step out" or "step over".

#Try debugging the following code

x = 7

# Increment value of variable x by 1

x += 1

# Perform this operation

y = x * x + 2 * (x + 1) + max(x + 1, 5)

# Calling print() with 4 arguments

print("x =", x, "y =", y)

# Printing some sort of stick using the length of our message

message = "Hello"

print("+", "-" * (len(message) + 6), "+")

# Debuggers can be very powerful and it is recommended you familiarize yourself
# with this tool.

#######################
# DEFINING A FUNCTION #
#######################

# A function is a named block of code that performs a task. So far we have been
# using (calling) functions to do specific tasks (print(), input(), etc.) We
# can also define/create our own functions:
"""
def function_name(argument_1, argument_2, ..., argument_N):
        write code here
        return "something"
        
"""

# The first line is called a function header.
# "def" is a Python keyword used to define functions.
# You follow this up by giving your function a name, and in parentheses you
# list out the expected arguments. You must also give these arguments a name.
# The hardest part of programming is coming up with good names... 
# You complete your header by slapping a colon (:) at the end.

# What comes after the header is the body.
# Notice how the function body is INDENTED relative to the header. You can
# indent using "tab" on your keyboard. A single indent is equivalent to four
# spaces on your keyboard.

# NOTE: Python takes indenting VERY seriously. Improper indentation leads to 
# Python simply not understanding what you are writing. This is also something
# Python gets some flack for, as a more traditional approach to capturing the 
# "space that belongs to the function" is to use curly braces {} where the 
# function body resides inside the braces. Python decided to use indentation 
# instead.

# "return" is also a Python keyword. It is used to define the output of your
# function. In this case, the output is "something" (NOT a Python keyword).
# This could be a variable which holds a value, literally just a value, or
# NOTHING. Functions with no return value do not need the "return" keyword at
# all.

# When we define a function using def:
# It is not executed.
# Only the function name is created, which refers to the code block inside the
# function (the body). Only when we call a function (as we have done previously
# with print(), len(), type(), etc.), the code block inside the function (the
# body) is actually executed with the arguments it was given.

# NOTE: In most programming languages, indenting is not necessary. In Python,
# your code will literally not run if you indent things incorrectly (Python
# will throw an IndentationError at you). While I personally don't like this
# about Python, it does force you to write code following a standard that is
# largely universal across languages. If you ever venture out further to other
# programming languages, keep the indenting practices you learn here in your
# back pocket as it will make your code much easier to read.



###############################
# FUNCTIONS WITH NO ARGUMENTS #
###############################

# Such functions always do the same thing each time they are executed.
# For example:

def display_greeting():
    print("X------------X")
    print("| [REDACTED] |")
    print("X------------X")
    
# Function call
display_greeting()

###############################################
# FUNCTIONS WITH ARGUMENTS AND A RETURN VALUE #
###############################################

# Examples:

# Funtion that evaluates a polynomial:
def f(x):
    return x * x - x - 1

# Equivalently
def g(x):
    result = x * x - x - 1
    return result

# Call the function f
y = f(5)
print(y)

# Call it again with different argument. Remember we can compose functions!
print(f(10))

# We can have more than one argument

# Example:
# Function which calculates the average between two numbers:
def mean(x, y):
    return (x + y) / 2
# (notice the parentheses making it clear that we add first, then divide)

print(mean(3, 4))
print(mean(f(5), f(10)))

# When a function is called, the correct number of arguments must be passed to
# avoid an error.

##############
# DOCSTRINGS #
##############

# A docstring (documentation string) is a multiline (triple-quoted) string that
# we write after the header of a function to explain how it works.

# As stated earlier, writing code that others can read is one of the most
# important parts of programming. Writing a detailed description of how to use
# a function you have written goes a long way. If people don't know how your
# code works, they will scrap it and write it themselves.

# Even if you are not working collaboratively, if you write some fucked up
# shit, you might forget how it works by the time you have to go and debug
# it...

def euclidean_distance(x1, y1, x2, y2):
    """
    Computes Euclidian distance between to points in 2D.

    Args:
        x1: x-coordinate of first point (float)
        y1: y-coordinate of first point (float) 
        x2: x-coordinate of second point (float) 
        y2: y-coordinate of second point (float) 

    Returns: the euclidean distance as a float
    """
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return d ** 0.5

print(euclidean_distance(1, 1, 2, 2))

# Notice the format:
# 1) Start with a general description of what the function does
# 2) List what each argument is supposed to be, and include the expected type!
# 3) Describe what the output is including its type!
