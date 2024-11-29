# Author: Simon Lavoie
# Contact: goadedwiththesocks (on discord) / simon515lavoie@gmail.com
# Feel free to contact if anything is unclear. If I take too long to answer, there's always ChatGPT.
# It's a legitimately good resource for reading more about certain topics in programming.

################
# CHAPTER ZERO #
################

# This set of notes is adapted from an introductory-level computer
# science course I took in 2021 which aims to teach the basics of
# programming through the Python programming language. Each file consists
# of an entire lecture. I highly recommend you have the notes open in one window,
# and copy the code one line/block at a time.

# Before any of this, you'll probably have to install the Python interpreter
# https://www.python.org/downloads/
# This is what allows your computer to read a file which has the ".py" extension
# (default python source code file type) and understand that it is Python code as opposed to
# any other language or plain text.

# Next, you'll need an "IDE" (Integrated development environment) or a text-editor. This is the program
# you will use to actually write the code. There are many to chose from, but a basic -
# no bullshit IDE I highly recommend is Thonny (https://thonny.org/). While I no longer
# personally use this text-editor for Python (in favour of neovim), this one allows you to get
# right into the action, with zero bloat or unnecessary features. Another good choice 
# would be VSCode, but it could be a little more overwhelming to set up.

# For the purposes of this tutorial, I'll assume you picked Thonny.

# Thonny opens up with a large window for you to write code.
# Any time you learn a new programming language, it is tradition to write a "Hello World!" program.
# This is a program that does nothing other than print text to the terminal.
# In python this is very simple. It begins by using a built-in Python function called "print()".
# We'll talk more about functions later, including how to write our own, but for now, try writing:

print("Hello World!")

# And then run the program using the little green play button.
# You'll notice that Hello World! is printed to the terminal. The terminal is an interactive
# environment where you can enter Python code and see the results immediately.
# It's a powerful tool for learning and testing small pieces of code.
# You can write "print("Hello World!")" directly in there too! It then runs by simply pressing Enter.
# (just make sure your cursor is placed to the right of the three arrows (>>>))

# Let's dissect this single line of code we wrote. As previously mentioned, "print()" is a function. It takes
# as input what we call an argument. You feed arguments to functions and they do something with it,
# generating an output. These arguments need to be surrounded by parentheses! ()

# In this case we fed it "Hello World!". These two words are also further surrounded by quotation marks.
# This is what we call a String in the programming world. Strings don't have to be words. They can be any sequence
# of characters surrounded by quotes.

# Let us use this to segue into "types"

#########
# TYPES #
#########

# Programming is all about manipulating data. As you probably expect, however, there are multiple "kinds" of data we
# can manipulate. We call these types. Strings are a type, but they are far from the only one. A few of the most important
# basic types (called primitive types) are:
    # Integers: 0, 1, 2, ...
        # These are the whole numbers (including the negatives). We call these "int"
    # Floats: 1.3212, 9.8, 1.0, ...
        # This is any number having a decimal point. Note that 1 is an int, but 1.0 is a "float"
    # Strings:
        # This is literally any sequence of characters surrounded by quotes. Therefore, "1" is not an int! It's a float. So is "kys"
    
# Of course, there exists more types out there, but we'll take the time to properly introduce them later.
# In order to start playing around with types, let us introduce the concept of a "variable"

#############
# VARIABLES #
#############

# A variable is actually just a name you use to store data within your program.
# This data is often referred to as the variable's "value".
# You may name your variables just about anything you want
# (the exception being certain names reserved by Python itself).

# In order to "declare a variable", you write the desired variable name on the left, followed by an equal sign (=),
# then you provide a value on the right of the equal sign.
# The classic variable is "x". 

x = 5

# Now, any time we reference "x" in our program, the value 5 will appear. Give this a shot by writing print(x),

# Another handy built-in function we will use to test things is the "type()" function. 
# Try writing type(x) and running the program.
# It does nothing.
# Now try writing print(type(x)).
# Now it'll print the result of the type() function.
# We've just "composed" two functions together!

# With these pieces laid out, you can mess around and see how variables work in Python. Try changing the value
# stored at x. Try defining some new variables. Try printing their types.

# In messing about, you may run into your first set of errors. Consider the following line of code:
x = y
# If you run this, Python will complain that "y is not defined". It might even complain
# before you run it, depending on the text-editor you're using.
# This is because "y" is a new name that the python interpreter hasn't learned yet.
# To make something like "x = y" a legitimate line of code, you'd have to assign
# a value to y beforehand.

# EXAMPLE:
y = 6
x = y

# Now, since I set y to 6, then write "x = y", I'll get that x has the same value as y, namely 6.

# NOTE:
# Swapping the order of these two lines will not work.
# Python only knows about names that come before any specific line.

# Before I conclude chapter zero, let me introduce some operators

# OPERATORS
# we've already seen one operator, equals!
# There are many more:

    # Equals (=): Assign a value to a name (x = 5 works, 5 = x won't!)
    #            (Which introduces us to a new rule in naming variables,
    #             namely, variable names can't start with a number).
    
    # Plus (+): Add stuff
        # * Try adding variables. Perhaps with different types? See if that breaks stuff.
        # * What happens when we add strings together?
        
    # Minus (-): Subtract ints or floats
        # * This one doesn't work on things that aren't numbers
        # * There are two "minus" operators
        
    # Minus (-): Negate a number
        # * This one is what we call a "unary" operator. This means that instead of being "binary"
        #   (takes two inputs, one on the left and one on the right), it takes only one, on the right.
        #   This is all to say just slap a minus in front of a number to make it negative.
        
    # Times (*): Multiply stuff
        # * What happens if you multiply a string by an int?
        
    # Divide (/): Divide lol
    
    # Integer Division (//): Find the whole number answer when dividing two numbers
        # * This always yeilds an integer (int)
    
    # Mod (%): Obtain the remainder of a number divided by another
        # * This is the "missing part" of integer division
        # * Seems useless at first but don't underestimate this guy
        
    # Exponentiate (**): If you wanna do "three squared" it's 3**2
        # * Though sometime's it's cleaner to just do 3 * 3

# And i'll leave it at that. Plenty to mess aroud with already. I highly
# recommend you write a few lines of code trying to use these operators, assign
# them to variables, print the results, maybe use the operators in the print
# function itself, tinker around! It's the best way to learn.


#####################################################################
# ORDER OF OPERATIONS - PEMDAS (Please Excuse My Dark Ambient Swag) #
#####################################################################

# When an expression contains multiple operators, which one is applied first?
# All Python operators have some hierarchy.

# The following web page contains a handy table listing the hierarchy with some
# examples: https://medium.com/@thoashook/operations-in-python-69bbbef781a4

# Generally however, you don't need to memorize this.
# An immensely important facet of programming is writing code that other people
# can actually read.

# The order of operations from one programming language to another may or may not
# be the same, but one thing is true for all of them: parentheses () are king.

# This means that instead of writing some garbage like "x = 12 //4 + 2 **4–5"
# use parentheses to make clear what you are trying to do.

x = (12 // 4) + (2 ** 4) - 5
print(x)

    
        
