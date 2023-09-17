from move import Move
import random

class Player:
    
    def __init__(self):
        self.name = "Random player 4"
        self.currentbet = 0
        self.minraiseamount = 0
        self.bigblindamount = 0
        # anything your bot needs to do on initialization
    
    def make_move(self):
        choice = random.randint(1, 4)
        if choice == 0:
            return Move.ALLIN
        elif choice == 1:
            return Move.CHECKORCALL
        elif choice == 2:
            return Move.FOLD
        elif choice == 3:
            ramount = random.randint(1, 10)
            return Move.RAISE(self.minraiseamount * ramount)
        
    def update(self, message):
        if message[0] == "raise" or message[0] == "all in" or message[0] == "check or call":
            if self.currentbet < message[2]:
                self.minraiseamount = message[2] - self.currentbet
                self.currentbet = message[2]
        elif message[0] == "blind amounts":
            self.bigblindamount = message[2]
            self.minraiseamount = message[2]
            self.currentbet = message[2]
        elif message[0] == "flop" or message[0] == "turn" or message[0] == "river":
            self.minraiseamount = self.bigblindamount