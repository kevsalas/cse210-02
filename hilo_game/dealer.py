from random import randint


class Dealer:

    def __init__(self):
        self.first_card = 0
        self.second_card = 0

    def pick_card_1(self):
        self.first_card = randint(1, 13)
        print(f'The card is: {self.first_card}')

    def pick_card_2(self):
        self.second_card = randint(1, 13)
        print(f'Next card was: {self.second_card}')
