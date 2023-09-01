from enum import Enum

class Move(Enum):
    CHECK = "Check" # Checking when there is a bet will be considered a fold
    CALL = "Call"
    FOLD = "Fold"
    ALLIN = "AllIn"
    
    @classmethod
    def RAISE(amount: int) -> int: # Amounts less than the minimum will be considered a call / check
        return int(amount)  # Amounts greater than possesed chips will be considered all in