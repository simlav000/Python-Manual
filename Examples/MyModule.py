def MyFunction():
    print("Aye")


# Testing
MyFunction()

# If anyone imports this file as a module, they will see the result of calling
# the above function printed to their terminal, and they will likely be
# confused as to where this comes from.

# You can protect this from happening via the following incantation:


if __name__ == "__main__":
    MyFunction()
    print("This won't print when someone imports this module")

    # Here, we are referring to a special variable called __name__.
    print(__name__) # __main__

# This is outside the incantation, and you should see that this will print
# "MyModule" when some other file imports this.
print(__name__)

# Aside from the use-case of keeping your modules clean, this incantation is
# also not-optional in many other languages. The ability to just write a line
# of code that doesn't exist inside a function is not universal to other
# languages, which often require a main() function to exist as an entry-point.

# 
