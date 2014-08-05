from random import randrange

class NewGame(object):
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds
        self.current_round = 0
        
    
class Player(object):
    def __init__(self):
        self.score = 0
        
    def win_round(self):
        self.score += 1
        
    def win_game(self):
        print("YOU WON!")
    

class ComputerPlayer(Player):
    
    def win_game(self):
        print("THE COMPUTER WON!")
        
        


def who_won(score1, score2):
    human_player_score = score1
    comp_player_score = score2
    if human_player_score > comp_player_score:
        human_player.win_game()
    if human_player_score < comp_player_score:
        comp_player.win_game()
    if human_player_score == comp_player_score:
        print ("IT WAS A TIE!")

def round():
    
    comp_choice = randrange(1, 4)
    choice = int(raw_input("Rock [1] Paper [2] Scissors [3]"))
    
    if choice == comp_choice:
        print("It was a tie.")
    elif choice == 3 and comp_choice == 2:
        print("The computer has won. Scissors cut paper.")
        comp_player.win_round()
    elif choice == 2 and comp_choice == 3:
        print ("You won. Scissors cut paper.")
        human_player.win_round()
    elif choice == 2 and comp_choice == 1:
        print ("You won. Paper covers rock.")
        human_player.win_round()
    elif choice == 1 and comp_choice == 2:
        print ("You lost to the computer. Paper covers rock.")
        comp_player.win_round()
    elif choice == 1 and comp_choice == 3:
        print ("You won. Rock smashes scissors.")
        human_player.win_round()
    elif choice == 3 and comp_choice == 1:
        print ("You lost. Rock smashes scissors.")
        comp_player.win_round()
    game.current_round += 1
    


def game_play():
    num_rounds = raw_input("How many rounds? ")
    global game
    game = NewGame(num_rounds)
    global human_player
    global comp_player
    human_player = Player()
    comp_player = ComputerPlayer()   
    while game.current_round < int(num_rounds):
        round()
        print "COMPUTER: ", comp_player.score, "HUMAN: ",human_player.score
    who_won(human_player.score, comp_player.score)
    
    

if __name__ == '__main__':
    game_play()
	
        