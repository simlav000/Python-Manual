################################################
# BOOLEAN EXPRESSIONS AND COMPARISON OPERATORS #
################################################

# Python has two values "True" and "False" of type "bool", which are useful for
# expressing and storing yes/no kind of data

print(type(True)) #<class 'bool'>
print(type(False)) #<class 'bool'>

# This is a new primitive type to worry about!

########################
# COMPARISON OPERATORS #
########################

# These are used to compare two values, such as numbers or strings. The result
# is always a bool value (True or False) The comparison operators we have are:

    # Equals (==): compares two values/variables to see if they are the same.
        # * This is not the same thing as the (=) operator!
    
    # Not Equals (!=): This is the opposite of (==)
        # * If (==) returns True, then (!=) returns False and vice versa.
    
    # Less than (<): Returns true if the left operand is smaller than the right operand.
        # * Returns False if both operands are equal
    
    # Less than or equal to (<=): Same as (<) but
        # * Returns True if both operands are equal
        
    # Greater than (>): Returns true if the left operand is larger than the right operand.
        # * Returns False if both operands are equal
        
    # Greater than or equal to (>=): Same as (>) but
        # * Returns True if both operands are equal

# For example:
print("1: ", 10 == 10) # True
print("2: ", 20 == 10) # False
x = 5
y = 10
print("3: ", x == y) # False
print("4: ", x != y) # True
print("5: ", x < y) # True
print("6: ", x > y) # False
# NOTE: I'm just numbering the print statements to make the output more easy to read

# We can use variables to store results of boolean expressions (just like we
# did for arithmetic expressions)
x = 3
is_positive = x > 0
print("6: ", is_positive) # True

x = 5
y = 5
is_equal = x == y
print("7: ", is_equal) # True

# ORDER OF OPERATIONS
# All comparison operators (==, !=, >, >=) have the same priority and are
# evaluated from left to right. All arithemtic and string operations have
# higher priority than comparison operators. Again, parentheses are king for
# removing any ambiguity in this.

x = 5
is_this_true_questionmark = x + 1 == 6
# Checking to see if 5 + 1 == 6
# Apparently you can't end your variable names with actual question marks D:
# This is just like 1984.
print("8: ", is_this_true_questionmark) # True

# Consider this function which checks to see if a number is even:
def is_even(x):
    if (x == 1):
        return False
    if (x == 2):
        return True 
    if (x == 3):
        return False 
    if (x == 4):
        return True 
    if (x == 5):
        return False 
    if (x == 6):
        return True 
    if (x == 7):
        return False 
    if (x == 8):
        return True 
    if (x == 9):
        return False 
    if (x == 10):
        return  True 
    if (x == 11):
        return False 
    if (x == 12):
        return  True 
    if (x == 13):
        return False 
    if (x == 14):
        return  True 
    if (x == 15):
        return False 
    if (x == 16):
        return  True 
    if (x == 17):
        return False 
    if (x == 18):
        return  True 
    if (x == 19):
        return False 
    if (x == 20):
        return  True 
    if (x == 21):
        return False 
    if (x == 22):
        return  True 
    if (x == 23):
        return False 
    if (x == 24):
        return  True 
    if (x == 25):
        return False 
    if (x == 26):
        return  True 
    if (x == 27):
        return False 
    if (x == 28):
        return  True 
    if (x == 29):
        return False 
    if (x == 30):
        return  True 
    if (x == 31):
        return False 
    if (x == 32):
        return  True 
    if (x == 33):
        return False 
    if (x == 34):
        return  True 
    if (x == 35):
        return False 
    if (x == 36):
        return  True 
    if (x == 37):
        return False 
    if (x == 38):
        return  True 
    if (x == 39):
        return False 
    if (x == 40):
        return  True 
    if (x == 41):
        return False 
    if (x == 42):
        return  True 
    if (x == 43):
        return False 
    if (x == 44):
        return  True 
    if (x == 45):
        return False 
    if (x == 46):
        return  True 
    if (x == 47):
        return False 
    if (x == 48):
        return  True 
    if (x == 49):
        return False 
    if (x == 50):
        return  True 
    if (x == 51):
        return False 
    if (x == 52):
        return  True 
    if (x == 53):
        return False 
    if (x == 54):
        return  True 
    if (x == 55):
        return False 
    if (x == 56):
        return  True 
    if (x == 57):
        return False 
    if (x == 58):
        return  True 
    if (x == 59):
        return False 
    if (x == 60):
        return  True 
    if (x == 61):
        return False 
    if (x == 62):
        return  True 
    if (x == 63):
        return False 
    if (x == 64):
        return  True 
    if (x == 65):
        return False 
    if (x == 66):
        return  True 
    if (x == 67):
        return False 
    if (x == 68):
        return  True 
    if (x == 69):
        return False 
    if (x == 70):
        return  True 
    if (x == 71):
        return False 
    if (x == 72):
        return  True 
    if (x == 73):
        return False 
    if (x == 74):
        return  True 
    if (x == 75):
        return False 
    if (x == 76):
        return  True 
    if (x == 77):
        return False 
    if (x == 78):
        return  True 
    if (x == 79):
        return False 
    if (x == 80):
        return  True 
    if (x == 81):
        return False 
    if (x == 82):
        return  True 
    if (x == 83):
        return False 
    if (x == 84):
        return  True 
    if (x == 85):
        return False 
    if (x == 86):
        return  True 
    if (x == 87):
        return False 
    if (x == 88):
        return  True 
    if (x == 89):
        return False 
    if (x == 90):
        return  True 
    if (x == 91):
        return False 
    if (x == 92):
        return  True 
    if (x == 93):
        return False 
    if (x == 94):
        return  True 
    if (x == 95):
        return False 
    if (x == 96):
        return  True 
    if (x == 97):
        return False 
    if (x == 98):
        return  True 
    if (x == 99):
        return False 
    if (x == 100):
        return   True 

# Just kidding.

def is_even_for_real_this_time(x):
    return (x % 2) == 0

print("9: ", is_even(8)) # True

# How does the function work? It uses the % operator (remember, this determines
# the remainder when divided by 2). If a number is even, then it is divisible
# by 2. Therefore, the remainder will be zero! If it's an odd number, then the
# remainder will not be zero! Then, we use the == operator to check if this
# remainder is equal to zero.

# In this example, I use parentheses around (x % 2), but in the future, I will
# omit them. This is because I know that the Mod operator (%) has higher
# precedence than the comparison operator (==). Again, if you aren't sure, add
# parentheses or test it out yourself!

#####################
# COMPARING STRINGS #
#####################

# Comparison operators work for strings as well!

# The comparison is done alphabetically:
print("10: ", "cat" == "dog") # False

# The letter "c" in "cat" appears before "d" alphabetically:
print("11: ", "cat" < "dog") # True

# Uppercase letters appear before lowercase letters:
print("12: ", "cat" < "Dog") # False

# We can compare different types of equalities:
print("13: ", "cat" == 2) # False

# But not inequalities
# print("cat" < 2) #ERROR

# All of the above work the same when using variables.
s1 = "cat"
s2 = "dog"
print("14: ", s1 == s2) #False

########################################
# EQUALITY WITH FLOATING POINT NUMBERS #
########################################

# So I've ommitted A LOT of details when it comes to floats. They're
# complicated. I'm not going to explain how they work but I will show off a
# strange quirk they have. Consider the following example

x = 1.1 + 2.2
print("15: ", x == 3.3) # False
# Can you imagine? Stupid computer can't even do this simple math question.

# Since floating point numbers aren't 100% precise, there is always some small
# error when we add them together (or multiply, divide, etc..) This means that
# in Python, 1.1 + 2.2 != 3.3

# To get over this hurdle, we can check for "equality" by seeing if our answer
# is "close enough"
tolerance = 0.00001
x = 1.1 + 2.2
print(x)

# Check if x and 3 are within our tolerance
print("16: ", abs(x - 3.3) < tolerance) # True
# Here, abs is giving us the difference between the COMPUTED value of 1.1 +
# 2.2, and 3.3 We don't care about the sign since we just want to know how far
# apart these two numbers are, hence the abs() Depending on our tolerance, this
# may evaluate to False

#####################
# LOGICAL OPERATORS #
#####################

# These are useful to combine multiple conditions. Logical operators take
# boolean expressions as operands and produce a result of the type bool
# Python has 3 boolean operators
    # 1: "not" - a unary operator
    # 2: "and" - binary operator
    # 3: "or" - binary operator

# BUT WHAT DO THESE DO EXACTLY?
# 1: "not"
# "not" is an operator (and keyword) you write to the left of any
# variable/value of type "bool" to invert it's value.

# EXAMPLE:
x = True
print("17: ", not x) # False

y = False
print("18: ", not y) # True

# 2: "and"
# "and" allows you to combine two boolean expressions together. It returns True
# if and only if both expressions to the left and right are also True. If any of
# the two expressions are False, the whole "and" expressions evaluates to False

# EXAMPLE:
I_am_human = True
I_can_read = True
I_am_six_at_least_feet_tall = False

print("19: ", I_am_human and I_can_read) # True
print("20: ", I_am_human and I_am_six_feet_tall) # False

# 3: "or"
# The "or" operator allows you to combine two boolean expressions in a
# different manner. It returns True if any of the sub expressions are True.


# EXAMPLE:
its_raining_sharks = False

print("21: ", I_am_human or its_raining_sharks) # True

# NOTE:
# These operators (not, and, or) have what we call "truth tables" you can look
# up online. The truth table for a single "or" between two boolean variables P
# and Q is:
# #----------------#
# | P | Q | P or Q |
# | T | T |   T    |
# | T | F |   T    |
# | F | T |   T    |
# | F | F |   F    |
# #----------------#
# T means True
# F means False
# This table shows off all possibilities of two expressions with an "or" in
# between. It encapsulates the rule that if either P or Q are True, the whole
# thing (P or Q) is True.

# NOTE:
# The use of the word "or" here is actually quite different than the way we use
# the word "or" in English. Generally, if I say "I will eat soup or salad
# today", it sort of feels like a lie if I end up eating both. The English
# language actually uses what we call an "exclusive or", as in, it excludes the
# case where both things end up being true. While there is an exclusive or
# operator in Python, it's not used in the same manner. Just know that "or"
# evaluates to True if both expressions are True, and that this may be a little
# counter-intuitive.

# ORDER OF OPERATIONS
# In order of highest to lowest priority we have:
# not
# and
# or

##############
# CHALLENGES #
##############

# 1. Write a function that takes 3 integers x,y,z as inputs and prints out True
# if y is an even number between x and z. False otherwise. Assume all 3 numbers
# are different. You can use "is_even()" from above simply by calling it!
# Though you should probably use the is_even_for_real_this_time() function.
def challenge(x, y, z):
    return "Implement your answer here"

# 2. Draw the truth table for P AND Q.
