import importlib as il
import sys

class Game:
    
    def __init__(self, players: list, small_blind_amount: int, big_blind_amount: int):
        if len(players) > 2: # normal play
            self.state = {
                'players': players,
                'community cards': [],
                'bets': [],
                'small blind player': 1,
                'small blind amount': small_blind_amount,
                'big blind player': 0,
                'big blind amount': big_blind_amount
            }
            dealer = len(players)
            self.player_holes = []
            for player in players:
                self.player_holes.append([])
        else: # heads up play
            pass
            
    
    def wrapping_increment(self, n: int) -> int:
        return (n + 1) % len(self.state['players'])
            
    
            