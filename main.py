import settings
import player
from random import randint

def throw_dice(quantity=1):
    """
    Randomize dice throw.
    :param quantity: Quantity of dices thrown - integer.
    :return: Values from 1 to 6, quantity times as a list of integers.
    """
    if not isinstance(quantity, int) or quantity<1:
        raise ValueError('Need int >1 for this function')
    else:
        return [randint(1, 6) for _ in range(quantity)]

def input_players_qty():
    """
    Ask players quantity from user. Allowed from MIN_PLAYERS_NUMBER to MAX_PLAYERS_NUMBER from settings.
    :return: Quantity of players as integer.
    """
    while True:
        try:
            qty = int(input(f'Enter player q-ty: {settings.MIN_PLAYERS_NUMBER}-{settings.MAX_PLAYERS_NUMBER}\n'))
            if settings.MIN_PLAYERS_NUMBER <= qty <= settings.MAX_PLAYERS_NUMBER:
                return qty
        except ValueError:
            pass
        print('Wrong q-ty!')


def input_player_names(quantity):
    """
    Ask players names and create objects of class Player for each of them.
    :param quantity: Quantity of players for particular game - integer.
    :return: List of players.
    """
    player_list = [player.Player(input('What is your name? ')) for _ in range(quantity)]
    return player_list


if __name__ == '__main__':
    players_qty = input_players_qty()
    players = input_player_names(players_qty)

