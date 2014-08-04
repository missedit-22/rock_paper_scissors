from random import randrange

class NewGame(object):
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.round = 0
        self.player_score = 0
        self.comp_score = 0 
        
    def turn(self):
        while self.round < int(self.num_rounds):
            self.comp_choice = randrange(1, 4)
            print(self.comp_choice)
            self.choice = int(raw_input("Rock? [1] Paper? [2] Scissors? [3]"))
            self.round += 1
            game.who_won(self.choice, self.comp_choice)
            print(self.player_score, self.comp_score)
        game.final_score(self.player_score, self.comp_score)
                
                    
    def who_won(self, choice, comp_choice):
        self.choice = choice
        self.comp_choice = comp_choice
        if self.choice == self.comp_choice:
            print("It was a tie.")
        elif self.choice == 3 and self.comp_choice == 2:
            print("The computer has won. Scissors cut paper.")
            self.comp_score += 1
        elif self.choice == 2 and self.comp_choice == 3:
            print ("You won. Scissors cut paper.")
            self.player_score += 1
        elif self.choice == 2 and self.comp_choice == 1:
            print ("You won. Paper covers rock.")
            self.player_score += 1
        elif self.choice == 1 and self.comp_choice == 2:
            print ("You lost to the computer. Paper covers rock.")
            self.comp_score += 1
        elif self.choice == 1 and self.comp_choice == 3:
            print ("You won. Rock smashes scissors.")
            self.player_score += 1
        elif self.choice == 3 and self.comp_choice == 1:
            print ("You lost. Rock smashes scissors.")
            self.comp_score += 1
    
    def final_score(self, player_score, comp_score):
        self.player_score = player_score
        self.comp_score = comp_score
        if self.player_score > self.comp_score:
            print("You beat the computer!")
        if self.comp_score > self.player_score:
            print("You lost to the computer!")
        if self.comp_score == self.player_score:
            print("It was a tie!")  
            
def start_menu():
    num_rounds = raw_input("How many rounds?")
    global game
    game = NewGame(num_rounds)
    game.turn()
    
start_menu()

