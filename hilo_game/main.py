from dealer import Dealer
from player import Player


def main():
    dealer = Dealer()
    player = Player()

    while player.keep_playing and player.score > 0:
        dealer.pick_card_1()
        player.guess_next()
        dealer.pick_card_2()
        if (dealer.first_card < dealer.second_card and player.guess == "h"):
            player.add_points()
        elif (dealer.first_card > dealer.second_card and player.guess == "l"):
            player.add_points()
        else:
            player.subtract_points()
        player.play_again()


if __name__ == "__main__":
    main()
