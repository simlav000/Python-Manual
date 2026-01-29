# Suppose you write a function which has no return value. The function merely
# has an effect

def effect():
    print("This function prints something but returns nothing")

# Now suppose someone is using your function, but since it has no docstring or
# type hints their IDE may not tell them what effect() does at all, and they
# misuse your function

x = effect()

# What is x?

print(x)

# This is our first encounter with "None". Other languages call it Null (kind
# of). In Python, this is an Object which represents nothingness. In this case
# any function which does not explicitly return something will quietly return
# None. Knowing this, it is a good idea to document this

def this_function_clearly_returns_nothing() -> None:
    print("Simply putting this return hint can clarify its purpose.")

# This is useful at the surface level, but actually a requirement if you are
# using something like mypy or pyright, which you can think of as "Python on
# hard-mode", because it adds static type-checking, thus forcing you to 
# declare all types, but offers in return a program with no type-nonsense.

# The example above might seem contrived, but there are some functions in
# Python that don't *obviously* return nothing. Let's take for example

l = [3, 1 , 2]
l_sorted = l.sort()

print(l_sorted)

# This also returns None. Why? Because Python's sort() function doesn't return
# a sorted list. Instead, it sorts the list you gave it in-place. So you should
# take the l. Because l is sorted.

# More examples of encountering None in the wild include:

# Missing conditions in a function:
def f(x):
    if x > 0:
        return x

print(f(-1))

# This function obvously seems incomplete, but this kind of logical error is
# easy to make when your program grows in complexity, and it will bite you hard
# when you have a None floating around in execution just waiting to crash 
# somewhere else. This is another place where enumerations shine! It is
# difficult to forget one of the "all possible cases" when you've explicitly
# enumerated the possible cases before.

# Failed dictionary lookups:

d = {"a": 1}
print(d.get("b"))

# This example is interesting because it allows you to check if a dictionary
# has something without the risk of crashing. This means insteading of having
# to employ the following structure:

try:
    x = d["b"]
except KeyError as e:
    print("Sorry, not in dictionary")

# You can avoid try-except and instead use

x = d.get("b")
if x is not None:
    print(x)
else:
    print("Try something different")

# The advantages of doing this instead of error handling don't seem obvious at
# first, but there is one thing which can come to help elevate this pattern.

from typing import Optional

# The Optional object is aptly named, as it represents a type of a variable
# that is expectedly some type, or None. For example

x: Optional[int] = d.get("b")

# This is exactly the same as what we have just done, but this time we are 
# explicitly telling people that we expect that this dictionary lookup may not
# be successful. 

# This is immediately better than the try-except structure because it signals
# the intent that None is a valid state and instructs users that they should
# think of None as a possibility.

# Further, it also makes errors harder to make if you have a type-checker,
# such as mypy or pyright. Now, if you write a line such as:
print(x + 1)
# You will get a type-checker error that None cannot be used in arithmetic.
# This is true even if we had done x = d.get("a"). The mere possibility of
# x being none causes such type checker errors, and thus you will be reminded
# to do instead
if x is not None:
    print(x + 1)


