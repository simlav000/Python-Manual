from .Rank import Rank
from .Suit import Suit


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        if not isinstance(rank, Rank):
            raise TypeError("Not a valid rank!")
        if not isinstance(suit, Suit):
            raise TypeError("Not a valid suit!")
        self.rank = rank
        self.suit = suit

    def is_face_card(self) -> bool:
        return self.rank in {"Jack", "Queen", "King"}

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __int__(self) -> int:
        return self.rank.value

    # Comparison methods
    def __eq__(self, other: "Card") -> bool:
        return (self.rank == other.rank) and (self.suit == other.suit)

    def __lt__(self, other: "Card") -> bool:
        return self.rank.value < other.rank.value

    # __eq__ and __lt__ can be used to derive the rest
    def __le__(self, other: "Card") -> bool:
        return (self < other) or (self == other)

    def __gt__(self, other: "Card") -> bool:
        return other < self

    def __ge__(self, other: "Card") -> bool:
        return (self > other) or (self == other)
