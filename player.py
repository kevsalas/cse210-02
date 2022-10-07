class Player:
    """ Class Player """
    def __init__(self):
        # Initial Player points 
        self.points = 300
        # Boolean Game playing 
        self.if_playing = True

        
    def win(self):
        self.points += 100
        
    
    def lose(self):
        self.points -= 75

    """ Method to continue the game if the player wants """
    def continue_game(self):
        self.ask = input("Do you want to continue the game? ")
        if self.ask.lower() == "yes":
            self.if_playing = True
        else:
            self.if_playing = False
    

    
