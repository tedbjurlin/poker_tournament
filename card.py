import enum
import functools

class Suit(enum.StrEnum):
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
        return f"{self.rank} of {self.suit.value}"
    
    def __repr__(self):
        return f"{self.rank} of {self.suit.value}"
    
    def from_pokerkit(card: str):
        rank = card.rank.value
        suit = card.suit.value
        try:
            rank = int(rank)
        except:
            if rank == "T":
                rank = 10
            elif rank == "J":
                rank = 11
            elif rank == "Q":
                rank = 12
            elif rank == "K":
                rank = 13
            elif rank == "A":
                rank = 14
        
        if suit == "h":
            suit = Suit.HEARTS
        elif suit == "d":
            suit = Suit.DIAMONDS
        elif suit == "s":
            suit = Suit.SPADES
        elif suit == "c":
            suit = Suit.CLUBS
        
        return Card(rank, suit)