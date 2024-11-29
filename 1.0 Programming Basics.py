#####################
# MORE ON OPERATORS #
#####################

# Just to flesh out a few of the lessons I hope you've learned through tinkering
# on your own with operators, consider the challenge of converting some given "duration", 
# expressed as elapsed time in seconds, to some more intuitive format such as 
# minutes and seconds.

duration = 320
minutes = duration // 60 # Integer division, basically divide by 60 and round the result down
seconds = duration % 60  # Modulus operator, gives the remainder of the above division operation.
print(duration, "seconds equal", minutes, "minutes and", seconds, "seconds.")

# For all operators (except divison / and integer division //):
# * If one or more of the operands are of type "float" the resulting value will also have type "float"
# * If both operands are of type int, result will be of type int

# For division operator /:
# * The result value is always of type "float"

# For integer divisioin //:
# * The result is always an "int"

# Here we can see these rules in action
x = 3
y = 9
z = 9.0
a = x*y
b = x*z
print(x*y)
print(type(a))
print(x*z)
print(type(b))

# BASIC STRING OPERATIONS
# Strings are sequences of zero or more characters.
# In Python, strings are enclosed by either single or double quotes.

"Hello"

'everyone!'

# Double quotes can be placed in single quotes
'So that its possible to "use them,"'
         # ^ *

"and singles can be used in doubles to use apostrophies like I'm doin' 'ere." # and vice versa.

# * : Can't put an apostrophe here or else Python will terminate the string early and you'll be 
# left with a SyntaxError. Your code edit can helps you avoid these mistakes thanks to the color
# difference between strings and variable names.

'123' # this is a string, not a number!

"" # this is an empty string (zero characters long!)

# A multi-line string using triple quotes
"""

          .?77777777777777$.            
          777..777777777777$+           
         .77    7777777777$$$           
         .777 .7777777777$$$$           
         .7777777777777$$$$$$           
         ..........:77$$$$$$$           
  .77777777777777777$$$$$$$$$.=======.  
 777777777777777777$$$$$$$$$$.========  
7777777777777777$$$$$$$$$$$$$.========= 
77777777777777$$$$$$$$$$$$$$$.========= 
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++: 
 7$$$$$$$.==================++++++++++. 
 .,$$$$$$.================++++++++++~.  
         .=========~.........           
         .=============++++++           
         .===========+++..+++           
         .==========+++.  .++           
          ,=======++++++,,++,           
          ..=====+++++++++=.            
                ..~+=...
"""
# Credit: https://gist.github.com/xero


# Single quotes work too
'''
B
R
U
H
'''

########################
# STRING CONCATENATION #
########################

# Strings can be joined with + operator.

message_1 = "Hello" + "everyone"
print(message_1) #Helloeveryone

name = "Alice"
message_2 = "Hello " + name
# Notice the space^    v
print(message_2) #Hello Alice

# Strings are not numbers
string = "1" + "2" + "3"
print(string) #123

# Addition like this is undefined
price = 100
print(price + "USD") #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#####################
# STRING REPETITION #
#####################

# Strings can be repeated multiple times using * operator
print("Rats? Rats make me crazy, I was in a room once, a rubber room. A rubber room with rats. " * 20)

#######################
# THE LENGTH FUNCTION #
#######################

# the function len() returns length of its argument string.

password = "xyz123"
# terrible password btw
print("Password length:", len(password)) # Password length: 6

# Out of all the types we currently know, str is the only one which is accepted
# by the len() function.
# print(len(1234)) #TypeError: object of type 'int' has no len()

#####################
# MORE ON VARIABLES #
#####################

# Let us write code that implements a formula to convert fahrenheit to clesius:
# Variables allow "saving" intermediate results of a computation.
# Using variable fahrenheit, now we just change value here
# instead of changing it in the formula below
fahrenheit = 10
#Store the result of the expression
celsius = 5*(fahrenheit - 32)/9
print(fahrenheit, "F in C is", celsius)

# Variables can be reassigned new values
# Create variable name "number" and assign a value to it
number = 123
print(number) #displays 123

# Assign new value to existing variable "number"
number = -50
print(number) #displays -50

# Add 10 and assign the resulting value to existing variable "number"
number = number + 10
print(number) #displays -40

# What did we just do here? On the right of the equal sign, "number" is holding the value -50. We add 10
# to this and store the result (-40) to the same variable "number"

# NOTE:
# The pattern of doing: number = number + 10 is so common that new operators were introduced to reduce the
# redundant use of the variable name twice. You can instead use the "increment" operator:

number += 10 # "Add another lot of 10 to number"
print(number) # Displays -30

# As expected, there are associated "decrement" operators and one for multiplication/division too.
# Try messing around with (-=), (*=) and (/=)


# New values can be of different types than they were
number = 123  # an int value
message = "hello"  # a string
print(number, type(number))
print(message, type(message))

# Now, message refers to the number 123
message = number
print(number, type(number))
print(message, type(message))

# NOTE:
# This is actually fairly uncommon in most programming languages, and Python gets a lot a flack for it. On one hand,
# it is nice that you have the freedom to change what type a variable is holding. On the other hand, it actually makes
# code much more breakable. Imagine you're writing a program that has a timer. You probably only want your timer to have
# type int if you're counting seconds elapsed, or float if you want some extra precision. Unfortunately, Python happily
# will allow you to make the mistake of making the timer a string. Be careful!

###################
# Swapping Values #
###################

# Sometimes we need to swap two values.
x = 137
y = 42

# Try swapping:
temp = x
x = y
y = temp
print("x =",x,", y =",y) # 42 137

# Try to think of why we need a temporary variable?
# What happens if we try to skip the middleman?



