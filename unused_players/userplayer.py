from move import Move

class Player:
    
    def __init__(self):
        self.name = input("What is your name? -> ")
    
    def make_move(self):
        while True:
            choice = input(f'{self.name} - Would you like to:\n1. Check or Call\n2. All In\n3. Fold\n4. Raise\n\nEnter a number from 1 to 4. -> ')
        
            if choice == "1":
                return Move.CHECKORCALL
            elif choice == "2":
                return Move.ALLIN
            elif choice == "3":
                return Move.FOLD
            elif choice == "4":
                bet = input("How much would you like to bet? -> ")
                if bet.isdigit():
                    return int(bet)
                else:
                    print("Please enter an integer.")
        
    def update(self, message):
        print(f"{self.name}: {message}")
        # this function is called whenever something happens
        # use it to update your bot on the state of the game