

""" Player is the person playing the game who has a score

    Player class is responsible for keeping track of the score

    Attributes:
        score (int): this will be the players total score

"""


class Player:
    """ Constructs a new instance of Player with a score attribute

    Args:
        self (Player): an instance of the player

    Methods:
        Add 100 points to score if guessed correctly
        Subtract 75 points if guessed incorrectly

    """

    def __init__(self):
        self.score = 300  # Player starts the game with 300 points
        self.keep_playing = True
        self.guess = ""

    def add_points(self):
        self.score += 100
        print(f"Your score is: {self.score}")

    def subtract_points(self):
        self.score -= 75
        print(f"Your score is: {self.score}")

    def guess_next(self):
        guess_is_false_input = True
        while guess_is_false_input:
            self.guess = input("higher or lower? [h/l]")
            if self.guess.lower() == "h" or self.guess.lower() == "l":
                guess_is_false_input = False
            else:
                print('Please Write "H" for Higher card or "L" for Lower card.')

    def play_again(self):
        play_again_input_is_false = True
        while play_again_input_is_false:
            play_again = input("Play again? [y/n]")
            if play_again.lower() == "y":
                self.keep_playing = True
                play_again_input_is_false = False
            elif play_again.lower() == "n":
                self.keep_playing = False
                print("Thanks for playing!")
                play_again_input_is_false = False
            else:
                play_again_input_is_false = True
                print('Please Write "Y" for "Yes" and "N" for "No"')


""" Following lines used to test Player class. Uncomment and run player.py to test this class"""
#player = Player()
#print(f"We start with {player.score} points")
# player.add_points()
#print(f"Then we add 100 points using 'add_points()' for a total of {player.score} points")
# player.subtract_points()
#print(f"Then we subtract 75 points using 'subtract_points() for a total of {player.score} points")
