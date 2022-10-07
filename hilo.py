class Player:
    current_guess = ""
    points = 300
    decision_to_keep_playing = True

    def __init__(self, points=300):
        self.points = points
