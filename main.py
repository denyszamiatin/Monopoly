import settings
import player
import random
from collections import deque


def throw_dice() ->list[int]:
    """
    Randomize dice throw.
    :return: Values from 1 to 6, quantity times as a list of integers.
    """
    count = 0
    while True:
        if count < 3:
            rand_list = [random.randint(settings.DICE_MIN, settings.DICE_MAX) for _ in range(settings.DICE_AMOUNT)]
            if len(rand_list) == len(set(rand_list)):
                return rand_list
            else:
                count += 1
                return rand_list
        else:
            """ TODO: create field jail and using function move, put player into jail."""
            pass


def get_dice_sums(dices):
    return [sum(i) for i in dices]


def get_first_player(players: list[player.Player]):
    """
    Throws dices and returns adress of the Player object who has the biggest value, if tie - called again.
    :param players: List of players - list of objects.
    :return: Adress of Player object.
    """
    if all(isinstance(x, player.Player) for x in players):
        print('Rolling the dices!')
        first_dices = [throw_dice() for _ in range(len(players))]
        [print(f'{players[x].name} rolled {first_dices[x]}') for x in range(len(players))]
        dice_sums = get_dice_sums(first_dices)

        max_value = max(dice_sums)
        winner_values = [i for i, j in enumerate(dice_sums) if j == max_value]

        winners = {}
        for i,v in enumerate(winner_values):
            winners[players[v]] = players[v].name

        if len(winners)>1:
            print(f"It's a tie for {list(winners.values())}, they rolled {max_value}")
            return get_first_player(list(winners.keys()))
        else:
            print(f'{list(winners.values())[0]} got {max_value} and goes first!')
            return (list(winners.keys())[0])
    else:
        raise TypeError('Input must be a list of Player class objects')


def sort_player_list(players: list[player.Player],first_player: player.Player):
    """
    Sorts player list so first player is first in the list.
    :param players: List of players - list of objects.
    :param first_player: Player object.
    :return: Adress of Player object.
    """
    index = players.index(first_player)
    items = deque(players)
    items.rotate(-index)
    print(f'Player order is : {[item.name for item in items]}')
    return items


def input_players_qty() -> int:
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


def input_player_names(quantity: int) -> list[player.Player]:
    """
    Ask players names and create objects of class Player for each of them.
    :param quantity: Quantity of players for particular game - integer.
    :return: List of players.
    """
    player_list = [player.Player(input('What is your name? ')) for _ in range(quantity)]
    return player_list


def find_position(name):
    """
    Asks player name and changes his position.
    :param name: Player`s name.
    :return: Player`s new position after a dice roll.
    #TODO implement order of players
    """
    name.field += sum(throw_dice())
    if name.field > 40:
        name.field = abs(40 - name.field)
    print(name)
    return name.field


if __name__ == '__main__':
    players_qty = input_players_qty()
    players = input_player_names(players_qty)
    first_player = get_first_player(players)
    players = sort_player_list(players,first_player)
    print('Players now have gold:')
    for player in players:
        print(f'{player.name} has {player.all_money} as {player.money}')
    order = 0
    find_position(players[order])