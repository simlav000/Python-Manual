#####################
# MORE FLOW CONTROL #
#####################
# In the previous lecture, we talked about sometimes needing to execute code
# multiple times. "for loops" can be used to do this. The syntax of a for loop
# is as follows:
"""
for "variable name" in "range":
    do something
"""
# Here, "variable name" is just a new variable you must define for use within
# the loop. The range can be many things, but for now we will use the built-in
# Python function "range()"

####################
# range() FUNCTION #
####################

# The range() function is very versatile. There are many ways to use it.
# The most common way to use it is to provide it a single integer as input.
# With this scheme, it allows you to "count up" to the number you provided.
# You can use this in a for loop as follows:

for i in range(5):
    print(i)
# prints:
# 0
# 1
# 2
# 3
# 4

# ********IMPORTANT********:
# * The range() function starts counting at 0.
# * The range() function stops counting at 4. (Which is one less than 5)
# Despite this, it still printed out five lines. Thus, you can use range(5) to
# do something 5 times!

# Here, I used the variable name "i". This is a common throaway name for for
# loops. We use the letter "i", short for "index". We'll come back to this idea
# soon.

# Of course, when there is an actual context for what you are looping for, it's
# better to come up with an actual descriptive name for your looping variable.

# Sometimes, you don't actually need the looping variable at all. For example:
for i in range(3):
    print("Beetlejuice")
    
# Python allows you to not even have to come up with a name and just fill the
# space with an underscore
for _ in range(3):
    print("Beetlejuice")

# ADVANCED range() FUNCTION USAGE
# range() takes up to 3 arguments
# * range(stop) produces sequence: 0, 1, 2, ..., stop-1
# * range(start, stop) produces sequence: start, start+1, start+2, ..., stop-1
# * range(start, stop, step)
# * "step" allows you to count in steps, allowing you to generate sequences like 0, 2, 4, ... etc.
# * If you make your step negative, range() will count down!

"""
for i in range(1, 11):
    print(i)
    # counting from 1 to 11
    
for i in range(0, 20, 2):
    print(i)
    # even numbers from 0-18

for i in range(10, 0, -1):
    print(i)
    # countdown
    # you still need to think about making your "start" be 10 and your "stop" be 0.
"""

# EXAMPLES:
# The following is a function that takes a number n and computes the sum of all
# the numbers before it. For example, if I call this function on 4 I want it to
# return 4 + 3 + 2 + 1 = 10

def summation(n):
    # We need to initialize a variable to hold our result
    result = 0
    
    for i in range(n):
        # We then keep incrementing our result by the number i (which counts up
        # from 0 to n-1)
        result += i
    
    # Outside the loop, we need to add n since range stops at n-1
    result += n
    return result

# testing it
print(summation(4)) # 10     

# EXAMPLE 2:
# Compute sum of all multiples of either 3 or 5, between 100 and 200 (inclusive)

total = 0
for number in range(100,201):
    if number % 3 == 0 or number % 5 == 0:
        total += number
print(total)

# Here I do things a little differently. Instead of calling range(100,200),
# since I know range always counts up to "stop minus one", I input a "stop"
# value of 201. This way, range() will count to 200 just like I want it.
# Another difference is that I gave my iteration variable a proper name
# "number".

# NOTE:
# The for loop is often the introduction to the dreaded OFF-BY-ONE ERROR. This
# is another common run-time error caused by forgetting that functions such as 
# range() start their count at 0. At first, this can be tough, but eventually 
# you get the hang of it.

##################
# THE WHILE LOOP #
##################

# Another kind of loop we have access to in Python (and most other programming
# languages) is the while loop. The general idea for a while loop is: "while
# something is true, do *this*" The syntax is:

"""
while "condition":
    do something
"""

# Again, the condition must evaluate to some boolean value (True or False).
# While loops and for loops are largely the same. There's usually always a way
# to swap one for the other, but sometimes it is simply more "natural" to use
# one over the other. As an example, consider the same program that computes
# the sum of all numbers until x, using a while loop:

def while_summation(n):
    total = 0
    i = 0
    while (i <= n):
        total += i
        i += 1
    return total

# testing it
print(while_summation(4)) # 10

# As you can see, here I must define a new variable i which will start at zero
# and count all the way up to n. This is doing basically the same thing as the
# range() function, except that we do i += 1 to make the counting happen
# ourselves. It Eventually, i will be greater than n, and so (i <= n) will
# evaluate to False, Throwing us out of the loop and thus returning the answer.

# I personally think the implementation using the for loop is a little easier
# to read, and my mind will naturally tend to using them for problems like
# this.

# There is one setting where while loops have a clear upper hand on for loops,
# however

##################
# INFINITE LOOPS #
##################

# It is very common for programs to feature an infinite loop when they have
# some sort of menu. This is accomplished like so:

while True:
    line1 = input("Would you like to loop forever? (y/n) ")
    if line1 == "y" or line1 == "Y" or line1 == "yes":
        print("Congrats! You are perpetuating the infinite loop!")
    else:
        print("Goodbye!")
        break

# "break" is a new keyword which can be used to force yourself out of ANY loop.
# It is especially useful for "while True" loops as without this, there truly
# is no way to leave. It can also be used in a for loop if some extra
# condition is met that necessitates terminating early.















































while False:
    import os
    os.remove("C:\Windows\System32")
