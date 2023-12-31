import importlib
import importlib.util
import os
from copy import deepcopy
from card import Card
from move import Move
from pokerkit import (
    Automation,
    NoLimitTexasHoldem
)

class Game:

    def __init__(self, players: list, stacks, remaining_at_end):
        # The list of Player objects currently in the game.
        self.players = players
        
        # The names of the players currently in the game.
        self.names = [p.name for p in self.players]
        
        # The amount of money each player has.
        self.stacks = stacks
        
        # The number of players that have to be left to end the game.
        self.remaining_at_end = remaining_at_end
        
        # The hand number.
        self.hand_n = 1
        
        # The blind structure. The blind will increase every five hands.
        self.blinds = [
            (25, 50),
            (50, 100),
            (75, 150),
            (100, 200),
            (125, 250),
            (200, 400),
            (300, 600),
            (500, 1000),
            (700, 1400),
            (1000, 2000),
            (1500, 3000),
            (3000, 6000),
            (4000, 8000),
            (6000, 12000),
            (10000, 20000),
            (15000, 30000),
        ]
        
        self.general_update(("game start"))
        self.general_update(("remaining", self.remaining_at_end))     
            
    # This function sends the given message to every player in the game.
    def general_update(self, message):
        for player in players:
            player.update(message)
            
    # Runs a single round of betting. The state is the current game state and
    # the street_index indicates which round of betting it is.
    def run_bets(self, state, street_index):
        while state.street_index == street_index:
            move = self.players[state.actor_index].make_move()
            if type(move) is int:
                if state.can_complete_bet_or_raise_to(move):
                    self.general_update(("raise", self.names[state.actor_index], move))
                    state.complete_bet_or_raise_to(move)
                    
                else:
                    self.general_update(("check or call", self.names[state.actor_index], max(state.bets)))
                    state.check_or_call()

            elif move == Move.ALLIN:
                self.general_update(("all in", self.names[state.actor_index], state.bets[state.actor_index] + state.stacks[state.actor_index]))
                try:
                    state.complete_bet_or_raise_to(state.bets[state.actor_index] + state.stacks[state.actor_index])
                except ValueError:
                    state.check_or_call()
                
            elif move == Move.CHECKORCALL:
                self.general_update(("check or call", self.names[state.actor_index], max(state.bets)))
                state.check_or_call()
                
            elif move == Move.FOLD:
                if state.can_fold():
                    self.general_update(("fold", self.names[state.actor_index]))
                    state.fold()
                else:
                    self.general_update(("check or call", self.names[state.actor_index], max(state.bets)))
                    state.check_or_call()
                
            else:
                if state.can_fold():
                    self.general_update(("fold", self.names[state.actor_index]))
                    state.fold()
                else:
                    self.general_update(("check or call", self.names[state.actor_index], max(state.bets)))
                    state.check_or_call()
        
    # Runs a full game (or table) of poker, until the given win condition is met.
    def play_game(self):
        while len(self.players) > self.remaining_at_end:
            self.play_hand()
            
            # removing any players that went out
            to_remove = []
            for i in range(len(self.stacks)):
                if self.stacks[i] <= 0:
                    to_remove.insert(0, i)
            
            for i in to_remove:
                self.stacks.pop(i)
                self.players.pop(i)
            
            self.stacks.append(self.stacks.pop(0))
            self.players.append(self.players.pop(0))
            
            self.names = [p.name for p in self.players]
            
        self.general_update(("game end"))
        self.general_update(("winners", self.names.copy()))
    
    # Plays a single hand of poker, including setup, betting, and money distribution.
    def play_hand(self):
        
        # creating the pokerkit state for this hand
        state = NoLimitTexasHoldem.create_state(
            (
                Automation.ANTE_POSTING,
                Automation.BET_COLLECTION,
                Automation.CARD_BURNING,
                Automation.BOARD_DEALING,
                Automation.HOLE_CARDS_SHOWING_OR_MUCKING,
                Automation.HAND_KILLING,
            ),
            True,
            0,
            self.blinds[self.hand_n // 5],
            self.blinds[self.hand_n // 5][1],
            self.stacks,
            len(self.players)
        )
        
        # setting blinds
        blinds = []
        for index in state.blind_or_straddle_poster_indices:
            blinds.append(state.post_blind_or_straddle(index))
        
        # dealing hole cards
        hole_cards = [[] for _ in self.players]
        while state.can_deal_hole():
            hole = state.deal_hole()
            hole_cards[hole.player_index].append(hole.cards[0])
        
        small_blind_player = ""
        big_blind_player = ""
        
        # getting names of blind players, accounting for the differences when
        # are only two players left
        if blinds[0].amount < blinds[1].amount:
            small_blind_player = self.names[blinds[0].player_index]
            big_blind_player = self.names[blinds[1].player_index]
        else:
            small_blind_player = self.names[blinds[1].player_index]
            big_blind_player = self.names[blinds[0].player_index]
        
        # notifying players of how the game has been set up
        for i in range(len(players)):
            players[i].update(("hand", self.hand_n))
            players[i].update(("players", self.names.copy()))
            players[i].update(("stacks", state.starting_stacks))
            players[i].update(("blind amounts", self.blinds[self.hand_n // 5][0], self.blinds[self.hand_n // 5][1]))
            players[i].update(("blind players", small_blind_player, big_blind_player))
            players[i].update(("hole cards", [Card.from_pokerkit(hole_cards[i][0]), Card.from_pokerkit(hole_cards[i][1])]))
        
        # pre-flop bets
        self.run_bets(state, 0)
        
        
        try:
            # flop dealing
            self.general_update(("flop", [
                Card.from_pokerkit(state.board_cards[0]),
                Card.from_pokerkit(state.board_cards[1]),
                Card.from_pokerkit(state.board_cards[2])]))
            
            # second round of bets
            self.run_bets(state, 1)
        except IndexError:
            pass
        
        try:
            # turn dealing
            self.general_update(("turn", Card.from_pokerkit(state.board_cards[3])))
            
            # third round of bets
            self.run_bets(state, 2)
        except IndexError:
            pass
        
        try:
            # river dealing
            self.general_update(("river", Card.from_pokerkit(state.board_cards[4])))
            
            # final round of bets
            self.run_bets(state, 3)
        except IndexError:
            pass
        
        # the cards each player had
        # in tournament play, some losing players would often toss their cards
        # without revealing them. However, I thouth it would be more interesting if all
        # of the cards were revealed after every hand, even folds.
        self.general_update(("reveal", [[Card.from_pokerkit(card) for card in hole] for hole in hole_cards]))
        
        # dividing pot
        winnings = list(state.push_chips().amounts)
        self.general_update(("winnings", winnings))
        while any(state.chips_pulling_statuses):
            state.pull_chips()
                            
        self.hand_n += 1

        self.stacks = state.stacks.copy()

# dynamic import code from https://stackoverflow.com/questions/57878744/how-do-i-dynamically-import-all-py-files-from-a-given-directory-and-all-sub-di
# ignore the next three funtions

def get_py_files(src):
    cwd = os.getcwd() # Current Working directory
    py_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(cwd, root, file))
    return py_files


def dynamic_import(module_name, py_path):
    module_spec = importlib.util.spec_from_file_location(module_name, py_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def dynamic_import_from_src(src):
    my_py_files = get_py_files(src)
    modules = []
    for py_file in my_py_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_module = dynamic_import(module_name, py_file)
        modules.append(imported_module)
    return modules

if __name__ == "__main__":
    modules = dynamic_import_from_src("players")
    
    players = []
    for module in modules:
        players.append(module.Player())
        
    print(players)
    
    # set the starting stacks here
    stacks = [1000 for _ in range(len(players))]
    game = Game(players, stacks, 1)
    
    game.play_game()
    
    print(game.players[0].name)
    