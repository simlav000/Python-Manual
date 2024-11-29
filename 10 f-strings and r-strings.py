###########################
# F-STRINGS AND R-STRINGS #
###########################

# This one is short and sweet but don't underestimate this power.

# The following knowledge I bestow upon you is hands-down one of my
# favourite features of python, as it makes working with strings, and
# specifically printing strings such a breeze. Say I have a few variables

player_health = 100
player_damage_taken = 10
player_dead = player_health - player_damage_taken < 0 # False

# And say we want to print something letting the player know if they have
# survived taking this damage. The old way we know how to do it is through
# string concatenation
print("Player with " + player_health + " health takes " + 
       player_damage_taken + " damage. Player dead: " + player_dead)


# We need to add the + operator in between everything, and we also
# have to put serious thought into adding spaces inside our text or else things
# get jumbled up. Now check this out:

print(f"Player with {player_health} health takes {player_damage_taken} damage. Player dead: {player_dead}")
#     ^ Simply by adding this guy (f), we get to use curly braces to substitute
#     our variables in this string. The conversion from whatever type the
#     variable actually is to a string is also automatically done for us, and
#     we don't need to think extra hard about adding spaces to the proper
#     places since the variables are substituted in-place! f-strings are legal
#     tender in any string, not just print statements.

f_string = f"{player_health} percent"
print(f_string)

#############
# R-STRINGS #
#############

# Very often in Python you'll want to open a file on your computer. Maybe a
# text file, maybe even an mp3 file. I don't care. You'll probably do something
# like this:

fname = "\home\usr\Simon\Music\MoBambda.flac"

# and then when you use fname in some function that knows how to open files,
# things won't work. Why? Because the slashes cause some problems. It has
# something to do with slashes having some special power, we'll get to it. 
# What I'll focus on now is how to get over this hurdle.

# 1. Escape your slashes
fname = "\\home\\usr\\Simon\\Music\\MoBamba.flac"
# This amounts to doubling up your slashes which is the universal way to siphon
# the power contained within gifted characters.


# 2. Slap a funny "r" out front
fname = r"\home\usr\Simon\Music\MoBamba.flac"

# This is my favourite alternative because if you're anything like me you
# simply copy-pasted your file path into python and don't want to manually add
# slashes. I think the r stands for raw but don't quote me on that. You can
# double up on r and f out front a string to get all those features!

#####################
# ESCAPE CHARACTERS #
#####################
# TODO: If you're reading this, email me and tell me to do this. 

# Email is in chapter zero.
