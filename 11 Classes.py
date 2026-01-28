###########
# Classes #
###########

# Variables are nice but they can only take you so far.
# Say you are programming a card game and want to represent a deck of cards.
# Variables work but... this seems tedious no?

card_1 = ("Ace of spades")
card_2 = ("Two of spades")
...
card_n = ("King of Diamonds")
# etc.

# Then, we could extract the rank and suit by doing:
card_1_rank = card_1.split(" ")[0]
card_1_suit = card_1.split(" ")[2]
print(card_1_rank)
print(card_1_suit)
# The above calls the split() function which acts on a string
# and breaks the string up into a list, with the input as the
# separator. In this case, we are breaking up by a single space
# hence " ". Thus the list becomes ["rank", "of", "suit"].

# But now imagine doing this for all 52 cards... what a pain.

# In come classes!

# Classes allow you to define a template "Card" that you can make multiple
# unique instantiations of. For example:

# It is customary to define class names using leading capital letter SuchAsThis
# This style is referred to as UpperCamelCase or PascalCase.


class Card:
    # The following function is called the constructor. It must be called
    # __init__, and the first argument it takes must be the "self" keyword.
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

# The self.rank and self.suit business is what we call setting an attribute
# for a card. This allows us to tack on a rank and suit to each card we create,
# and these are set at creation!


# With this, we can define multiple cards, for example
c1 = Card("Ace", "Spades")
c2 = Card("Two", "Clubs")

# c1 and c2 are both Card instances. Notice that despite naming the constructor
# __init__, we didn't actually write __init__ when constructing a card. This
# is because __init__ works in the background. Every time you have a class, it
# has an __init__ function, and when you construct an object of some class
# "ClassName", python is secretly doing ClassName.__init__().

# One advantage of this class is that we no longer have to do some fancy string
# splitting to get the rank and suit. We can access this information directly
# from their attributes!

print(c2.rank)
print(c2.suit)

# Seeing this might help you understand what "self.rank" meant when we wrote it
# in the constructor. In this case, "self" here is c2.

# Another advantage to packaging all this information into a class is that
# we don't have to pass ranks and suits explicitly to some function
# which may need it. Instead, all we have to do is pass as input the Card
# and the function will be able to access these values.


# We can flesh-out this class a bit more by adding some logic for our
# Cards
class Card2:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    # This "function" is referred to as a "method" of the Card class.
    def is_face_card(self) -> bool:
        return self.rank in {"Jack", "Queen", "King"}

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __int__(self) -> int:
        rank_to_int: dict[str, int] = {
            "Ace": 1,
            "Two": 2,
            "Ten": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13
        }
        return rank_to_int[self.rank]


c3 = Card2("Queen", "Hearts")

# Now, we've enabled Card2 objects to answer questions about themselves. Maybe
# your game needs to check if a card is a face card often. Now, all you have to
# do is ask

if c3.is_face_card():
    print("Face card accepted")

# We also implemented a __str__ method. This is a special method, because while
# you can use it similarly to is_face_card(), e.g.

c3_description = c3.__str__()
print(c3_description)

# It also automatically is called whenever you call print() on one of your cards!
print(c3)

# Lastly, we implemented a __int__ method, which is also special, and is called
# automatically when we try to convert a Card2 into an int

print(int(c3))

# As you can already tell, anything with __something__ is special, and we like
# to call these "double underscore" methods as "dunder" methods.
