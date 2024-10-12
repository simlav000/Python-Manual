#####################
# FLOW OF EXECUTION #
#####################

# This refers to the order in which statements (lines of code) are executed. So
# far in our programs, each line was executed unconditionally. For most
# programs, it is not enough as we need to make choices as to what should be
# done, or run code repeatedly.

# We need to control the flow of execution in our programs
# This control flow determines:
    # Which parts of the code should always run
    # Which parts should be run only under certain conditions
    # Which parts should be executed repeatedly
# All of these can be achieved using control flow statements
    # "if" statemet for conditional execution
    # "for" and "while" loops for repeated execution

# IF STATEMENT - TO EXECUTE OR NOT TO EXECUTE
# To write useful programs, we almost always need to check certain conditions
    # we might want to execute certain statements only in specific situations
    # The "if" keyword gives us this ability
    # The syntax of an "if statement" in Python is as follows:
"""
if "condition":
    # do something
"""
# Conditions must be a boolean expression. That is, they evaluate to
# something of type bool "do something" here is just one or more Python
# statements (lines of code) Notice the indent after the if statement
# Indentation is required to tell Python that the code belongs inside the "if"
# statement Lastly, we add a colon (:) at the end of the condition

#EXAMPLE 1
x = 10
if x > 0:
    print(x, "is positive")
# Try changing x to a negative number and notice that this line of code is not
# executed

#EXAMPLE 2
num = -5.2

absolute_num = num
if num < 0:
    absolute_num = -num

print("Absolute value of", num, "is", absolute_num)

#EXAMPLE 3
x = 1000
y = 123
min_value = x
if y < min_value:
    min_value = y

print("minimum of", x, "and", y, "is", min_value)

#################################
# IF STATEMENT WITH "ELSE" PART #
#################################

# If statements can have and "else" condition to choose between two code blocks
# The syntax is as follows:
"""
    if condition :
        code block 1
    else:
        code block 2
"""
# When "condition" is True, code block 1 is ran
# otherwise, code block 2 is ran.
# These code blocks are also called branches of the if-statement

x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative")
# This time one of the branches will always run, but which one it is depends on
# the value of x.

x = -5
if x > 0:
    print("x is positive")
else:
    print("x is negative")

# What if there are more than two conditions? Sometimes we want to check a
# series of mutually exclusive conditions. To do so, we can use a series of
# "elif" blocks in an if statement. "elif" is short for "else-if" The syntax is
# as follows:
"""
if condition_1:
    code block 1
elif condition_2:
    code block 2
elif condition_3:
    code block 3
...
"""
# With this syntax, you may also add an "else" clause as a catch-all if none of
# the previous branches have met the necessary conditions

# EXAMPLE
income = 20000

if income < 12000:
    tax = 0.0
elif income < 30000:
    tax = income * 15.0 / 100
elif income < 100000:
    tax = income * 20 / 100
else: # If all the above were False i.e. income >= 100000
    tax = income * 25.0 / 100
print("Your tax is", tax)

# These being mutualy exclusive implies only one of the above will get
# executed. Order here matters. If the first condition is True, later
# conditions will not be checked.

# EXAMPLE 2
# Can you catch the issue with the following program?
money = 5000.0

if money > 0.0:
    print("Positive balance")
elif money > 1000.0:
    print("You're rich! Go celebrate!")
else: 
    print("Uh-oh. No money.")

# The problem with this code is that any value over 0 will return "positive
# balance" meaning "You're rich! Go celebrate!" will never be printed. This can
# be fixed by swapping the first two branches. This is a very common mistake
# that Python will not throw error messages at you for. It is up to you to
# avoid these logical errors. 
# Good luck!

########################
# NESTED IF STATEMENTS #
########################

# if-statements can be nested within other if-statements

# EXAMPLE
x = 10
if x > 0:
    print("positive")
else:
    if x < 0:
        print("negative")
    else:
        print("zero")

# this code is logically equivalent to the chained if statements:
x = 10
if x > 0:
    print("positive")
if x < 0:
    print("negative")
else:
    print("zero")

# Both can be used but it is worth noting that nested conditionals can become
# difficult to read

# NOTE:
# When in a function, if we return a value, the rest of the function will not
# execute, as returning is the final thing it does. This means that we can 
# avoid the following pattern:

def bad_example(one_thing):
    if one_thing:
        return True
    else:
        return False

# In favor of:

def good_example(one_thing):
    if one_thing: # If this is true
        return True # This executes and we exit the function
    return False # Otherwise, we execute this and exit the function

# NOTE:
# As a very loose guideline, if-then statements begin being difficult to read
# once you get three or four levels deep. It is often possible and preferable
# to reduce the "depth" of your nesting by using the boolean operators such as
# "and", "or", and "not". This is also not always easy to do.

# EXAMPLE
# Consider the following function which tells you if a customer is eligible for
# a discount based on their age, purchase amount, and membership status

# First, with nesting
def is_eligible_nested(age, amount, is_member):
    if age > 21:
        if amount >= 50:
            if is_member:
                return True # is eligible
    return False

# Now with boolean operators:
def is_eligible(age, amount, is_member):
    if age > 21 and amount >= 50 and is_member:
        return True
    return False

# Much cleaner right?

# NOTE:
# Often times, the logic you are trying to implement is much more complex. This
# actually opens up a whole branch of mathematics called "propositional logic".
# It's like doing math with truth statements instead of numbers. (A truth
# statement is one that can be judged to be either True or False) This is where
# the truth tables come from, among other things. While you absolutely do not
# need propositional logic to write code, it is here that you would learn the
# tools required to simplify complicated logic into something much easier to
# digest, among other things. If ever you go and learn some math for
# programming, this is a great place to start.

# CHALLENGE
# WRITE A FUNCTION THAT GIVEN A NUMBER X PRINTS EITHER OF THE FOLLOWING:
    # X IS EVEN
    # X IS AN ODD NUMBER MULTIPLE OF 3
    # X IS AN ODD NUMBER NOT MULTIPLE OF 3
