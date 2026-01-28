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
    # was a list!
    def __iter__(self):
        return iter(self.cards)

    # This special method returns the length of the underling list
    # of cards.
    def __len__(self):
        return len(self.cards)

    """
    Draws a card off the top of the Deck (thus removing a card).
    """

    def draw(self) -> Card:
        return self.cards.pop()

    def shuffle(self) -> None:


d = Deck()

# The following is only possible thanks to __iter__
for c in d:
    print(c)
