import settings
import player
import random


def throw_dice(quantity=1):
    """
    Randomize dice throw.
    :param quantity: Quantity of dices thrown - integer.
    :return: Values from 1 to 6, quantity times as a list of integers.
    """
    if not isinstance(quantity, int) or quantity<1:
        raise ValueError('Need int >1 for this function')
    else:
        return [random.randint(settings.DICE_MIN, settings.DICE_MAX) for _ in range(quantity)]


def get_dice_sums(dices):
    return [sum(i) for i in dices]


def get_first_player(players):
    """
    Throws dices and prints who has the biggest value, if tie - called once again.
    :param players: List of players - list of objects.
    #TODO define if this function needs to return something, if yes - what? example: first player object adress, player index in list, player's name, etc
    """
    if all(isinstance(x, player.Player) for x in players):

        print('Rolling the dices!')
        first_dices = [throw_dice(2) for _ in range(len(players))]
        [print(f'{players[x].name} rolled {first_dices[x]}') for x in range(len(players))]
        dice_sums = get_dice_sums(first_dices)
        max_value = max(dice_sums)
        winner_values = [i for i, j in enumerate(dice_sums) if j == max_value]

        winners = {}
        for i,v in enumerate(winner_values):
            winners[players[v]] = players[v].name

        if len(winners)>1:
            print(f"It's a tie for {list(winners.values())}, they rolled {max_value}")
            get_first_player(list(winners.keys()))
        else:
            print(f'{list(winners.values())[0]} got {max_value} and goes first!')
            #return
    else:
        raise TypeError('Input must be a list of Player class objects')


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
    get_first_player(players)
    print('Players now have gold:')
    for player in players:
        print(f'{player.name} has {player.all_money} as {player.money}')
