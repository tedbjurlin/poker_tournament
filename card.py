import enum
import functools

class Suit(enum.Flag):
    DIAMONDS = enum.auto()
    CLUBS = enum.auto()
    HEARTS = enum.auto()
    SPADES = enum.auto()

@functools.total_ordering
class Card:
    def __init__(self, rank: int, suit):
        self.rank = rank
        self.suit = suit
        
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.rank == other.rank)

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.rank < other.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"