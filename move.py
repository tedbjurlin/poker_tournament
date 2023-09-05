from enum import Enum

class Move(Enum):
    CHECKORCALL = "Check or Call"
    FOLD = "Fold"
    ALLIN = "AllIn"
    
    @classmethod
    def RAISE(self, amount: int) -> int: # Amounts less than the minimum will be considered a call / check
        return int(amount)  # Amounts greater than possesed chips will be considered all in