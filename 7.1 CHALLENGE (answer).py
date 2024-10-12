# CHALLENGE
alphabet = "abcdefghijklmnopqrstuvwxyz"
# 1. Slice "alphabet" to print every second letter starting from "a"
# I.E: "acegikmoqsuwy"
# (Basically skipping every second letter of the english alphabet)

# 2. Now every other letter but starting at "b"
# I.E: "bdfhjlnprtvxz"

# 1.
print(alphabet[::2])

# What's going on?
# I am telling the slice to start and stop at their default values,
# which considers the whole string, but I am making the "step" equal to 2
# which skips every other letter.

# 2.
print(alphabet[1::2])

# What's going on?
# This time, I am doing the same thing, but I am starting my slice at the
# index 1. Recall that an index of 1 actually means the second letter ("b").
# Thus, starting at "b" with a step size of 2 gives me every other letter.
