from enum import Enum, auto


class OldCard:
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

# So we've made it this far and created a Card class with some cool
# functionality. We're proud of this design and we let our friends use it.
# Then they create their first card:


my_card = OldCard("One Billion", "Slugs")
print(my_card)

# Right... so that's not supposed to be in the game. How do we prevent this?

################
# ENUMERATIONS #
################
# A deceptively powerful "genre" of class is the humble enumeration.
# Enumerations are a beautifully simply way to represent a class which
# can only be a limited number of things. As far as a Card goes, there are
# only 13 different ranks, and 4 different suits. We can enumerate them!


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

# With this enumerated class, we can also put the integer mapping directly
# in the class definition, instead of in a dictionary stored in some function.
# We can also access these values directly by doing:


print(Rank.ACE.value)

# Notice something about the Rank class: I didn't have to explicitly create an
# instance of the Rank class. It just exists for me to use. As a matter of fact
# only one such item *can* exist!

# Moving on to Suits:


class Suit(Enum):
    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()

# Here, we used a feature of the Enum Module, namely the auto() function. This
# is to be used when there is no real other meaning to be derived from the Enum
# members; when the Enum name tells the whole story.

# So why did we do this? Can Enums prevent our friend from making the One
# Billion of Slugs? Well, kind of. Let's make a new Card class:


class CardMadeOfEnums:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

# Now our constructor is hinting that it wants specifically one of the Rank
# and Suit options we enumerated above. In any compiled programming language,
# this would be enough to deter your friend. Unfortunately Python treats these
# type hints as... hints.


c4 = CardMadeOfEnums("Negative One", "Landlords")

# Don't despair! We can fight back. All we have to do is *manual input
# validation*.


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        if not isinstance(rank, Rank):
            raise TypeError("Not a valid rank!")
        if not isinstance(suit, Suit):
            raise TypeError("Not a valid suit!")
        self.rank = rank
        self.suit = suit


# Here, I used a new function "isinstance". You can
# probably guess what the latter does: it returns True if "rank" is a member
# of the "Rank" class. If it isn't we "raise" a TypeError, which completely
# crashes the program and spits out the message we gave. No more fun and games
# for your friend! We get the last laugh.

# "Why bother with any of this?", you may ask.

# This kind of defensive programming might seem overkill, but as a project
# grows, or as the hours of the day run scarce, it is nice to be able to rest
# assured that Objects that shouldn't exist aren't swimming somewhere in your
# code waiting to crash, or even worse: result in some unexpected result down
# the road. When you code like this, you ensure that Python will not allow you
# to make mistakes, and that will save you precious time and patience debugging.
