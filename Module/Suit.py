from enum import Enum, auto


class Suit(Enum):
    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()

    def __str__(self):
        return str(self.name)[0] + str(self.name)[1:].lower()
