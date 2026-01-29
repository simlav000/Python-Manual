#====================
# 16.0 Decorators.py
#====================


# 1. Functions are objects

def say_hello():
    print("Hello")

# We can assign a function to a variable
f = say_hello

# And call it through that variable
f()

# This already tells us something important:
# functions can be passed around like any other object.


# 2. Functions can take other functions

def call_twice(func):
    func()
    func()

call_twice(say_hello)

# Nothing fancy so far.
# But this is the core idea behind decorators.


# 3. Functions can return functions

def make_greeter():
    def greet():
        print("Hi!")
    return greet

g = make_greeter()
g()

# So now we know:
# - functions can be passed in
# - functions can be returned
#
# Decorators combine these two facts.


# 4. A first decorator (manually)

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_bye():
    print("Bye")

say_bye = my_decorator(say_bye)

say_bye()

# What happened?
#
# say_bye originally referred to the original function.
# After decoration, say_bye now refers to wrapper().
#
# The original function still exists, it's just enclosed
# inside wrapper via a closure.


# 5. The @decorator syntax

# Python gives us syntactic sugar for the previous pattern.

@my_decorator
def say_thanks():
    print("Thanks!")

say_thanks()

# This is exactly equivalent to:
#
# say_thanks = my_decorator(say_thanks)
#
# Nothing more, nothing less.


# 6. Decorators with arguments

def make_loud(func):
    def wrapper():
        result = func().upper() + "!!!"
        return result
    return wrapper

@make_loud
def get_greeting():
    return "Hello"

print(get_greeting())

# Important rule:
# The wrapper must accept the same arguments as the function
# it is wrapping (or be flexible enough to handle them).


# 7. General-purpose decorators (*args, **kwargs)

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        print(f"  args = {args}")
        print(f"  kwargs = {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(2, 3))

# This is the most common decorator shape you will see in real code.


# 8. Decorators that modify behavior (timing example)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)

slow_function()

# This is a classic use-case for decorators.

# One nice thing about decorators is that they can be implemented once and then
# tacked onto other functions if needed, and easily removed. The timing example
# is great. If you notice your code starts running slow, implement a quick 
# timing decorator, slap it on your functions, then find the slowest function.
# Then, you know who is taking the most time!

# This pattern is also great for logging, caching, validation, authorization,
# etc.
