from move import Move

class Player:
    
    # continue play without betting
    # if there is already a bet that round, then checking will be considered folding
    def check(): 
        return Move.CHECK
    
    # match the current bet
    # if there is no bet then calling will be considered the same as checking
    def call():
        return Move.CALL
    
    # bet all of your money
    def goAllIn():
        return Move.ALLIN
    
    # stop playing the current hand
    # any money already bet will be lost, but you won't lose any more
    def fold():
        return Move.FOLD
    
    # raise the bet by the given amount
    # if the amount raised is less than the minimum, it will be considered a call
    # if it is more than the amount of money you possess, it will be considered going all in
    def raiseBet(amount: int):
        return Move.RAISE(amount)
    
    def make_move(game_state: dict):
        return fold()
        # implement your bot here
        # feel free to make helper functions