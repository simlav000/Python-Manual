# CHALLENGE
# WRITE A FUNCTION THAT GIVEN A NUMBER X PRINTS EITHER OF THE FOLLOWING:
    # X IS EVEN
    # X IS AN ODD NUMBER MULTIPLE OF 3
    # X IS AN ODD NUMBER NOT MULTIPLE OF 3

def challenge(x):
    if x % 2 == 0:
        print(x, "is even")
    else:
        if x % 3 == 0:
            print(x, "is an odd multiple of 3")
        else:
            print(x, "is odd and not a multiple of 3")
            
# Here, I'm choosing to go for an approach which nests two if-then statements. I personally find
# it to be fairly straight forward. Any number is either even, or it isn't, and if it isn't even,
# it's either a multiple of 3 or it isn't. 

# TESTING
challenge(2)
challenge(3)
challenge(6)
challenge(21)
challenge(23)