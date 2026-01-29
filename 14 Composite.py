# Already, we have used composition for our previous Card design.
# Composition just refers to recursively defining types as combinations of 
# other types. For example, a Card is a composition of a Rank and a Suit.

from Module import Card, Rank, Suit
import random

# With our Card class in hand, it is natural to want a deck of cards. Of
# course, we could model a deck of cards as a simple list of Card Objects, but
# we would be missing out on many of the features of that Object-Oriented
# Programming gives us


class Deck:
    # This function generates a full Deck of cards using the fact that we can
    # iterate over all members of an enumerated class.
    def __init__(self):
        cards = []
        for s in Suit:
            for r in Rank:
                cards.append(Card(r, s))
        self.cards = cards

    # This special method allows us to iterate over a deck directly as if it
    # was a list! Without going into too much detail, iter objects are used to
    # implement iterating over objects without indices in Python.
    def __iter__(self):
        return iter(self.cards)

    # This special method returns the length of the underling list
    # of cards.
    def __len__(self):
        return len(self.cards)

    def __str__(self):
        output = ""
        for c in self.cards:
            output += str(c) + "\n"
        return output

    """
    Draws a card off the top of the Deck (thus removing a card).
    """
    # See if you can catch a bug in this implementation.
    def draw(self) -> Card:
        return self.cards.pop()

    """
    Uses the random package to shuffle cards.
    """
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def sort(self) -> None:
        # Because we implemented the comparison methods for our Card class,
        # we automatically have access to the list class' sort() method!
        self.cards.sort()


d = Deck()

# The following is only possible thanks to __iter__
for c in d:
    print(c)
print()

d.shuffle()
print(d)

d.sort()
print(d)
