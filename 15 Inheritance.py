# Maybe we're happy with our Deck class, but we quickly realize that in our
# game, we will need a Hand, and a DiscardPile, and all of these also look a 
# lot like a list of Cards. It would be a shame if we had to re-make a bunch
# of classes that all have the same basic structure...

# This is what Inheritance solves. Instead of jumping directly into making a 
# Deck and Hand class, let's make a more abstract CardCollection class

from Module import Card, Rank, Suit
# Here, abc means Abtract Base Class
from abc import ABC
from typing import Iterable, Optional


class CardCollection(ABC):
    # Here, we are saying that a CardCollection is created optionally as a
    # some collection (Iterable) of Cards, or we pass nothing, and we
    # implement that if we pass nothing, the cards list is empty []
    def __init__(self, cards: Optional[Iterable[Card]] = None):
        self.cards: list[Card] = list(cards) if cards is not None else []

    # Then, we implement the absolute minimum functionality for a
    # CardCollection. This should be all the functions we need from ALL
    # subclasses which will be inheriting this. You will notice, for example,
    # that there is no draw() function, because in my game, you cannot draw
    # from a hand... you draw from a DiscardPile, or a Deck, but those drawn
    # cards should go INTO the hand.
    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        output = ""
        for c in self.cards:
            output += str(c)
        return output

    # Depending on the application, we can even say this is unnecessary, since
    # while we shall be adding cards to hand, and to the DiscardPile, maybe we
    # won't be adding cards to the Deck. Maybe we will. It depends on your game.
    def add(self, card: Card) -> None:
        self.cards.append(card)

    def sort(self) -> None:
        self.cards.sort()

    def isEmpty(self) -> bool:
        return len(self.cards) == 0


class Deck(CardCollection):
    # Here, we claim that our Deck constructor should delegate its job to the
    # supercalss' constructor (hence super()), but with it a list of all cards
    # passed as input.
    def __init__(self):
        super().__init__(
            [Card(r, s) for s in Suit for r in Rank]
        )

    # Here, we implement drawing from the deck, and we use the inherited
    # isEmpty() functionality defined in the superclass.
    def draw(self) -> Optional[Card]:
        if self.isEmpty():
            return None
        return self.cards.pop()

class Hand(CardCollection):
    def discard(self, card: Card) -> Optional[Card]:
        if card not in self.cards:
            return None
        self.cards.remove(card)
        return card

class DiscardPile(CardCollection):
    def draw(self) -> Optional[Card]:
        if self.isEmpty():
            return None
        return self.cards.pop()

d = Deck()
h = Hand()
p = DiscardPile()

print(f"Size of deck: {len(d)}")

c = d.draw()
if c is not None:
    h.add(c)

    print(f"Size of deck: {len(d)}")
    print(f"Hand: {h}\n", f"Discard Pile: {p}")

    c2 = h.discard(c)
    if c2 is not None:
        p.add(c2)

    print(f"Hand: {h}\n", f"Discard Pile: {p}")

# One of the rules I am following here is that objects (Hand, Deck, etc.) are
# removing from their own state (draw from deck, discard from hand) and offering
# the cards to others. You could do something like discardpile.take_from(hand)
# but this is unclean, since it makes it difficult to track the internal state
# of the hand. What if I want to implement Uno? Then I need to keep track of
# hand size to determine who wins, and if the discard pile is stealing from the
# hand, I have to be very careful with *how* it does this. It is better for
# Hand to manage itself, and keep an internal counter that it decrements each
# time it discards.

# When a class manages its own internal state, it is much easier to reason 
# about it, and it will avoid many bugs.
